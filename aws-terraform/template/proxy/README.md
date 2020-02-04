# 使用方法  

1. awsまたはコマンドでキーペアを踏み台サーバ用と作業サーバ用の二種類を作る  
2. variable.tfのkey設定に公開鍵の指定をする  
3. terraform init,applyコマンドを実行  
4. 踏み台サーバに作業用サーバにつなぐための秘密鍵を.sshに置く  
5. chmod 600 ~/.ssh/{key_name}でセキュアにする  
6. 踏み台サーバにssh接続後、作業サーバにssh接続をする  
  
# 参考文献  
・EC2インスタンスとDB用インスタンスを立てたミニマム構築  
https://tech.recruit-mp.co.jp/infrastructure/post-10665/  
  
・variablesの使い方  
https://qiita.com/samskeyti/items/5855f1f2b5262e27af6e  
  
・terraformで踏み台サーバ構築  
https://qiita.com/bunty/items/5ceed66d334db0ff99e8  
  
・最新のCentos7のAMIを取得するコマンド  
https://dev.classmethod.jp/cloud/aws/get_latest_centos_ami_id/  