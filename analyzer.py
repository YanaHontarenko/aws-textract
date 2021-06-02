import boto3
import io


class Analyzer:

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.s3_resource = boto3.resource('s3',
                                          aws_access_key_id=aws_access_key_id,
                                          aws_secret_access_key=aws_secret_access_key,
                                          region_name=region_name)
        self.textract_client = boto3.client('textract',
                                          aws_access_key_id=aws_access_key_id,
                                          aws_secret_access_key=aws_secret_access_key,
                                          region_name=region_name)

    def _get_data_from_bucket(self, bucket, image_name):
        s3_object = self.s3_resource.Object(bucket, image_name)
        s3_response = s3_object.get()
        stream = io.BytesIO(s3_response['Body'].read())
        image_binary = stream.getvalue()
        return stream, image_binary

    def analyze_image(self, bucket, image_name):
        stream, image_binary = self._get_data_from_bucket(bucket, image_name)
        response = self.textract_client.analyze_document(Document={'Bytes': image_binary},
                                                         FeatureTypes=["TABLES", "FORMS"])
        blocks = response['Blocks']
        return stream, blocks