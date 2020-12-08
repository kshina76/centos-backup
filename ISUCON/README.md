# ISUCONやパフォーマンスチューニングまとめ

## 手法一時待避所
### ディスクI/O
1. CPU、メモリ、ディスクI/O、ネットワーク帯域などのハードウェアリソースを見る
2. ディスクI/Oが高かったら「メモリの無駄な使用」や「ミドルウェアがデータをメモリに載せる制限をかけている」や「単にメモリ不足」
3. 例えば、RDBMSの初期設定でバッファプールが小さい場合は大きくすることで、データを多くキャッシュしてくれるようになったり、クエリを改善したり
- https://dev.classmethod.jp/articles/dentry-cache/

### AWS Lambdaのパフォーマンスチューニング
- Lambdaはメモリサイズに比例してCPUパワーも割り当てられます。ですので、メモリ消費が少ないからとメモリサイズを下げますと、CPUパワーも下がってしまうところがLambdaのパフォーマンスチューニングの難しいところ
- https://dev.classmethod.jp/articles/reinvent-2019-svs224/
- https://dev.classmethod.jp/articles/lambda-performance-tuning/
<br></br>

## なぜWebアプリケーションのパフォーマンスが重要か
### UX: ちょっとでも待たせるとユーザは離れる
### KPI: Googleはスピード見てる､1秒遅れると
### インフラコスト
- AWS EC2の例
(クラウド時代ではちょっとした改善がそのままお金になる｡｡｡)

---

<br></br>

## Webアプリケーションのチューニングで行うこと
### レスポンスタイムが小さい
- リトルの法則により、安定した系において、レスポンスタイムが小さくなればスループットは向上するため、レスポンスタイムとスループットは相関
### スループット (req/s) が大きい
- 一秒あたりにどれだけのリクエストを捌けるか
### CPUやメモリなどリソース消費量が小さい
- リソース消費量の改善は、レスポンスタイムに寄与するというよりは、サーバ管理にまつわる人的または金銭的なコストを下げる
- そういった無駄を省くことで、アプリケーションの処理効率がよくなり、結果としてレスポンスタイムが良くなることはある

---

<br></br>

## 事前準備
### デプロイの自動化のスクリプトを書いておく
- CI/CDとかを使うという話ではなくて、チューニングする際に設定変更した後にDBやnginxを全てrestartして、繋ぎ直すから
- restartはバックエンドから行う

---

<br></br>

## オペレーション
### 0. チューニングの大まかな方針
- ベンチマークはnginxとかapacheでリクエストを大量送れるのでそういったものを使う
#### 0-1. ボトルネック解析
- nginxでアクセスログを解析
  - URLごとに解析するために行う
- MySQLでスロークエリログ
  - SQLの発行状況を見てN+1問題などが起きていないか解析する
  - pt-query-digestを使う
- プロファイラでコードレベルの実行時間解析
  - コードレベルでボトルネックになっているところはないかを解析する
  - golangならpprofが便利
#### 0-2. Opsチューニング
- OS
- MySQL
- nginx
- memcached
- redis
- アプリケーションのwebまわり

#### 参考文献
- https://blog.yuuk.io/entry/web-operations-isucon

<br></br>

### 1. リソース利用率の把握とログの確認
- リソース消費量を把握しておくことはボトルネック特定のヒントになる

#### 1-1. ログインしたら確認すること
#### 1-1-1. 他にログインしている人がいるか確認（w）
- 負荷を掛ける作業や再起動を掛ける作業をするときに、他の人がログインしていたら大変だから
#### 1-1-2. サーバの稼働時間の確認 (uptime)
#### 1-1-3. プロセスツリーをみる (ps)
- サーバにログインしたときに必ずと言っていいほどプロセスツリーを確認する
- そのサーバで何が動いているのかをひと目で把握できる
- `f`オプションでプロセスの親子関係を把握しやすい
  - 実際には同じプロセスグループなのに、同じプロセスが多重起動していておかしいと勘違いしやすいから
- プロセスごとのCPU利用率やメモリ使用量をみることができるから`pstree`より`ps`

```bash
ps auxf
```


<br></br>

### 2. MySQL(RDBMS)データサイズ確認
```sql
use database;
SELECT table_name, engine, table_rows, avg_row_length, floor((data_length+index_length)/1024/1024) as allMB, floor((data_length)/1024/1024) as dMB, floor((index_length)/1024/1024) as iMB FROM information_schema.tables WHERE table_schema=database() ORDER BY (data_length+index_length) DESC;
```

<br></br>

### 3. アクセスログの解析
- proxyでアクセスログを解析することにより、URLごとのリクエスト数やレスポンスタイムを集計
- alpという集計コマンドを使うと便利
  - https://github.com/tkuchiki/alp
- nginxでアクセスログをlstv形式で書き込む
  - https://qiita.com/key/items/038b7913b3bb0298c625

<br></br>

### 4. MySQLスロークエリログの解析
- 実行時間が閾値以上のクエリのログを吐いてくれるというもの
- long_query_time = 0 にして、全クエリのログをとる
- pt-query-digestで集計するのが便利
- 本番のベンチマークではオフにするのを忘れずに

<br></br>

### 5. チューニング
#### 5-1. 静的ファイルのReverse Proxyで配信
- Reverse Proxyは画像,CSS,JSを返す役割がある
#### 5-2. nginx化
- Webサーバ
- 高速に動作
- メモリ使用量が少ない

![2020-12-08 13 12のイメージ](https://user-images.githubusercontent.com/53253817/101439040-042e1900-3957-11eb-952c-65287a50cd51.jpeg)

#### 5-3. UNIXドメインソケット化
- 一つのサーバにミドルウェアが同居している場合に使える
  - 実務では分けると思うから使えないかな？？
- 「proxy <-> app <-> db」をTCPでやるのは無駄が多い
- TCPだと遅い
- run.iniを書き換えていた。やり方はよくわからんから調べる

![2020-12-08 13 20のイメージ](https://user-images.githubusercontent.com/53253817/101439659-50c62400-3958-11eb-9767-01f6b8ea7f21.jpeg)

#### 5-4. 外部プロセスの高速化
- 外部プロセスはメインのプロセス以外のプロセスのこと(多分)
- どのような外部プロセスを起動しているかを調べて、その外部プロセスを高速化するモジュールはないか調べる
  - 例えばmarkdownのparserを外部プロセスとして呼んでいたら、そのプロセスを高速化できるモジュールを調べて置き換えてみる

#### 5-5. N+1クエリ問題の解消
- SQLのログや実際のコードを見て無駄にfor文でSQLが発行されていないかを調べる
- https://qiita.com/massaaaaan/items/4eb770f20e636f7a1361

#### 5-6. index
- 値ごとに分岐していくようなB-Treeを構築して走査を高速化する手法(多分)
- indexを張るというのは、このことだと思う

![2020-12-08 15 57のイメージ](https://user-images.githubusercontent.com/53253817/101450607-24b59d80-396e-11eb-804a-c1534f82f669.jpeg)

![2020-12-08 15 57のイメージ](https://user-images.githubusercontent.com/53253817/101450608-254e3400-396e-11eb-83c0-b029011da280.jpeg)

#### MySQL、nginx、redis、memcachedチューニング
- https://kazeburo.hatenablog.com/entry/2014/10/14/170129

#### 参考文献
- https://www.slideshare.net/kazeburo/isucon-summerclass2014action2final
