import json
import boto3
import time
import subprocess

def exec_cmd(cmd):
    result = subprocess.run(
        cmd.split(" "),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    result = result.stdout.decode()
    print(result)
    return result 

def get_client(service):
    client = boto3.client(service)
    return client

def create_account():
    client = get_client('servicecatalog')
    
    # get product id which is account factory.
    res = client.search_products_as_admin()
    product_id = res['ProductViewDetails'][0]['ProductViewSummary']['ProductId']
    print('product_id:{}'.format(product_id))
    
    # get provisioning artifact id which is account factory.
    res = client.describe_product_as_admin(Id=product_id)
    provisioning_artifact_id = res['ProvisioningArtifactSummaries'][0]['Id']
    print('provisioning_artifact_id:{}'.format(provisioning_artifact_id))

    # debug
    #client = boto3.client('sts')
    #account_id = client.get_caller_identity()["Account"]
    #print(account_id)

    # get list launch path which is account factory.
    # error
    ll_path = exec_cmd('./aws servicecatalog list-launch-paths --product-id {}'.format(product_id.replace('\n','').replace(' ','')))
    ll_path = ll_path['LaunchPathSummaries'][0]['Id']
    print('ll_path:{}'.format(ll_path))

def lambda_handler(event, context):
    #cmd = 'chmod +x ./aws'
    #result = subprocess.run(
    #    cmd.split(" "),
    #    stdout=subprocess.PIPE,
    #    stderr=subprocess.STDOUT
    #)
    #print(result.stdout.decode())
    
    #exec_cmd('ls -l')
    
    create_account()

