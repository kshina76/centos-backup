# アーキテクチャ  

# 使用方法  
## 1.terraformでVPCなどのネットワークを構築  
```bash  
$ terraform init  
$ terraform plan  
$ terraform apply  
```

## 2.シェルスクリプトを実行してemrクラスタの作成  
サブネットIDとS3バケットIDを後で使うので、控えておく。  
```bash  
$ bash create_cluster.sh  
```

## 3.シェルスクリプトを実行してemrクラスタにジョブを渡して実行する  
さっき控えたIDを使ってシェルスクリプトの中身を書き換える。  

## クラスタの削除方法と削除されたか確認  
クラスタIDのメモをして、以下のファイルのIDを変更してから実行。  
```bash  
$ bash destroy_cluster.sh  
$ bash confirm_destroy.sh  
```

## 作成したいMapReduceを用いたデータ分析  
・気象情報のデータを使った分析  
https://qiita.com/khiraiwa/items/8ac019d11d93f5041f2d  
  
・平均値の算出  
http://www.mwsoft.jp/programming/hadoop/average_mapreduce.html  
  
・ワードカウント(MapReduceのhelloworld的なもの)  
https://blog.amedama.jp/entry/2017/05/20/121839  

## トラブルシューティング  
・create_cluster.shを実行したときにjson関連のエラーが出る  
jsonの書き方が間違っているときに出てくる。jsonの途中で円マークで改行しているので、改行しないようにする。  

・クラスタ作成時にEMR_DefaultRole is invalidと表示される  
EMR_DefaultRoleが無いので作成する。
```bash  
$ aws emr create-default-roles  
```
https://aws.amazon.com/jp/premiumsupport/knowledge-center/emr-default-role-invalid/  

・SSH接続ができない  
キーを登録してから接続するようにしたいとつなげないようになっている。  
https://qiita.com/toshihirock/items/1634f0dfeb7b6f7baf47  

## 参考文献  
・awscliを使ってemrクラスタを構築する  
https://dev.classmethod.jp/cloud/aws/hadoop-streaming-on-emr/  
