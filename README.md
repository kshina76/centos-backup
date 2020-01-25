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

```bash  
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2  
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo  
$ sudo yum install -y docker-ce docker-ce-cli containerd.io  
$ sudo systemctl start docker  
$ sudo systemctl enable docker  
$ docker --version  
  
Docker version 19.03.5, build 633a0ea  
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

## 3-5.pyenvのインストール(同時にpipenvも構築したほうがいいので、その時が来たらやる)  
```bash  
$ sudo yum install gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel  
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv  
$ echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile  
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile  
$ source ~/.bash_profile  
$ pyenv --version  
pyenv 1.2.2-6-g694b551  
```

・pythonのバージョンのリストを表示。ここから選んでインストールする  
```bash
$ pyenv install --list  
```

・pythonのバージョン切り替え(3.6.4を選択)  
```bash  
$ pyenv install 3.6.4  
$ pyenv global 3.6.4  
$ pyenv rehash  
$ python --version  
Python 3.6.4  
```

### 参考文献  
・pyenvのインストール  
https://qiita.com/ksugawara61/items/ba9a51ebfdaf8d1a1b48  

## 3-6.awscliのインストールと設定
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

## 3-7.eksとkubectlのインストール  
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

## 3-8.terraformのインストール  
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

