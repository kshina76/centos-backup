# 構成  

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
・ecsの最小単位がタスク(k8sでいうポッド)のことから、それぞれのコンテナのIPは共有なので注意。つまりnginxにlocalhostの設定を施す  
・aws_ecs_serviceの中のlbの設定で今回作るサーバのエンドポイントとなるコンテナ名を指定する。  
・タスク定義のdependsOnのconditionはSTARTにする。もっと厳密に行うならHEALTHYで行う。以下参照  
https://christina04.hatenablog.com/entry/ecs-fargate-dependson-parameter  

  

# codepipeline  
・各ステージはS3にデータzipにして、を出し入れして共有する  
・sourceステージではgithubのソースコードをzipにしてS3に保存  
・buildステージではsourceステージの成果物(ソースコードのzip)を入力として、出力を今回はイメージの定義ファイルとしている  
・deployステージではbuildステージの成果物を入力として、デプロイを実行する  
  
## codepipelineの流れ  
1. GitHubへのpush  
・開発者がコードをプッシュする。flaskのpythoファイルでもDockerfileでもなんでもトリガーになる  
  
2. pipeline起動  
・開発者がコードをプッシュした事がトリガーになり、pipelineが起動する  
  
3. pipelineのsourceステージ  
・ここではCI/CDのインプットとなるディレクトリにあるファイル(GitHubのプロジェクトルートディレクトリにあるコードとか)をS3に取り込むステージ  
・S3に取り込むことで後のデプロイステージで使えるようになる。  
・コードが置いてあるプロバイダを指定することで、そのプロバイダに変化が生じたらルートディレクトリからすべてコードを引っ張ってくる。  
・今回はGitHubをプロバイダに指定しているので、pushされたらルートディレクトリにあるすべてのファイルをzipにしてS3に取り込むようになっている。  
  
4. pipelineのbuildステージ  
・buildspec.ymlに定義された内容を実行する。buildspecにビルドした後にテスト実行を書くことで自動テストも実現できる  
・今回はここでECRにコンテナイメージをプッシュする動作も行う。これもbuildspecにすべて記述する  
・sourceステージによってgithubのルートディレクトリがbuildステージでのカレントディレクトリになっている  
・最終的に成果物としてimagedefinition.jsonを生成する  
  
5. pipelineのdeployステージ  
・imagedefinition.jsonに記述されたコンテナイメージを起動する  
・今回はimagedefinition.jsonはbuildステージの成果物として作られている  
・imagedefinition.jsonはtaskdefinition.jsonのイメージを新しいものに置き換えるための動作に必要となる  
  
~ここにpipelineのわかりやすい画像を載せたい~  

## 注意点やわかったこと  
・imagedefinition.jsonにはnameとimageUriしか書かない。portmappingとかは定義できなくて、タスク定義の方でportmappingとかを行う。  
・つまりimagedefinitionとタスク定義は違うモノなので注意  
・imagedefinition.jsonに記述した内容はpipelineが自動的にタスク定義のコンテナを置き換えてくれる。  
・今回はcodedeployを使用していないが、これにcodedeployを組み合わせるとブルーグリーンデプロイが実現できるのでやる  
・task definitionはecsのタスク(コンテナ)を定義するためのモノで、docker-compose.ymlにawsのインフラ構成を加えたような設定ファイル  
・開発者はflaskなどのアプリケーションコードとDockerfileやbuildspec.ymlをgithubにpushすることでCI/CDを実現している  

## 参考文献  
・CI/CDのパイプラインやimagedefinitionの定義の仕方やシャルスクリプトにまとめる方法などあるので、絶対に見たほうがいい  
https://www.m3tech.blog/entry/elixir-fargate-impl-2  

・CI/CDがどのような流れで動くかがわかりやすい  
https://blog.spacemarket.com/code/ci-cd-codepipeline/  
  
・ECSの用語とか概念がわかりやすい  
https://qiita.com/NewGyu/items/9597ed2eda763bd504d7  
  
・タスク定義のテンプレート(Amazon公式)  
https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/create-task-definition.html  
https://aws.amazon.com/jp/blogs/news/use-aws-codedeploy-to-implement-blue-green-deployments-for-aws-fargate-and-amazon-ecs/  
https://www.terraform.io/docs/providers/aws/r/ecs_task_definition.html  
  
# ECS  
## タスク定義  
・起動タイプをFARGATEにする場合はネットワークモードをawsvpcを選択する必要がある  
・ネットワークモードでawsvpcを設定した場合はポートマッピングでhostPortとcontainerPortを同じにする必要がある  
・terraformでタスク定義を管理する場合、familyやvolumeやroleはterraformで定義して、コンテナの中身とかをjsonで記述する方式になる  
また、containerDefinitionsも書かないので注意。エラーになる。一番外のかっこも[]なので注意。  
https://www.terraform.io/docs/providers/aws/r/ecs_task_definition.html  
  
## ネットワークモードとは  
https://dev.classmethod.jp/etc/ecs-networking-mode/  

# to do  
・taskdefinition.jsonとbuildspec.ymlとbuildspec内のimagedefinition.jsonをいじってflaskのデプロイを完了させる。  
注意したほうがいいのは、CI/CDはあくまでも初期状態のサービスが動いていることは前提として、更新する際に初めてpipelineが機能する。  
つまり、一番最初のtaskdefinition.jsonはサービスの初期状態として定義する必要があって、そこにimagedefinitionで書き換えられてCI/CDで開発されていく感じ  
以下の記事を参考に進める  
https://www.m3tech.blog/entry/elixir-fargate-impl-2  
  
・ecsを起動したときに、githubにpushしていないのにgithubの内容を反映していたから、この挙動がどのようなものかを調査する  
  
・taskdefinition.jsonからdocker-compose.ymlを生成する  
ECSはクラウドで行うのでお金がかかってしまう。そこでまずはローカルの環境でテストをしたいときに以下のURLでdocker-composeを生成する  
https://dev.classmethod.jp/cloud/aws/ecs-local/  
  
・codedeployを追加する  
https://dev.classmethod.jp/cloud/aws/codepipeline-ecs-codedeploy/  

・ECSのタスクのdependsOnでHEALTHYにする  
https://christina04.hatenablog.com/entry/ecs-fargate-dependson-parameter  
https://qiita.com/kai_kou/items/5ad5e0f6d749ef724ad1  
  
・インフラ未経験が内定から入社までに読んだ本  
