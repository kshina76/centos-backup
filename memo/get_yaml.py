import urllib.parse
import boto3
from datetime import datetime
import random
import subprocess
import yaml

def lambda_handler(event, context):
    #bucket = event['Records'][0]['s3']['bucket']['name']    # バケット名を取得
    #key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')  # オブジェクトのキー情報を取得
    s3 = boto3.resource('s3')
    bucket = 'test-get-yml'
    key = 'config.yml'
 
    # ローカルのファイル保存先を設定
    # /tmp/はlambdaで一時ファイルとして保存できる領域
    file_path = '/tmp/' + key
 
    try:
        bucket = s3.Bucket(bucket)   # バケットにアクセス
        bucket.download_file(key, file_path)  # バケットからファイルをダウンロード
        # ファイルがダウンロードされているかlsコマンドで確認
        print(subprocess.run(["ls", "-l", "/tmp"], stdout=subprocess.PIPE))
    except Exception as e:
        print(e)
    
    f = open("/tmp/config.yml", "r+")
    data = yaml.load(f)
    print(data)

#############################################
# 手順
# pip install pyyaml -t . 
# ファイルを選択してzipに圧縮

# 参考文献
# https://recipe.kc-cloud.jp/archives/10035
# https://qiita.com/namkim/items/3edb9abe3871963bf0f7
# https://www.sejuku.net/blog/69240
#############################################
