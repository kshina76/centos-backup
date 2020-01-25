# 使用方法  

## 事前準備  
・test-codepipelineというリポジトリにbuildspec.ymlをpushしておく。  
・アカウントとリポジトリ名を変更したい場合は、tfファイルの該当箇所を変更する。  
・gitコマンドにgithubのアカウントやパスワードの情報を記憶させる  
・git remote origin <リポジトリ>  
・githubでwebhookを実現させるためにgithubの自分のアカウントからトークンを発行する  
・export GITHUB_TOKEN=<発行したトークン>　を.bash_profilに設定する。sourceコマンドを忘れずに。  

## コマンド  
```bash  
$ terraform init  
$ terraform apply  
$ git add ./Dockerfile  
$ git commit -m "add"  
$ git push -u origin master  
```

## 注意点  
・pushしてからデプロイされるまで時間がかかる  