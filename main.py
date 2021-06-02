# Analyzes text in a document stored in an S3 bucket. Display polygon box around text and angled text
from dotenv import load_dotenv
from PIL import Image, ImageDraw

from analyzer import Analyzer
from visualization import *

import os

load_dotenv()

if __name__ == "__main__":
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    region_name = os.environ.get("REGION_NAME")

    bucket = os.environ.get("BUCKET")
    image_name = os.environ.get("IMAGE_NAME")

    analyzer_obj = Analyzer(aws_access_key_id, aws_secret_access_key, region_name)
    stream, blocks = analyzer_obj.analyze_image(bucket, image_name)

    image = Image.open(stream)

    width, height = image.size
    draw = ImageDraw.Draw(image)
    print('Detected Document Text')

    # Create image showing bounding box/polygon the detected lines/text
    for block in blocks:

        DisplayBlockInformation(block)

        draw = ImageDraw.Draw(image)
        if block['BlockType'] == "KEY_VALUE_SET":
            if block['EntityTypes'][0] == "KEY":
                ShowBoundingBox(draw, block['Geometry']['BoundingBox'], width, height, 'red')
            else:
                ShowBoundingBox(draw, block['Geometry']['BoundingBox'], width, height, 'green')

        if block['BlockType'] == 'TABLE':
            ShowBoundingBox(draw, block['Geometry']['BoundingBox'], width, height, 'blue')

        if block['BlockType'] == 'CELL':
            ShowBoundingBox(draw, block['Geometry']['BoundingBox'], width, height, 'yellow')
        if block['BlockType'] == 'SELECTION_ELEMENT':
            if block['SelectionStatus'] == 'SELECTED':
                ShowSelectedElement(draw, block['Geometry']['BoundingBox'], width, height, 'blue')

    # Display the image
    image.show()