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
### 0-1. ボトルネック解析
- nginxでアクセスログを解析
  - URLごとに解析するために行う
- MySQLでスロークエリログ
  - SQLの発行状況を見てN+1問題などが起きていないか解析する
  - pt-query-digestを使う
- プロファイラでコードレベルの実行時間解析
  - コードレベルでボトルネックになっているところはないかを解析する
  - golangならpprofが便利
### 0-2. Opsチューニング
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

### 1-1. ログインしたら確認すること
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
$ ps auxf
```

#### 1-1-4. NICやIPアドレスの確認 (ip)
- IPアドレスの構成はどのようになっているのか
- プライマリIPだけでなくセカンダリIPがついているのかなど

```bash
$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 00:16:3e:7d:0d:f9 brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.10/22 brd z.z.z.z scope global eth0
       valid_lft forever preferred_lft forever
    inet 10.0.0.20/22 scope global secondary eth0
       valid_lft forever preferred_lft forever
```

#### 1-1-5. ファイルシステムの確認（df）
- `-T`をつけるとファイルシステムの種別を確認できる
- `-h` をつけると、サイズ表記が人間に読みやすいフォーマットになる
- dfコマンドにより、ディスク容量以外にも、いくつかわかる
  - MySQLのようなデータをもつストレージサーバは、本体とは別の専用のディスクデバイスをマウントして使っていることがわかる（EC2のEBSボリュームやFusion-IOの ioDriveなど）
    - ストレージ専用のサーバをマウントすることで、IOを高速化できるから
  - 上記の出力例の場合、/data/redis に着目します。前述の「プロセスツリーをみる」により、Redisが動いていることもわかるので、RedisのRDBやAOFのファイルが配置されていると想像できる

```
$ df -Th
Filesystem                                             Type      Size  Used Avail Use% Mounted on
rootfs                                                 rootfs     20G  2.4G   17G  13% /
udev                                                   devtmpfs   10M     0   10M   0% /dev
tmpfs                                                  tmpfs     3.0G  176K  3.0G   1% /run
/dev/disk/by-uuid/2dbe52e8-a50b-45d9-a2ee-2c240ab21adb ext4       20G  2.4G   17G  13% /
tmpfs                                                  tmpfs     5.0M     0  5.0M   0% /run/lock
tmpfs                                                  tmpfs     6.0G     0  6.0G   0% /run/shm
/dev/xvdf                                              ext4     100G   31G    69G   4% /data/redis
```

### 1-2. 負荷状況確認
- 秒単位での負荷の変化やCPUコアごと、プロセスごとの負荷状況など、可視化ツールで取得していない詳細な情報がほしい時に使う
- Mackerelである程度あたりをつけて、サーバにログインしてみてコマンドを使って様子をみるというフローが一番多い
#### 1-2-1. top
- `top -c` をよく使う。 -c をつけると、プロセスリスト欄に表示されるプロセス名が引数の情報も入る
- さらに重要なのが、top 画面に遷移してから、 キーの`1`をタイプすることです。`1`をタイプすると、各CPUコアの利用率を個別にみることができる

```bash
top - 16:00:24 up 22:11,  1 user,  load average: 1.58, 1.43, 1.38
Tasks: 131 total,   2 running, 129 sleeping,   0 stopped,   0 zombie
%Cpu0  : 39.7 us,  4.1 sy,  0.0 ni, 48.6 id,  0.3 wa,  0.0 hi,  6.9 si,  0.3 st
%Cpu1  : 24.4 us,  1.7 sy,  0.0 ni, 73.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  : 14.7 us,  1.7 sy,  0.0 ni, 83.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu3  :  0.0 us,  2.0 sy, 98.0 ni,  0.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu4  :  3.3 us,  0.7 sy,  0.0 ni, 96.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu5  :  2.0 us,  0.3 sy,  0.0 ni, 97.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu6  :  2.3 us,  0.3 sy,  0.0 ni, 97.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu7  :  0.7 us,  0.3 sy,  0.0 ni, 99.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:   7199160 total,  5764884 used,  1434276 free,   172496 buffers
KiB Swap:        0 total,        0 used,        0 free,  5161520 cached

  PID USER      PR  NI  VIRT  RES  SHR S  %CPU %MEM    TIME+  COMMAND
16659 root      39  19  8612  632  440 R 100.3  0.0   0:12.94 /bin/gzip
 2343 nginx     20   0 60976  14m 1952 S  23.2  0.2 112:48.51 nginx: worker process
 2328 nginx     20   0 61940  15m 1952 S  19.9  0.2 111:49.12 nginx: worker process
 2322 nginx     20   0 61888  15m 1952 S  19.3  0.2 113:44.95 nginx: worker process
 2324 nginx     20   0 61384  14m 1952 S  16.6  0.2 113:30.52 nginx: worker process
 2340 nginx     20   0 61528  14m 1952 S  11.0  0.2 114:02.36 nginx: worker process
 ...
```

- この情報からわかること
  - 下のプロセスリストをみると、`/bin/gzip`がCPU 100%使いきっている。これはlogrotateがアクセスログを圧縮している様子を表している。
  - 上段のCPU利用率欄をみると、Cpu3 が 0.0 idとなっている。`id`は`idle`の略であり、`id`が`0%`ということはCpu3を使いきっているということ。
  - これらの状況から gzip プロセスが Cpu3 を使いきっているということが推測できます。

- CPU利用率欄には他にも、us, sy、ni、wa、hi、si、stがある。これらは、CPU利用率の内訳を示しています。よくみるのは、us、sy、waの3つ
  - us(user): OSのユーザランドにおいて消費されたCPU利用の割合。userが高いということは、アプリケーション（上記の場合nginx）の通常の処理にCPU処理時間を要していることです。
  - sy(system): OSのカーネルランドにおいて消費されたCPU利用の割合。systemが高い場合は、OSのリソース（ファイルディスクリプタやポートなど）を使いきっている可能性があります。カーネルのパラメータチューニングにより、負荷を下げることができるかもしれません。fork 回数が多いなど、負荷の高いシステムコールをアプリケーションが高頻度で発行している可能性があります。straceでより詳細に調査できます。
  - wa(iowait): ディスクI/Oに消費されたCPU利用の割合。iowaitが高い場合は、次の iostat でディスクI/O状況をみましょう。

- **基本は各CPUコアの`idle`をざっと眺めて、`idle`が`0`に近いコアがないかを確認し、次に`iowait`をみてディスクI/Oが支配的でないかを確認し、`user`や`system`を見る**

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
