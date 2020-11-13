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

# 入社までに読む書籍、サイト
- Webエンジニアが学ぶべき書籍をいっぱい紹介している
    - https://qiita.com/JunyaShibato/items/3aa5f7f3fc991de17f3f

- 面白そうな本
    - 論理学
        - 論理トレーニング101題
        - 論理学(野矢茂樹)
    - 統計学
        - 統計はこうしてウソをつく―だまされないための統計学入門

- エンジニアのためのドローイングツール
    - https://dev.classmethod.jp/articles/drawing_tools/

- git
    - GitHub実践入門 ~Pull Requestによる開発の変革

- vim
    1. vimをインストールしたら、「vimtutor」というコマンドを打ってチュートリアルをやってみる
    2. 「実践vim」という書籍でtipsを学ぶ。画面分割とかいきなりやると、「こいつできるんじゃね？」ってなる

- Linux
    1. Linux標準教科書(無料配布)
        - https://linuc.org/textbooks/linux/
    
    2. Linuxコマンドポケットリファレンス
        - 確か似たようなの持ってた
    
    3. Linuxサーバ構築標準教科書
        - https://linuc.org/textbooks/server/
    
    4. シェルスクリプトの何かしらの本
    
    5. Linuxシステム管理標準教科書
        - https://linuc.org/textbooks/admin/

- いいコードを書くためのノウハウ
    - リーダブルコード(書籍)
        - 持ってる
        - さらに深い内容が知りたかったら
            - https://www.amazon.co.jp/gp/product/4048676881/ref=as_li_tf_tl?ie=UTF8&camp=247&creative=1211&creativeASIN=4048676881&linkCode=as2&tag=hirokidaichi-22

- オブジェクト指向
    - オブジェクト指向でなぜ作るのか
        - kindleに入ってる

- データベース
    1. 達人に学ぶSQL徹底指南書

    2. 達人に学ぶDB設計徹底指南書
    
    3. 基礎からのMySQL
    
    4. SQLアンチパターン

- HTML/CSS

- go言語
    1. a tour of go(サイト)
        - goの文法を網羅

    2. effective go(サイト)
        - goの命名規則やgoらしい書き方など、一歩踏み込んだ内容
        - 英語
            - https://golang.org/doc/effective_go.html
        - 日本語
            - http://golang.jp/effective_go

    3. スターティングGo言語(書籍)
        - Goの基本的な文法やライブラリなど

    4. Goプログラミング実践入門(書籍)
        - 標準ライブラリを使わずにwebアプリを開発
        - プロトコルを作るわけではないので、通信方式などはライブラリに頼る
        - 読み終わったけど、goの勉強をした後にまた戻ってくる

    - 参考文献
        - https://qiita.com/yoskeoka/items/d07b60f755e8a9b30ccf

- JavaScript
    - React
        - フロントエンドのフレームワーク
        - これをやる前にjavascriptを使ったフロントエンドはどうするのがいいかを調べてから考える
    - Node.js
        - javascriptでバックエンドのプログラムを書くことができるもの

- TCP/IP 4階層モデル、ネットワーク周りの技術
    1. TCP/IPの要点
        - データがいろいろな層を経由して送信側から受信側に渡されていく流れが掴める
            - アプリケーション同士(例えばブラウザとwebアプリケーション)が通信する際には4つの層を経由していることがわかる
                - アプリケーションを作るエンジニアはHTTPとTCPの規約に沿っていれば問題ないが、さらに裏側を知るのは重要
            - 送信側からルータを経由しながら送信先に送られる手順
                - 実際に伝送ケーブルや無線を使ってデータが移動しているのは、横矢印の部分だけ。縦矢印は一つのコンピュータ内でソフトウェアが動いて、ヘッダを追加して、次のソフトウェアに渡してヘッダを追加しての繰り返し。
                - https://zenn.dev/naoki_mochizuki/articles/68748997ae1f4d6a5fd7

            ![2020-10-26 22 06のイメージ](https://user-images.githubusercontent.com/53253817/97182102-70a5ec00-17df-11eb-9473-b4a5fbac7d54.jpeg)

            - ソケット通信
                - HTTPが下位のレイヤーを使うときにソケット通信を使っている
                    - アプリケーション層からトランスポート層のプロトコルを利用する時に使う 
                        - トランスポート層からインターネット層はどのように通信しているのかな？
                - 例えばブラウザを使用したHTTP通信で、サーバのTCPポート80番に対してソケットを使ったプロセス間通信を行う

        - https://qiita.com/genre/items/05186691fbf8c10a4a48
        - http://www.al.cs.kobe-u.ac.jp/~ohta/old_public_html/lecture/info_comm_eng/2002/slide/networkprogramming.pdf
    
    2. ネットワークはなぜ繋がるのか
        - 「ブラウザにURLを入力〜webページが表示されるまで」をLANや光ファイバのレベルまで掘り下げて説明している
    
    3. マスタリングTCP/IP入門編(書籍)
        - 以下の「TCP/IP 階層」の説明を網羅している
            - ネットワークインタフェース層
                - Ethernet
            - ネットワーク層
                - IP,ARP,RARP,ICMP
            - トランスポート層
                - TCP,UDP
            - ルーティングプロトコル
                - RIP,OSPF,BGP
            - アプリケーション層
                - DNS,www,telnet,ftp,http
            - https://www.infraexpert.com/study/tcpip.html
    
    4. マスタリングTCP/IP シリーズ全巻
        - https://www.ohmsha.co.jp/tbc/text_series_0201.htm

    5. TCP/IP プロトコルスタック自作
        - ルーター自作でわかるパケットの流れ(書籍)
        - go言語を使ったプロトコルスタック
            - https://github.com/pandax381/lectcp
        - go言語でEthernetやARPを実装している
            - 標準ライブラリを使わないで、作成しているのだと思う
            - https://terassyi.net/posts/2020/03/29/ethernet.html
            - https://github.com/terassyi/proto

- web技術、web開発の基本を網羅
    1. Web技術の基本(書籍)
        - 持ってる
        - 読み物として
        - https://www.amazon.co.jp/exec/obidos/asin/4797388811/akiyoko0b-22/

    2. プロになるためのWeb技術入門(書籍)
        - 借りた
    
    3. Webを支える技術(書籍)
        - 借りる申請をした
        - もう少し踏み込んだ内容

    4. 体系的に学ぶ 安全なWebアプリケーションの作り方 第2版 脆弱性が生まれる原理と対策
        - 借りる申請をした
        - 攻撃手法などわかりやすく解説しながら、安全なものを作るための説明

- インフラ
    1. インフラエンジニアの教科書
        - インフラの基礎知識
    2. インフラエンジニアの教科書2
        - インフラの幅広い知識から障害対応まで
    3. 絵で見てわかるITインフラの仕組み
        - 冗長化とかキャッシュとか色々な知識
    4. 絵で見てわかるOS/ストレージ/ネットワーク
    5. インフラ設計のセオリー
        - 要求定義から設計、運用保守といった工程を順序立てて説明している
    6. 入門監視
        - システムをどのように監視するべきかを解説している
    7. Infratructure as code(オライリー)
        - 特定のツールに縛られないでIaCを説明している
    - 参考文献
        - https://dev.classmethod.jp/articles/11-technical-books-summary/

- AWS
    1. Amazon Web Services 基礎からのネットワーク&サーバー構築
    2. 実践terraform
        - 読んだけど、復習したほうがいい
    3. IAMの基本、設計
        - https://booth.pm/ja/items/1563844

- スクレイピング
    1. サーバサイドで動的生成しているサイトをスクレイピング(requests+BeautifulSoup)
        - https://www.youtube.com/watch?v=bXBa-88BiYA
    2. クライアントサイド(ブラウザ)で動的生成しているサイトをスクレイピング(requests-html)
        - 最近のwebアプリはクライアントサイドレンダリングやSPAが多い
        - https://gammasoft.jp/blog/how-to-download-web-page-created-javascript/
    3. それでもスクレイピングできなかったら以下を参照(SPAとかのスクレイピング)
        - https://qiita.com/Azunyan1111/items/b161b998790b1db2ff7a
        - https://qiita.com/devneko/items/9ac978965717d5513aa5

- OS
    - ロードマップに書いてあるlinuxコマンド
    - Linuxの仕組み〜実験と図解で学ぶ〜
        - Linuxの美味しいところを解説している
    - はじめてのOSコードリーディング
        - 小さいUnixのOSを用いて解説している
    - コンピュータシステムの理論と実装
    - 30日でできる! OS自作入門
        - アセンブリを書くから、その知識がないときついかも
    - Goで覗くシステムプログラミングの世界
        - OSの機能をgoで覗いている
        - https://ascii.jp/elem/000/001/234/1234843/

- コンピュータアーキテクチャ
    - 最新図解でわかるPCアーキテクチャのすべて
        - 借りてる
        - 初心者でも読み進められる

    - コンピュータアーキテクチャ (電子情報通信レクチャーシリーズ)
        - 薄いけど内容は濃い本
        - わかりやすかった覚えがある

    - コンピュータアーキテクチャ技術入門 ~高速化の追求×消費電力の壁

    - Raspberry Piで学ぶコンピュータアーキテクチャ

    - コンピュータの構成と設計
        - 結構難しいけど名著
        - 上下巻見たけど忘れてるかも

- 文字コード
    - プログラマのための文字コード技術入門
        - Unicodeとは何かなど

- セキュリティ
    - 図解まるわかり セキュリティの仕組み
        - 借りてる
        - セキュリティの基礎知識、攻撃、対策手法について幅広く解説
    - プロフェッショナルSSL/TLS
        - 全部読むのはオーバーかもなので、ハンドシェイクや暗号化httpsの基礎くらいは知っておくのはいいかも

- エンジニアの三代嗜み
    - 自作OS
    - 自作コンパイラ、インタプリタ(自作言語)
    - 自作プロトコルスタック

- SQL構文、DB設計
    - https://qiita.com/maaaaaaaa/items/4e1d84cb40c83004575f


- django
    1. djangogirls
        - ミニブログを作るチュートリアル
        - 終わった
    2. 公式チュートリアル
        - 投票アプリを作るチュートリアル
        - 終わった
    3. 現場で使えるdjangoの教科書 基礎編
        - 読んでる途中
    4. 現場で使えるdjangoの教科書 応用編
        - 持っていない

    - djangoの学習ロードマップ
        - https://akiyoko.hatenablog.jp/entry/2018/12/01/133427

- docker
    - 読んでいる途中

- html css
    - 基本的な本は読んだ

- テスト
    - CircleCI


- webアプリを開発するときにやること(クラス図、DB設計とか)
    - https://note.com/promitsu/n/n463792216407
    - https://qiita.com/Saku731/items/741fcf0f40dd989ee4f8

- デザインパターン
    - https://techacademy.jp/magazine/9195

- 参考文献
    - 低レイヤーの書籍まとめ
        - https://qiita.com/hareku/items/3383be7aee616e04b80f

    - https://qiita.com/hirokidaichi/items/d30714f0698dcff1200f

# 優先してやるべきこと
- IntelliJとかvscodeのデバッガ機能の使い方
    - デバッガでプログラムの裏側の動きを追えるように訓練する

- Gitの使い方
    - これがないと生きていけない

- オブジェクト指向

- go言語のREADMEを完成させる

- 自動コールグラフ作成
    - 関数の呼び出し関係をグラフィカルに表示してくれるツール
    - go言語ならgo-callvisというライブラリがある
        - https://qiita.com/mnuma/items/fa25886c39fe991ecdfd
    - PythonならPyCallGraphというものがある
        - 実行時間がかかりすぎた関数を赤く表示するなど、チューニングに使えそうな機能もある
        - https://kazuhira-r.hatenablog.com/entry/2019/04/13/191053

- 自動でクラス図、パッケージ図を作成する
    - グラフィカルに表示してくれるツール
    - pythonならPyreverseというライブラリがある
        - https://qiita.com/kenichi-hamaguchi/items/c0b947ed15725bfdfb5a

- 要求定義から設計、コーディングという手順で開発を進めてみる
    - https://tkmt-hrkz.hatenablog.com/entry/2020/09/15/【開発プロセス】個人開発の流れ

- 今学んできたWeb開発の知識を使ってプログラミングをする
    1. ブログにユーザ認証をつけて、有料記事機能を作成する
        - セッションやクッキーや認証方式など色々な知識を使うから勉強になると思う
        - GoggleAPIを積極的に使ってみる(検索とか)
        - セキュリティの意識とかもする
    2. text to speechのapiを使って実況用ボイスの提供サイト作成
        - goggleのttsのapi
            - https://blog.apar.jp/web/9893/#toc10
        - サイトのレイアウトの例
            - https://www.yukumo.net/#/

- javascript/typescriptをやる
    - まずはjqueryとか低レイヤーのところからやるといいかもしれない

- dockerとdocker-composeで色々なパターンの開発環境を作っておく
    - 開発環境の構築で使うことになると思うから、「検証->dockerfile作成->検証->...」のようなサイクルも染み込ませた方がいい。
    - kubernetesとかはモダンすぎるのかな？

- webアプリで重要事項についてのコードを蓄積しておく
    - セキュリティ
    - 認証

- go言語でweb開発のいろいろな手法を蓄積する
    - https://qiita.com/wsuzume/items/75d5c0cd2dd5a1963b9e
    - https://blog.k-bushi.com/post/tech/programming/golang/build-web-application-with-golang-14/
    - https://astaxie.gitbooks.io/build-web-application-with-golang/content/ja/09.3.html

- 研究テーマを考える
    1. go言語の非同期処理を行うことで、現在のバックエンドの処理を高速化する
    2. AWSの何かしらを改良してレスポンスを速くする
        - 例えば、Elastichacheとかを使って静的コンテンツの配信を爆速にするとか

---

# 絶対に読んだ方がいい記事、書籍
- エンジニアの情報収集先
    - https://qiita.com/nesheep5/items/e7196ba496e59bb2aa28
- 基本的なシステム構成図を理解するためのAWS基礎をまとめてみた
    - https://qiita.com/goldayushi/items/0e0f34d19813b8fdc2b8
- ドメイン駆動開発をわかりやすく解説している
    - 簡単なCRUDサービスならMVCでもいいけど、大規模なサービスになって複雑になってしまった場合はドメイン駆動が必要になってくる
    - https://qiita.com/tmknom/items/08b69594e32a92bccee5
    - https://qiita.com/little_hand_s/items/ebb4284afeea0e8cc752
    - https://tech.willgate.co.jp/entry/2020/02/11/183000
- 技術選定や設計前に確認しておくこと、決めておくことなど
    - 筆者が設計する際の順番に並んでいる
    - https://qiita.com/tmknom/items/08b69594e32a92bccee5
- webエンジニア1年目に読んだ方がいい本、記事(副業など多岐に渡って書かれている)
    - https://qiita.com/virtual_techX/items/35034d28cdb9255367ba
- WebAPI設計
    - https://qiita.com/mserizawa/items/b833e407d89abd21ee72
    - https://www.virtual-surfer.com/entry/1
- オブジェクト指向
    - オブジェクト指向でなぜ作るのか(書籍)
    - 増補改訂版Java言語で学ぶデザインパターン入門(書籍)
- RedisとElastiChache
    - https://qiita.com/gold-kou/items/966d9a0332f4e110c4f8
---

# 取る資格
- 基本情報技術者試験
    - テクノロジ(自分の技術力をあげるついでに勉強する)
        - ソフトウェア、ハードウェア
            - パタヘネとかのコンピュータアーキテクチャ系
        - データベース
            - 達人に学ぶ系をやる
        - ネットワーク
            - マスタリングTCP/IP
        - ソフトウェア設計
            - 
        - 情報セキュリティ
            - 図解まるわかり

        - データ構造とアルゴリズム

        - ソフトウェア開発
            - pythonとかCとかから選択して回答

    - マネジメント(基本情報の問題集みたいなのをやればいいかな)
        - プロジェクトマネジメント
        - サービスマネジメント
        - システム戦略
        - 経営戦略、企業と法務
    
    - 過去問
        - https://www.fe-siken.com/fekakomon.php

- 応用情報技術者試験
    - 基本情報のテクノロジの勉強でかなりの量をやっているので、そこにプラスして過去問や問題集みたいなのをやれば行けそう
    - 勉強法は以下のようにやると良さそう
        - https://qiita.com/drken/items/42e54d5c43d4d7815ed4
    - 過去問
        - https://www.ap-siken.com/apkakomon.php

- ネットワークスペシャリスト

- データベーススペシャリスト

- システムアーキテクト


# わかったこと
- クラウドサービス開発ってどのようなところの開発をするのか？
    - ロボットやiosアプリやandroidアプリの頭脳に当たる部分
        - ロボットやスマホアプリにデータの保存やデータの解析のバックエンドの処理を入れてしまうと、ロボット自体のコストや大規模な演算を行うことができなくなってしまう。なので、ロボットやスマホアプリはデータを収集することに重きを置いて、実際の演算はクラウドサービス側(社内に置かれているサーバ)で行う。なので社内のサーバで行う処理の開発を行うのだと思う。

- 常にアンテナを張っていたほうがいい
    - 例えば、いろいろな会社の動向を見て、新しいAPIが出たら叩いてみて、自分のプロダクトに反映できないかとか
        - AWSのサービスをとにかく触ってみる
        - yahooとかの新しいAPIを触ってみる
        - 企業の技術ブログを日頃から見てみる
        - 企業の技術のtwitterとかをフォローしておくとか
        - Udemy
            - 難しい応用的な物も乗っているから
        - 技術のメルマガとか
        - mlflowとかの技術を自分から触って組み込んだりしているか

- 現状で面倒なことを自動化して楽をしてみる

- プログラミングの勉強の手順
    1. プログラミング言語のチュートリアル
        - プログラミング言語の文法や慣例的な書き方を覚えるため
    2. フレームワークを使わないで簡単なブログを作成
        - webがどのように動いているのかやセキュリティの対策などを学べるため
        - 追加でwebやネットワークの基礎みたいな書籍で知識を補完しながら学べるといいと思う
    3. フレームワークのチュートリアル
        - フレームワークの使い方を学ぶため
        - ここでフレームワークを使うとどんなに便利かを思い知る
    4. フレームワークを使って簡単なブログを作成
        - CRUD機能だけ
    5. ブログにいろいろな機能を追加してみる
        - ランキング
    6. デザインをやってみる
        - CSSとか
    7. keep studying

    - フロントでもバックエンドでもどんな技術でも共通していることが、Expressを使う前にNode.jsを使って実装してみるとか、Node.jsを使う前に生のjavascriptで書いてみるとか。基礎的なところが重要になってくると思う

- ライブラリにもチュートリアルがあるから勉強する時は見たほうがいい

- APIをフル活用する上で重要なこと3選
    1. 自分で実装していて、この部分APIがありそうじゃないかと気づくこと
    2. APIを探すスキル
    3. APIを作るスキル

- エンジニアで必須のググりかた
    1. エラー文でググる
    2. 自分がわからないことをそのままググってみる
        - 例えば、「CSSが読み込まれないな」となっていたら、「CSS 読み込まれない」で検索する
    3. リファレンス名でググる
        - jsのforeahがわからなかったら、リファレンス名がmdnだから「foreach mdn」とググる
    4. リファレンスを読む
        - 公式リファレンスのサイトに行って「docs」というところになんでも書いてある
        - 公式リファレンスがないならgithubのREADME
    5. 英語でググる
    6. githubでググる
        - in this repository でググるとリポジトリ内で検索できる
        - issueでも調べる
        - discussionsでも調べる
            - Q&A機能としても使える

- 便利な翻訳MACアプリ
    - DeepL
    - https://www.youtube.com/watch?v=MhXVh1pn1KE

---
# 社会人メモ
## 頭の悪い話方
- 声が小さい
    - 自信がないような印象を抱かれる
    - 最後の確認で声が小さくなってしまうのが一番まずい
        - 大事な事柄に対する返答が小さい声だとまずい
        - ピークエンドの法則
    - 常に声を大きくするのが苦手な人は最後の文章だけを大きくする

- 曖昧な言葉を使う
    - アサインするとかアグリーするといった言葉
        - アサインは、業界によって違う意味になってしまうから
            - 本来は役職に任命するという意味
            - IT業界だと人材を確保するという意味
            - コンサルだと自分がプロジェクトに参加するという意味
    - 大事なのは簡単でわかりやすい言葉を使って高度な会話をする

- 必要な数字がない
    - 「多めに発注しておいて」のように数を指定してない

- 質問に答えていない
    - 質問には最初の一言で返すようにして、後から原因を話す、次からはこのような改善をしていきます と答える
    - 質問に対して言い訳から始まる人が多すぎる

- マシンガントーク

<br></br>

## 質問の仕方、バグレポートの仕方

- 画面全体のスクショを撮って送る
    - 画面全体のスクショを送れば、どのような動作をしてバグが起きて、その時のエラー文は何かということがわかるから
    - エラー文やログだけ送られてもわからないから必ず全体を送る

- 起きていることを詳細に正確に質問する
    - 事実と推測を分ける
        - 100%あっていることは事実で、1%でも間違っている可能性があるなら推測
        - 例えば、githubにpushするときに「プロキシ認証をとしたのですが、pushできないです」という場合は本当にプロキシを通せているのかが曖昧なら推測であることを告げる。「プロキシ認証ができているのかわからないですが、pushができない」のように

- 指示代名詞は使わない
    - 「あれ、これ、それ」を使われても相手には伝わらない

- 一つの段落に一つの質問にする
    - 話の冒頭で「解決したい問題が2つある」と述べておく
    - テキストベースの質問なら、1,2のように番号を振って質問をする

- 質問のフォーマットを作るのがいいかも
    - 「目的、状況(現状、事実)、添付、仮説(原因)」をフォーマット化しておいて埋めるだけで質問できるのが楽かもしれない

- メモ
    - ググり力は知識量に比例する

<br></br>

## 公式ドキュメントの読み方

- そもそも読むクセをつける
    - 毛嫌いして読まないのが問題
    - 初心者向けの記事と公式ドキュメントを一緒に読むことで、理解が一層深まる

- 語彙力をつける
    - プログラミングに置いて知識は必要。ソースコードは覚える必要はない
    - ドキュメントや本を読み込んで語彙力をつける

- 英語に慣れる
    - google翻訳はどんどん使っていい
    - ネイティブになる必要はない

- エラー文をちゃんと読む
    - エラー文を読んで理解する
    - 仮説を立てて実行する
    - 仮説を実行して解決できなかったら、最終的にググる

- ドキュメントを調べるとき
    1. 実現したい処理がわからない時
    2. 使いたいクラスや関数が決まっているが使い方がわからない時

- 一番大事なのはAPIリファレンス
    - 「メソッド、引数、返り値」が一番大事
        - 解説を見なくても、メソッド名と引数と返り値を見るだけでわかるレベルにならないといけない

<br></br>

## 新しい技術に触るときの勉強の進め方
1. 前提としてオブジェクト指向の知識はあるものとする
    - 概念の知識がないと、ただ文法を覚えるだけになってしまうため
2. 選定したプログラミング言語の公式チュートリアルをやってみる
3. 選定したプログラミング言語の応用的なチュートリアルをやってみる
    - 例えば、web開発を行うための主要なライブラリなどを学べるチュートリアルとか
4. 何かを自分で作ってみる
    - RSSリーダーを作ると、webアプリケーションに必要な要素が網羅されているらしい
    - ブログを簡単に実装してみる
    - 言語の文法に慣れるためだけなら、データ構造とアルゴリズムを実装するのもいいかも
5. 選定した技術のベストプラクティスを学ぶ

<br></br>

---

# 直近のto doリスト

- webアプリ開発のフローを使って設計しながら開発してみる
    - https://note.com/promitsu/n/n463792216407

- 一つ目の題材で開発をしてみる
    - Go言語でtechblogを完成させる
    - アプリケーションアーキテクチャ
        - レイヤー構成
            - 3層(小規模なので、データアクセス層はいらないので実質2層)
        - プレゼンテーション層
            - MVC
            - コントローラー
                - マルチプレクサとURLディスパッチャが二つでコントローラとして機能する
                - main.goがURLディスパッチャ
            - モデル
                - データベース自体の定義
                - データベースへの処理はここが担当する
                - CRUDとかビューにデータを返したり
                - ハンドラ関数はここに定義しない
                - dataディレクトリにまとめる
            - ビュー
                - ハンドラ関数が定義されたgoファイルが複数
                - データとテンプレートを混ぜて表示する処理を担当
                - リダイレクトなども行う
                - 必要に応じてモデルにアクセスする
                    - データの取得
                    - 受け取ったデータをモデルに渡してCRUD操作をしてもらう
        - ビジネスロジック層
            - ドメインモデル
                - モデルにCRUDなどの振る舞いを実装するという意味でこの言葉を使っている


- 二つ目の題材で開発をしてみる(API設計の本を読んでから)
    - 「vanilla-js + Node.js + Go言語(API)」でSPA
        - vanilla-jsではjqueryを使わずにDOM操作
            - https://wemo.tech/2101#index_id65
            - https://qiita.com/shshimamo/items/ba3a57a81d9780030969
        - Node.jsはHTML,CSS,JSを配信（レンダリングはブラウザで行う）
        - Go言語はAPIとしての役割
        - 例(以下にAPIを搭載して拡張するのでもいいかも)
            - https://vanillawebprojects.com
            - https://github.com/bradtraversy/vanillawebprojects
        - なぜやるか？
            - vanilla-jsで開発することでフロントエンドの基礎がわかる
            - APIの設計を学ぶ
            - SPAを学ぶ
            - JSとGoでオブジェクト指向を学ぶ
    - techblog
    - 以下のサービスを拡張(または参考にして新しいオリジナルのwebアプリを作成する)
        - 例(以下にAPIを搭載して拡張するのでもいいかも)
        - https://vanillawebprojects.com
        - https://github.com/bradtraversy/vanillawebprojects

- 三つ目の題材で開発をしてみる
    - Qiitaみたいに自分のブログサイトを持てる仕組み

<br></br>

- 以下の書籍やサイトで学んだことを使ってリファクタリングをしていく
    - オブジェクト指向
        - https://qiita.com/hirokidaichi/items/d30714f0698dcff1200f
        - https://qiita.com/hirokidaichi/items/591ad96ab12938878fe1
        - https://qiita.com/hirokidaichi/items/0de5ca336de862cc91bd
        - https://qiita.com/hirokidaichi/items/d6c473d8011bd9330e63
        - アジャイルソフトウェア開発の奥義 第2版 オブジェクト指向開発の神髄と匠の技
            - https://www.amazon.co.jp/gp/product/4797347783/ref=as_li_tf_tl?ie=UTF8&camp=247&creative=1211&creativeASIN=4797347783&linkCode=as2&tag=hirokidaichi-22

    - クラス設計
        - オブジェクト指向設計実践ガイド
            - https://www.amazon.co.jp/dp/B01L8SEVYI/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1

    - デザインパターン
        - 増補改訂版 Java言語で学ぶデザインパターン入門
            - https://www.amazon.co.jp/増補改訂版-Java言語で学ぶデザインパターン入門-結城-浩-ebook/dp/B00I8ATHGW/ref=sr_1_1?__mk_ja_JP=カタカナ&keywords=GoF本&qid=1563517192&s=digital-text&sr=1-1
        - GoF以外のデザインパターン
            - https://www.hyuki.com/dp/dpinfo.html#AbstractClass

    - ドメイン駆動設計
        - DDDに関してめちゃくちゃわかりやすそうな本と記事
            - https://qiita.com/little_hand_s/items/2040fba15d90b93fc124
            - https://little-hands.booth.pm/items/1835632
        - ドメイン駆動設計入門 ボトムアップでわかる！ドメイン駆動設計の基本
            - https://www.amazon.co.jp/ドメイン駆動設計入門-ボトムアップでわかる！ドメイン駆動設計の基本-成瀬-允宣-ebook/dp/B082WXZVPC
        - MVCモデルのモデル肥大化への対処(MVCのレイヤ化)
            - https://qiita.com/tentom/items/653d46ded6e292630a6c
        - 実際にドメイン駆動設計で開発をしている
            - https://qiita.com/tono-maron/items/345c433b86f74d314c8d
            - https://qiita.com/APPLE4869/items/d210ddc2cb1bfeea9338
        - 別途READMEを見る

    - UML（設計）
        - 簡単UML入門
            - https://www.amazon.co.jp/dp/B073NX8K1L/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1
        - UMLモデリング入門
            - https://www.amazon.co.jp/UMLモデリング入門-児玉-公信-ebook/dp/B00EH93MR8/ref=bmx_1/356-7197418-1133737?_encoding=UTF8&pd_rd_i=B00EH93MR8&pd_rd_r=8e8b68f5-a2bc-4690-9cea-3a144a1e9756&pd_rd_w=KbLBh&pd_rd_wg=KgoTp&pf_rd_p=6ad035f2-0f1c-4b9e-a763-5321d5c2cd6e&pf_rd_r=8C9CY6J1110CRR67YSPT&psc=1&refRID=8C9CY6J1110CRR67YSPT
        - UMLモデリングレッスン
            - https://www.amazon.co.jp/UMLモデリングレッスン-平澤-章-ebook/dp/B00EH93MNW/ref=bmx_2/356-7197418-1133737?_encoding=UTF8&pd_rd_i=B00EH93MNW&pd_rd_r=5f26ae74-61a9-48ba-bf38-2620d54770c2&pd_rd_w=QJCiG&pd_rd_wg=vr3Qg&pf_rd_p=6ad035f2-0f1c-4b9e-a763-5321d5c2cd6e&pf_rd_r=9DTRJS4CPSB7DXBQSC5J&psc=1&refRID=9DTRJS4CPSB7DXBQSC5J


- 参考文献
    - https://qiita.com/hikey/items/b049b9057fb765e40788
    - https://qiita.com/hirokidaichi/items/d30714f0698dcff1200f
