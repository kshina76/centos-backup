import boto3
import botocore

# get new account credentials
def assume_role(account_id, account_role):
    sts_client = boto3.client('sts')
    role_arn = 'arn:aws:iam::' + account_id + ':role/' + account_role
    assuming_role = True
    while assuming_role is True:
        try:
            assuming_role = False
            assumedRoleObject = sts_client.assume_role(
                RoleArn=role_arn,
                RoleSessionName="NewAccountRole"
            )
        except botocore.exceptions.ClientError as e:
            assuming_role = True
            print(e)
            print("Retrying...")
            time.sleep(60)

    # From the response that contains the assumed role, get the temporary
    # credentials that can be used to make subsequent API calls
    return assumedRoleObject['Credentials']

# get new account session from credentials
credentials = assume_role(account_id, accountrole)
session = Session(aws_access_key_id=credentials['AccessKeyId'],
                  aws_secret_access_key=credentials['SecretAccessKey'],
                  aws_session_token=credentials['SessionToken'],
                  region_name=REGION_NAME)

# switch to new account
client = session.client('sts')

# TO DO. creating same process which is creating new account from account factory. 
