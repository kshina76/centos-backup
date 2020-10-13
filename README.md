# 1.前準備  
## 1-1.centos7のインスタンスを作る
1.AWSコンソールでcentosのイメージを検索  
2.認証鍵の作成と登録  

# 2.インストール後やる事  

## 2-1.suのパスワード変更とリポジトリのアップデートとエディタのインストール  
```bash
$ sudo yum -y update  
$ sudo yum upgrade  
$ sudo yum -y install emacs  
```  

# 3.各種インストール

## 3-1.wgetをインストール  
```bash  
$ sudo yum -y install wget  
```

## 3-2.gitをインストールと自分のリポジトリをclone  
インストール  
```bash  
$ sudo yum -y install gcc curl-devel expat-devel gettext-devel openssl-devel zlib-devel perl-ExtUtils-MakeMaker autoconf  
$ cd /usr/local/src/  
$ sudo wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.5.tar.gz  
$ sudo tar xzvf git-2.9.5.tar.gz  
$ sudo rm -rf git-2.9.5.tar.gz  
$ cd git-2.9.5/  
$ sudo make prefix=/usr/local all  
$ sudo make prefix=/usr/local install  
$ $ git --version  
  
git version 2.9.5  
```

自分のリポジトリをcloneする。必要なスクリプトなどはここにすべて置いてある。  
```bash  
$ git clone https://github.com/kshina76/centos7_backup  
```


### 参考文献  
・gitのインストール  
https://qiita.com/tomy0610/items/66e292f80aa1adc1161d  
・gitコマンドの使い方  
https://qiita.com/kohga/items/dccf135b0af395f69144  


## 3-3.dockerをインストールと起動と自動起動設定  
・インストール  
```bash  
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2  
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo  
$ sudo yum install -y docker-ce docker-ce-cli containerd.io  
$ sudo systemctl start docker  
$ sudo systemctl enable docker  
$ docker --version  
  
Docker version 19.03.5, build 633a0ea  
```
  
・sudo無し実行  
```bash  
# exitはしないと設定が反映されないので注意  
$ sudo groupadd docker  
$ sudo gpasswd -a $USER docker  
$ sudo service docker restart  
$ exit  
```  

### 参考文献  
・dockerのインストール  
https://qiita.com/ymasaoka/items/b6c3ffea060bcd237478  

## 3-4.docker-composeをインストール
```bash  
$ cd {自分のリポジトリ}  
$ sudo yum -y install epel-release  
$ sudo yum install --enablerepo=epel jq  
$ bash dockcomp_inst.sh  
```

## 3-5.pyenv+pipenvの環境構築(gitも必要だけど3-2の方法でインストールしているものとする)
- pyenv+pipenvはアプリ開発やインフラ開発はこちらの環境を選択するといいと思う

```bash  
# 必要なライブラリをインストール
$ sudo yum install -y gcc zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel libuuid-devel xz-devel libffi-devel  
  
# pyenvをクローン  
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv  
  
# pyenvの環境変数設定  
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile  
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile  
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile  
$ exec "$SHELL" -l  
$ pyenv --version  
  
# virtualenv のディレクトリ（.venv）をプロジェクト内に作るように設定  
$ echo 'export PIPENV_VENV_IN_PROJECT=1' >> ~/.bash_profile  
  
# python 3.7.4 をインストールしてデフォルトに設定  
$ pyenv install 3.7.4  
$ pyenv global 3.7.4  
  
# pipenv をインストール  
$ pip install --upgrade pip  
$ pip install pipenv    
```
  
### pipenvの使いかた  
```bash  
# 作業ディレクトリに移動  
$ cd hoge  
  
# python仮想環境構築  
$ pipenv install --python 3.6  
  
# 試しにxgboostをインストール  
$ pipenv install xgboost  
  
# 仮想環境をアクティベート  
$ pipenv shell  
  
# 仮想環境から抜ける  
$ exit  
```
### 参考文献  
・pipenvのインストール  
https://blog.cles.jp/item/11113  
  
・pipenvの使い方  
https://narito.ninja/blog/detail/58/  

## 3-6.pyenv+anacondaの環境構築(pyenvは3-5でインストールしているものとする)
- pyenv+anacondaは、機械学習やデータ分析を行う際はこちらの環境を選択するといいと思う
- pyenvとanacondaは相性が悪く、activateするときにもんだいが起きるので少し工夫が必要(後述)
- https://qiita.com/y__sama/items/f732bb7bec2bff355b69

```bash
# anacondaのバージョン一覧を確認する
$ pyenv install -l | grep anaconda

# 使いたいバージョンをインストールする
$ pyenv install anaconda3-5.1.0

# インストールしたバージョンに環境を切り替える
$ pyenv global anaconda3-5.1.0

# anacondaで仮想環境を作る
$ conda create -n test python=3.6.5

# pyenvでanacondaの環境名を取得する
$ pyenv versions

# anacondaの仮想環境をactivateする(通常の方法だとできない。上記の参考文献を参照する)
$ source $PYENV_ROOT/versions/anaconda3-2.5.0/bin/activate <環境名>

# anacondaの仮想環境をdeactivateする
$ source $PYENV_ROOT/versions/anaconda3-2.5.0/bin/deactivate <環境名>

#パッケージインストール
$ conda install [パッケージ] or pip install -r requirements.txt など

```


## 3-7.awscliのインストールと設定
### awscliの前準備    
コンソールでIAMと検索してユーザー、ユーザの追加を選択してURLに沿って設定していく  
ユーザ名はAdministrator  
グループ名はAdministrators  
としているがなんでもいい。  
※設定した後にCSVをダウンロードするとキーとかIAMの情報が載っているからダウンロードしておくこと。  
※「プログラムからのアクセス」というやつにはチェックを付けておくこと(awsCLIを利用するため)  
・以下のURLを参考にして
https://newtechnologylifestyle.net/amazon-aws-iam/  
https://qiita.com/kzykmyzw/items/ca0c3276dfebb401f7d8  
https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/getting-started_create-admin-group.html  

### インストール  
```bash  
$ pip install awscli --upgrade --user  
$ echo 'export PATH="$HOME/.local/bin/:$PATH"' >> ~/.bash_profile  
$ source ~/.bash_profile  
$ aws --version  
```

### 設定  
csvはawsコンソールでIAMで新たなユーザを作ると手に入るので、そこから参照する。  
ここで、cofigureすることでcredentialが登録できて、terraformで鍵の設定などをしなくて済んでいたのかもしれない。  
```bash  
$ aws configure  
AWS Access Key ID [None]: csvファイルから  
AWS Secret Access Key [None]: csvファイルから  
Default region name [None]: ap-northeast-1  
Default output format [None]: json  
```

## 3-8.eksとkubectlのインストール  
### eks  
```bash
$ curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp  
$ sudo mv /tmp/eksctl /usr/local/bin  
$ eksctl version  
```

### kubectl  
作業用ディレクトリでなくて、ホームディレクトリとかで作業することをお勧めする。  
```bash
$ curl -o kubectl https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/kubectl  
$ curl -o kubectl.sha256 https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/kubectl.sha256  
$ openssl sha1 -sha256 kubectl  
$ chmod +x ./kubectl  
$ mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH  
$ echo 'export PATH=$HOME/bin:$PATH' >> ~/.bash_profile  
$ kubectl version --short --client  
```

### 参考文献  
・eksのインストール  
https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/getting-started-eksctl.html#w159aac11b7b5b9b7b3  
・kubectlのインストール  
https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/install-kubectl.html#w159aac27b9b9b3  

## 3-9.terraformのインストール  
```bash
$ sudo yum -y install unzip  
$ wget https://releases.hashicorp.com/terraform/0.12.19/terraform_0.12.19_linux_amd64.zip  
$ unzip terraform_0.11.9_linux_amd64.zip  
$ sudo mv terraform /usr/bin  
$ terraform --version  
```

### 参考文献  
・terraformの最新版のURLを取得する  
https://www.terraform.io/downloads.html  
・terraformのインストール  
https://410gone.click/blog/2018/10/22/linux-terraform%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/  
  
## 3-10.jupyter notebookのインストールとリモートサーバで起動させてローカルで使用  
```bash  
# jupyterをインストール  
$ pipenv install jupyter  
  
# ipythonを起動してjupyterログイン時のパスワードを設定  
$ ipython  
In [1]: from notebook.auth import passwd  
  
In [2]: passwd()  
Enter password: [パスワードを入力]  
Verify password: [パスワードを再度入力]  
Out[2]: 'sha1: [ハッシュ化されたパスワード]'  
```
外部接続環境用の設定ファイルを作成  
```bash  
$ mkdir ~/.jupyter  
$ emacs ~/.jupyter/jupyter_notebook_config.py  
```
```python:jupyter_notebook_config.py  
c = get_config()  
  
# Notebook上でplotを表示できるようにする  
c.IPKernelApp.pylab = 'inline'  
# 全てのIPから接続を許可  
c.NotebookApp.ip = '*'  
# IPython notebookのログインパスワード  
c.NotebookApp.password = 'sha1:[ハッシュ化されたパスワード]'  
# 起動時にブラウザを起動させるかの設定  
c.NotebookApp.open_browser = False  
# ポート指定  
c.NotebookApp.port = [接続ポート]  
  
接続ポートが8888だとしたらセキュリティグループでtcpを8888で0.0.0.0/0でリッスンする設定を施す  
  
```
jupyter起動  
```bash  
$ jupyter notebook  
```
表示されたアドレスにブラウザから接続する  
  
### 参考文献  
・jupyterをリモートで起動してローカルで動かす  
https://qiita.com/syo_cream/items/05553b41277523a131fd  
https://qiita.com/hiroseabook/items/1da01ea439b01c1eb48c  
  
・jupyterの使いかた  
https://pythondatascience.plavox.info/python%E3%81%AE%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83/jupyter-notebook%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86  

# 入社までにやること
- バックエンドエンジニアに必要な技術ロードマップを確認しつつ学んでいく
    - httpとかの基本的な理解なども含んでいるから、基礎学習の部分から取り組んでみるといいかもしれない
    - https://qiita.com/fukuda316/items/c6f5e75708033d15db04
- SPAやRESTやWeb APIの理解と開発
    - https://qiita.com/kanataxa/items/522efb74421255f0e0a1
- docker
    - 環境構築だけではなくて、AWSと連携してデプロイする方法なども含めて
- AWS
    - djangoで作ったアプリや研究内容を組み合わせて、インフラなどから考えて構築してみるとか
    - インフラのパターンとかを学習するといいかもしれない
- github
    - gitコマンドでブランチ切って開発したり、そこらへんを手足のように使えるようになる
- javascript/typescript
    - djangoでやったことをここらへんの言語を使って実装してみるとか
- go言語
    - 最近のwebアプリ開発はgo言語が優れていたりするらしいから、時間があったら学んでみてもいいかも
- vscodeでのデバッグ方法
    - デバッグだけではなくて、フレームワークの動作を見るときなどに使いたい
- vscodeのお気に入りプラグイン
    - lintとか自動補間とかでお気に入りのプラグインを見つけてメモしておくといいかもしれない
- テスト方法の学習
    - unittestとかを用いたテスト方法を学んでおくといいかもしれない