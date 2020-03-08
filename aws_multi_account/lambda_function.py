from datetime import datetime
from botocore.exceptions import ClientError
import urllib.parse
import boto3
import random
import subprocess
import yaml
import time
import base64
import zlib
import json
import logging
import sys
import ast
import urllib.request

def get_client(service):
    client = boto3.client(service)
    return client

def transform_to_json(event):
    data = zlib.decompress(base64.b64decode(event['awslogs']['data']), 16+zlib.MAX_WBITS)
    data_json = json.loads(data)
    log_json = json.loads(json.dumps(data_json["logEvents"][0], ensure_ascii=False))
    return log_json

def get_yaml_file(event):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    s3 = boto3.resource('s3')
    file_path = '/tmp/' + key
 
    try:
        bucket = s3.Bucket(bucket)
        bucket.download_file(key, file_path)
        print(subprocess.run(["ls", "-l", "/tmp"], stdout=subprocess.PIPE))
    except Exception as e:
        print(e)
    
    f = open(file_path, "r+")
    data = yaml.load(f)
    return data

def check_provisoned_product_status(account_name):
    client = get_client('servicecatalog')
    res = client.search_provisioned_products(
        Filters={
            'SearchQuery':['name:{}'.format(account_name)]
        }
    )
    try:
        status_message = res['ProvisionedProducts'][0]['StatusMessage']
    except KeyError:
        status_message = ' '
    
    if res['ProvisionedProducts'][0]['Status'] == 'ERROR':
        message_to_slack('ERROR---{}'.format(status_message))
        print('failed creating account')
    elif res['ProvisionedProducts'][0]['Status'] == 'AVAILABLE':
        message_to_slack('AVAILABLE---{}'.format(status_message))
    elif res['ProvisionedProducts'][0]['Status'] == 'UNDER_CHANGE':
        message_to_slack('UNDER_CHANGE---{}'.format(status_message))
    else:
        # another message
        message_to_slack('{}---{}'.format(res['ProvisionedProducts'][0]['Status'],status_message))

def message_to_slack(message):
    send_data = {"text": message}
    send_text = "payload=" + json.dumps(send_data)
    request = urllib.request.Request(
        "https://~~~~~~~~~~~~", 
        data=send_text.encode("utf-8"), 
        method="POST"
    )
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
    print(message)

def create_account(yaml_file):
    client = get_client('servicecatalog')
    
    # get product id at account factory
    res = client.search_products_as_admin()
    product_id = res['ProductViewDetails'][0]['ProductViewSummary']['ProductId']
    print('product_id:{}'.format(product_id))
    
    # get provisioning artifact id at account factory
    res = client.describe_product_as_admin(Id=product_id)
    pa_id = res['ProvisioningArtifactSummaries'][0]['Id']
    print('provisioning_artifact_id:{}'.format(pa_id))
    
    # get product path
    res = client.list_launch_paths(ProductId=product_id)
    ll_path = res['LaunchPathSummaries'][0]['Id']
    print(ll_path)

    account_name = yaml_file['spec'][0]['name']
    ou_env = yaml_file['spec'][0]['Env']

    try:
        res = client.provision_product(
            ProductId=product_id,
            ProvisioningArtifactId=pa_id,
            ProvisionedProductName=account_name,
            PathId=ll_path,
            ProvisioningParameters=[
                {'Key': 'SSOUserEmail','Value': '~~~+{}@gmail.com'.format(account_name)},
                {'Key': 'AccountEmail','Value': '~~~+{}@gmail.com'.format(account_name)},
                {'Key': 'SSOUserFirstName','Value': account_name},  
                {'Key': 'SSOUserLastName','Value': account_name},
                {'Key': 'AccountName','Value': account_name},
                {'Key': 'ManagedOrganizationalUnit', 'Value': ou_env}]
            )
    except ClientError as e:
        message_to_slack(e)
        return e

    time.sleep(15)
    check_provisoned_product_status(account_name) # throw message error or under_change
    return res

def lambda_handler(event, context):
    # separate s3 from cwl which is event type.
    try:
        event_type = event['Records'][0]['eventSource']
    except KeyError:
        event = transform_to_json(event)
        print(event)
        event_type = 'aws:cwl'
    
    if event_type == 'aws:s3':
        yaml_file = get_yaml_file(event)
        pp_status = create_account(yaml_file) # get provisioned_product status
    elif event_type == 'aws:cwl':
        print(event)
        account_name = ast.literal_eval(event['message'])
        print(type(account_name))
        account_name = account_name['serviceEventDetails']['createManagedAccountStatus']['account']['accountName']
        print('account_name : {}'.format(account_name))
        check_provisoned_product_status(account_name)