import json
import boto3
import botocore
import time

def get_client(service):
    client = boto3.client(service)
    return client

def create_account():
    client = get_client('servicecatalog')
    
    # get product id at account factory
    res = client.search_products_as_admin()
    product_id = res['ProductViewDetails'][0]['ProductViewSummary']['ProductId']
    print('product_id:{}'.format(product_id))
    
    # get provisioning artifact id at account factory
    res = client.describe_product_as_admin(Id=product_id)
    provisioning_artifact_id = res['ProvisioningArtifactSummaries'][0]['Id']
    print('provisioning_artifact_id:{}'.format(provisioning_artifact_id))
    
    # get product path
    res = client.list_launch_paths(ProductId=product_id)
    ll_path = res['LaunchPathSummaries'][0]['Id']
    print('ll_path:{}'.format(ll_path))

    # create account
    try:
        res = client.provision_product(
                                    ProductId=product_id,
                                    ProvisioningArtifactId=provisioning_artifact_id,
                                    ProvisionedProductName='piyopiyo',
                                    PathId=ll_path,
                                    ProvisioningParameters=[
                                        {
                                            'Key': 'SSOUserEmail',
                                            'Value': 'hoge+hoge@gmail.com'
                                        },
                                        {
                                            'Key': 'AccountEmail',
                                            'Value': 'hoge+hoge@gmail.com'
                                        },
                                        {
                                            'Key': 'SSOUserFirstName',
                                            'Value': 'hoge'
                                        },  
                                        {
                                            'Key': 'SSOUserLastName',
                                            'Value': 'piyo'
                                        },
                                        {
                                            'Key': 'AccountName',
                                            'Value': 'hogepiyo'  
                                        },
                                        {
                                            'Key': 'ManagedOrganizationalUnit',
                                            'Value': 'Custom'
                                        }
                                    ])
    except botocore.exceptions.ClientError as e:
        print("In the except module. Error : {}".format(e))

# get provisioned product status
def describe_status():
    client = get_client('servicecatalog')
    count = 0
    while(True):
        if count == 10:
            # TO DO. creating another lambda which is describe process.
            print('reach lambda limit.')
            break
        res = client.search_provisioned_products(
                Filters={
                    'SearchQuery':['name:tenantB_1']
                }
            )
        pp_status = res['ProvisionedProducts'][0]['Status']
        print(pp_status)
        if pp_status == 'UNDER_CHANGE':
            # TO DO. throw the message at slack
            print('creating account...')
            time.sleep(60)
        elif pp_status == 'ERROR':
            # TO DO. throw the message at slack
            # TO DO. delete failed account process
            print('create account process failed.')
            break
        elif pp_status == 'AVAILABLE':
            # TO DO. throw the message at slack
            print('creating accout successfully.')
            break
        else:
            print(pp_status)
        count += 1
    
def lambda_handler(event, context):
    create_account()
    time.sleep(30)
    describe_status()

    return {
        'statusCode': 200,
        'body': json.dumps('hello from lambda')
    }
