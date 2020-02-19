
'''
SNS(message)->lambda->cloudwatchlogs->lambda
'''

#############################################################
# 1つ目のlambda
# cloudwatchlogsをlambdaのトリガーにして、フィルターで「ERROR」としたらERRORという文字が含まれているjson全体(一つのログ全体)を抜き出してくる。
# cloudwatchlogsは、トリガーとして二つ目のlambdaのcloudwatchlogs指定して、監視している。今回はフィルターで「ERROR」を監視しているから二つ目のlambdaから
# cloudwatchlogsにERRORが含まれたものが書き込まれたら、1つ目のlambdaをキックする。
#############################################################
import boto3
import botocore
import time
import base64
import zlib
import json
import logging
import datetime

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    #logger.info(json.dumps(event))
    data = zlib.decompress(base64.b64decode(event['awslogs']['data']), 16+zlib.MAX_WBITS)
    data_json = json.loads(data)
    log_json = json.loads(json.dumps(data_json["logEvents"][0], ensure_ascii=False))
    print(log_json)


'''
def lambda_handler(event, context): #参考にさせて頂いたメール送信プログラム本体
    data = zlib.decompress(base64.b64decode(event['awslogs']['data']), 16+zlib.MAX_WBITS)
    data_json = json.loads(data)
    log_json = json.loads(json.dumps(data_json["logEvents"][0], ensure_ascii=False))

    #If文にメッセージチェック処理を追加
    if data_json["logGroup"] and not (log_message_omit_check(log_json['message'])):
        date = datetime.datetime.fromtimestamp(int(str(log_json["timestamp"])[:10])) + datetime.timedelta(hours=9)
        sns_body = {}
        sns_body["default"] = "" 
        sns_body["default"] += "Owner : " +  data_json["owner"] + "\n" 
        sns_body["default"] += "LogGroup : " + data_json["logGroup"] + "\n" 
        sns_body["default"] += "LogStream : " + data_json["logStream"] + "\n" 
        sns_body["default"] += "SubscriptionFilters : " + ''.join(data_json["subscriptionFilters"]) + "\n" 
        sns_body["default"] += "Time : " +  date.strftime('%Y-%m-%d %H:%M:%S') + "\n" 
        sns_body["default"] += "Message : " + log_json['message'] + "\n" 

    return 'Successfully processed {} records.'.format(len(event['awslogs']))

def log_message_omit_check(log_message): #特定のメッセージは省く関数
    
    omit_message = []
    omit_message.append('TEST_ERROR') #省きたいメッセージをシングルクオートの間に書く
    omit_message.append('ERROR_TEST') #複数ある場合は2行目以降にアペンドしていく
    
    #省くメッセージが入っていないかチェック
    for message in omit_message:
        if message in log_message:
            return True
    
    return False
'''


#############################################################
# 2つ目のlambda
# SNSをlambdaのトリガーとして、メッセージを受けとってcloudwatchlogsに書き込む
#############################################################

import boto3
import botocore
import time
import base64
import zlib
import json
import logging

# for getting launch paths
import shlex
import subprocess
import os

def get_client(service):
    client = boto3.client(service)
    return client
    
# execute shell command
def get_cmd_stdout(cmd):
    tokens = shlex.split(cmd)
    tokens = subprocess.run(tokens, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return tokens.stdout.decode("utf8").replace('\n','')
'''
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
                                    ProvisionedProductName='tenantB_2',
                                    PathId=ll_path,
                                    NotificationArns=['arn:aws:sns:us-west-2:343310143635:test'],
                                    ProvisioningParameters=[
                                        {
                                            'Key': 'SSOUserEmail',
                                            'Value': 'kshina47+tenantB_2@gmail.com'
                                        },
                                        {
                                            'Key': 'AccountEmail',
                                            'Value': 'kshina47+tenantB_2@gmail.com'
                                        },
                                        {
                                            'Key': 'SSOUserFirstName',
                                            'Value': 'tenantB_2'
                                        },  
                                        {
                                            'Key': 'SSOUserLastName',
                                            'Value': 'tenantB_2'
                                        },
                                        {
                                            'Key': 'AccountName',
                                            'Value': 'tenantB_2'  
                                        },
                                        {
                                            'Key': 'ManagedOrganizationalUnit',
                                            'Value': 'Custom'
                                        }
                                    ])
    except botocore.exceptions.ClientError as e:
        print("In the except module. Error : {}".format(e))
'''
'''
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.critical("[CRITICAL] log message")
    logger.error("[ERROR] log message")
    logger.warning("[WARNING] log message")
    logger.info("[INFO] log message")
    logger.debug("[DEBUG] log message")
    return 'Success'
'''

def lambda_handler(event, context):
    #create_account()
    #data = zlib.decompress(base64.b64decode(event['awslogs']['data']), 16+zlib.MAX_WBITS)
    print(json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('hello from lambda')
    }


######################################################################
# 方針
# lambda(account f、トリガー:cloudwatchlogsとS3)、cloudwatchlogsはtrailを監視
# ->cloudwatchlogs(trail)にアカウント作成完了が書き込まれる
# ->もう一回lambdaが今度はcloudwatchlogsをトリガーとして呼び出される
# slackを適宜実行する

# memo
# 複数トリガー : https://teratail.com/questions/152305
# 上記コード参考1 : https://www.dcom-web.co.jp/lab/cloud/aws/notify_filtered_cloudwatchlogs_by_lambda
# 上記コード参考2 : http://htnosm.hatenablog.com/entry/2016/05/06/090000
# 上記コード参考3 : http://engmng.blog.fc2.com/blog-entry-49.html
# logからjson抜き出し : http://blog.serverworks.co.jp/tech/2020/01/08/cloudwatch-filter-writing/
######################################################################

 
