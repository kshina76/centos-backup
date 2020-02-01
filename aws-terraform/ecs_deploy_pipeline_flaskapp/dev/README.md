# 構成
```
.
├── Makefile
├── README.md
├── app
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   └── default.py
│   │   ├── run.py
│   │   ├── server
│   │   │   ├── __init__.py
│   │   │   └── hoge
│   │   │       ├── __init__.py
│   │   │       └── hoge_api.py
│   │   └── tests
│   │       ├── __init__.py
│   │       └── test_hoge.py
│   └── uwsgi.ini
├── docker-compose.yml
└── nginx
    ├── Dockerfile
    └── nginx.conf
```

# memoとトラブルシューティング  
・terraformでリポジトリを作成して管理しているので、新たにリポジトリを作るときはterraformのecr.tfに追加する  
  
・buildspec内のAWS_DEFAULT_REGIONはビルトイン変数なので、実際に使うときはap-northeast-1は指定しない。  
しかし、pythonでスクリプトを書くときは、多分環境変数の展開に一工夫必要なので、今回は指定している  
  
・pythonでスクリプトを書くときは改行コードがコマンドに交じる事があるからreplaceで削除する  
  
・ファイルをまたいで変数を共有したいときに、グローバル変数が書かれているpyファイルをimportするとそのpyファイルを実行する事になる。  
つまり、dockerコマンドがpyファイルに書かれていたら実行されてしまうので、__main__を使うとその部分だけ実行されなくなる。  
  
・codebuildで使うディレクトリはすべてgithubのルートディレクトリのなので、  
カレントディレクトリの「.」はすべてgithubのルートディレクトリをあr和すことに注意。決してローカルマシンのカレントディレクトリではないので注意  
  
・デバッグはcloudwatchlogに標準出力されるので、そこで行う。  