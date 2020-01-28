# 使用方法  

## 事前準備  
・test-codepipelineというリポジトリにbuildspec.ymlをpushしておく。  
・アカウントとリポジトリ名を変更したい場合は、tfファイルの該当箇所を変更する。  
・gitコマンドにgithubのアカウントやパスワードの情報を記憶させる  
・git remote origin <リポジトリ>  
・githubでwebhookを実現させるためにgithubの自分のアカウントからトークンを発行する  
・export GITHUB_TOKEN=<発行したトークン>　を.bash_profilに設定する。sourceコマンドを忘れずに。  

## ecsクラスタ構築コマンド  
```bash  
$ terraform init  
$ terraform apply  
```  

## ecsクラスタにデプロイする方法  
```bash  
# dev_dirは任意の名前なので好きな名前を付けていい。単純にアプリ開発するディレクトリを作っているだけ  
# 当たり前だけどgit initは最初だけだよ。  
$ mkdir dev_dir  
$ cd dev_dir  
$ git init  
$ git pull <開発用のリポジトリ。buildspec.ymlとかを入れているところ>  
$ git remote add origin <pullしてきたディレクトリ>  
$ git add . または git add ./<成果物>  
$ git commit -m "add"  
$ git push -u origin master  
```  


## 注意点  
・applyしてからecsクラスタを構築するのに時間がかかるので注意  
・pushしてからデプロイされるまで時間がかかる  