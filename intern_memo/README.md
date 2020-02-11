# control towerとlanding zone  
・AWS ベストプラクティスをベースに構成されたセキュアでスケーラブルなマルチアカウント環境  
  
・かつてはlanding zone solutionとして提供されていたが現在はcontrol towerで簡単に作成できるようになっている  
  
・というよりはcontrol towerのlanding zoneが走って必要なアカウントやリソースを一式自動作成する感じ  

## 参考文献  
・control towerの概要をわかりやすく解説  
https://qiita.com/14kw/items/46a0054d90a4f5d779c4  
  
・control towerで作られるもの  
https://docs.aws.amazon.com/ja_jp/controltower/latest/userguide/how-control-tower-works.html  
  
・pythonでcontrol towerで作成したテンプレートを抜き出す  
https://dev.classmethod.jp/cloud/aws/export-cfn-template-from-control-tower/  
  
# account factroy  
・control towerでベースライン環境(マスターアカウント的な？)作った後にチームやアプリケーションに応じたアカウントを作成するところ。名前の通り「アカウントを作る工場」のこと。  
  
・control towerを使うとservice catalogに自動的にaccount factoryが作られるから、アカウントを新たに作りたかったらservice catalogのコンソールに行って「製品」を起動するという感じだと思う。
  

# cloud formation  
・Infrastructure as codeを実現するためのAWSのサービス  
  
・terraformはサードパーティ製だがcloud formationはawsのマネージドサービスという立ち位置  
  
・yamlで記述するのが特徴  

  
## 参考文献  
・cloud formationの説明とエントリ  
https://dev.classmethod.jp/cloud/aws/cloudformation-beginner01/  

  
# service catalog  
・cloud formationをいい感じに実行するためのもの  
  
・環境を構築する権限が無くても「起動」はできるようになる  
cloud formationを起動するにはテンプレートが提供するリソースを全て作成できる権限が必要になる。つまりVPCに加えてEC2とS3のリソースを作成するテンプレートをcloud formationで書いたとしたらEC2のIAM権限やS3のIAM権限が必要になるが、service catalogでlaunchを設定することで「作成」はできなくても「起動」はできるようになる。  
  
・使い道としては、開発者が作成したインフラ(cloud formation)の中身を変えれない状態でユーザに配布することで、ユーザがその製品を安全に使うことができる。さらにそれをユーザが適宜起動停止をすることで運用をユーザに任すことも可能になるのかもしれない。  
  
## 参考文献  
・めちゃくちゃわかりやすい  
https://dev.classmethod.jp/cloud/aws-service-catalog/  
  
・運用方法  
https://dev.classmethod.jp/cloud/aws/serca/  
  
# aws glue  
・データ分析のサービスで、EMRと比較される  
  
# aws step  
・lambdaを連携させてサーバレスワークフローを実現する  
  
# やりたいこと  
1.IaCをやるわけではないからcalalogとcontrol towerは手作業で作っておく。(IaCをやるならpythonでsubprocessでawscliのapiを叩いて自動で構築)  
  
2.control towerで作成してあるservice catalogの中のaccount factoryからtenantAを作成  
  
3.service catalogにcloud formationをいれて製品を作る  
  
4.TenantA内で3のservice catalogが実行されてcloud formationが起動  
  
5.VPCやEMRなどのリソースが作成される  
  
## 参考文献  
・GitHub+API Gateway+LambdaでSlackに通知を投げてみた  
https://dev.classmethod.jp/cloud/aws/github-slack/  
  
・GitHubのeventをLambdaで処理してSlackへ通知  
https://ijin.github.io/blog/2015/08/06/github-to-lambda-to-slack/  
  
・参考になった公式ドキュメント  
https://aws.amazon.com/jp/blogs/news/aws-control-tower-set-up-govern-a-multi-account-aws-environment/  
  