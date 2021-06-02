## This is repository for basic interaction with [Amazon Textract](https://console.aws.amazon.com/frauddetector/home)
### Prerequisites
#### Create an AWS account
1. Open https://aws.amazon.com and then choose Create an AWS Account.
2. Follow the on-screen instructions to complete the account creation. Note your 12-digit AWS account number.
#### Create an IAM user and assign required permissions
To use Amazon Fraud Detector, you have to set up permissions that allow access to the Amazon Fraud Detector console and API operations. You also have to allow Amazon Fraud Detector to perform tasks on your behalf and to access resources that you own.
The following describes how to create an IAM user and assign the needed permissions.
1. Open the [IAM console](https://console.aws.amazon.com/iam/).
2. In the navigation panel, choose **Users** and then choose **Add user**.
3. For **User name**, enter **_AmazonTextractUser_**.
4. Select the **AWS Management Console access** and **Programmatic access** check boxes, and then configure the user’s password.
5. (Optional) By default, AWS requires the new user to create a new password when ﬁrst signing in. You can clear the check box next to **User must create a new password at next sign-in** to allow the new user to reset their password after they sign in.
6. Choose **Next: Permissions**.
7. Choose **Create group**.
8. For **Group name** enter _**AmazonTextractGroup**_.
9. In the policy list, select the check box for **AmazonTextractFullAccess** and **AmazonS3ReadOnlyAccess**. Choose **Create group**.
10. In the list of groups, select the check box for your new group. Choose **Refresh** if necessary to see the group in the list.
11. Choose **Next: Tags**.
12. (Optional) Add metadata to the user by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM Users and Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html).
13. Choose **Next: Review** to see the **User details** and **Permissions summary** for the new user. When you are ready to proceed, choose **Create user**.
14. After this you will see credentials for this user - better to save it. You will need it further.
### Environment creation
#### 1. First of all, download and install python for you OS. 
#### 2. Next step is installing virtual environment library. 
```
pip install virtualenv
```
#### 3. Create and activate virtual environment:
```
python -m venv path-to-venv-folder
source path-to-venv-folder/bin/activate
```
#### 4. Install all requirements 
```
pip install -r requirements.txt
```
#### 5. Create `.env` file
```
sudo mv .env_template .env
```
#### 6. Fill `.env` file with right data.
### Use Amazon Fraud Detector
With using script, which you can find below, you can run text extraction and visualization of the results.
```
python main.py
```
### Useful notes about performance
Average time of reading data from s3 and its processing take `~6 seconds`,  depending on size of the image and text on it.

