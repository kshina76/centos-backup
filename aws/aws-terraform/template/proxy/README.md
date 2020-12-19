# 使用方法  

1. awsまたはコマンドでキーペアを踏み台サーバ用と作業サーバ用の二種類を作る  
2. variable.tfのkey設定に公開鍵の指定をする  
3. terraform init,applyコマンドを実行  
4. 踏み台サーバに作業用サーバにつなぐための秘密鍵を.sshに置く  
5. chmod 600 ~/.ssh/{key_name}でセキュアにする  
6. 踏み台サーバにssh接続後、作業サーバにssh接続をする  
  
# EC2やサーバに関してわかったこと  
## .sshディレクトリにあるauthorized_keyは何が記述されているのか  
自分自身の公開鍵が記述されている。つまり「ローカルサーバ -> リモートサーバ」のようにssh接続をするときのリモートサーバの公開鍵を登録している。  
これによってローカルサーバからリモートサーバに接続するための秘密鍵と、リモートサーバに設置されている公開鍵が合致して接続できる。  
ちなみに、known_hostsに記述されている内容は気にしなくていい。  
  
## ダイナミックポートフォワード  
### ダイナミックポートフォワードのユースケース  
例えば、大学からしか見れないサイトにアクセスしたい場合を考える(ieeeの論文索引とか)  
普通は大学内のLAN内に接続しないとダメ。  
しかし抜け道として、ローカルサーバ(自宅PC)からリモートサーバ(研究室PC)にダイナミックポートフォワードをするとまるで大学内のLAN内にいるように見立てることができる。  
LAN内にいると見立てられるので、LAN内に所属するのプライベートIPをブラウザに入力することでnginxの初期画面を表示することができる。  
  
### やり方  
0. 前提条件  
ローカルサーバ(自PC)から踏み台サーバ(EC2)にssh接続できること  
今回は踏み台サーバ兼nginxのリモートサーバとしている  
また、nginxが起動しているサーバ(リモートサーバ)の80番ポートを開けておくこと。  
  
1. gitbashを使って踏み台サーバにダイナミックポートフォワードをする  
```bash  
# 源ポートは自PCのどのポートをsocksプロキシとして使うかを設定する。1080推奨  
$ ssh -i {秘密鍵} -v -D {源ポート} centos@xxx.xxx.xxx.xxx 
```
  
2. リモートサーバでサービスを起動(flaskでもnginxでもなんでもいい。)  
dockerで起動する場合はリモートサーバとdocker間のポートフォワードを忘れずに。  
今回はnginxをdockerで起動して、80->80とポートフォワードすることにする。  
  
3. firefoxの設定でsocksプロキシとして動作するように設定  
socksホスト: localhost  
ポート: 1080(1で設定したポートを設定)  
SOCKSv5を選択  
  
4. firefoxのブラウザでリモートサーバに接続  
{nginxを起動しているリモートサーバのプライベートIP:1080}で接続してnginxの初期画面が出てくれば成功。  
リモートサーバとして複数のサーバが起動していても、踏み台サーバと同一LAN内のサーバなら、自PCからブラウザで該当サーバのプライベートIPを入力すれば接続できる    
  
# 参考文献  
・EC2インスタンスとDB用インスタンスを立てたミニマム構築  
https://tech.recruit-mp.co.jp/infrastructure/post-10665/  
  
・variablesの使い方  
https://qiita.com/samskeyti/items/5855f1f2b5262e27af6e  
  
・terraformで踏み台サーバ構築  
https://qiita.com/bunty/items/5ceed66d334db0ff99e8  
  
・最新のCentos7のAMIを取得するコマンド  
https://dev.classmethod.jp/cloud/aws/get_latest_centos_ami_id/  