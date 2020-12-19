# ISUCONやパフォーマンスチューニングまとめ

## 全体の参考文献一覧
- ISUCONの勝ち方
  - https://www.youtube.com/watch?v=vl1mYTq1ZYI&t=1604s
  - https://wiki.infra-workshop.tech/event/ISUCON8/ISUCON/ISUCONの勝ち方動画メモ
  - https://www.slideshare.net/kazeburo/isucon-yapcasia-tokyo-2015
- ISUCON予選突破を支えたオペレーション技術
  - https://blog.yuuk.io/entry/web-operations-isucon
- ベンチマークの取り方
  - https://tagomoris.hatenablog.com/entry/2018/10/26/150228
- Webサービスのパフォーマンスに関する考え方まとめ
  - https://qiita.com/kenjiszk/items/b33d0900e9cbf9fa60c0
- Linuxパフォーマンス調査などで使うコマンドメモ
  - https://qiita.com/toshihirock/items/0e0b20064730469e93e6
- いまさら聞けないLinuxとメモリの基礎＆vmstatの詳しい使い方
  - https://qiita.com/kunihirotanaka/items/70d43d48757aea79de2d
- ガチ勢のWebアプリケーションチューニング

## ブロッキングIO、ノンブロッキングIO、同期IO、非同期IOの違い
- https://wa3.i-3-i.info/word1618.html
- https://blog.takanabe.tokyo/2015/03/ノンブロッキングi/oと非同期i/oの違いを理解する/


## 手法一時待避所
### ディスクI/O
1. CPU、メモリ、ディスクI/O、ネットワーク帯域などのハードウェアリソースを見る
2. ディスクI/Oが高かったら「メモリの無駄な使用」や「ミドルウェアがデータをメモリに載せる制限をかけている」や「単にメモリ不足」
3. 例えば、RDBMSの初期設定でバッファプールが小さい場合は大きくすることで、データを多くキャッシュしてくれるようになったり、クエリを改善したり
- https://dev.classmethod.jp/articles/dentry-cache/
### RDB
- indexを張る
- queryを置き換える
- Redisへキャッシュする
### static file配信
- nginxなどでwebサーバから配信
### network I/O
- request処理のconcurrency向上
  - golangならgoroutine
### network帯域
- Cache-Control Headerで外部でキャッシュ
  - browserとかで

## AWS Lambdaのパフォーマンスチューニング
- Lambdaはメモリサイズに比例してCPUパワーも割り当てられます。ですので、メモリ消費が少ないからとメモリサイズを下げますと、CPUパワーも下がってしまうところがLambdaのパフォーマンスチューニングの難しいところ
- https://dev.classmethod.jp/articles/reinvent-2019-svs224/
- https://dev.classmethod.jp/articles/lambda-performance-tuning/

## 計測ツールまとめ
### netdata
- cpu, memory, network I/OなどOSのリソース使用量を計測
- https://blog.adachin.me/archives/3446
### kataribe
- nginxなどのWebサーバのログを整形して表示
  - ログは所定のフォーマットにしておく
- URLごとのlatency、throughputを表示
  - countが全体におけるimpact
### pt-query-digest
- MySQLのslow logやtcpdump経由で分析するツール
### 参考文献
- https://speakerdeck.com/south37/new-grad-isucon-for-learning?slide=15

## 可視化ツールまとめ
### td-agent
### fluentd
### kibana
### elasticsearch

---

<br></br>

## なぜWebアプリケーションのパフォーマンスが重要か
### UX: ちょっとでも待たせるとユーザは離れる
### KPI: Googleはスピード見てる､1秒遅れると
### インフラコストの提言
- 必要なサーバ台数の減少
- 高負荷サーバ現象
  - メンテナンスの手間が現象
- AWSのようなクラウド時代ではちょっとした改善がそのままお金になる

---

<br></br>

## サーバの種類と行うチューニング概要
### 1. Webサーバ
#### 1-1. 種類
- Apache httpd, Nginx, h2o ...
#### 1-2. 用途
- 静的コンテンツの提供
  - html, css/js, jpg/png, ...
- 動的コンテンツのために、リバースプロキシとして使用
  - セッションコントロール
  - ロードバランシング
  - Authentication(認証)
  - Caching(キャッシュ)
#### 1-3. チューニング
- そもそもサーバを変更する
  - Apache httpd -> Nginx など 
- パラメータの変更
  - プロセス・スレッド数設定、最大コネクション数設定
- レスポンス処理方法の変更
  - 静的ファイル(js, css, 変化しないhtml)をWebサーバから返す

<br></br>

### 2. Applicationサーバ
#### 2-1. 用途
- アプリケーションコードの実行
  - HTML, HTTP API endpoint
- Viewの生成
- SQLの呼び出し
- 外部APIの呼び出し
- キャッシュの参照
#### 2-2. チューニング
- プロセス数・スレッド数の変更 
- ソフトウェアの変更 
  - Unicorn -> Rhebok, Starman -> Starlet, などなど

<br></br>

### 3. Databaseサーバ
#### 3-1. 種類
- MySQL, PostgreSQL, Oracle DB, MS SQLServer, MongoDB, Cassandra, Redis
#### 3-2. 用途
- データの格納
- データへのCRUD
#### 3-3. チューニング
- クエリ単位のもの
  - インデックスの追加
- サーバ単位のもの
  - バッファ設定変更
  - コネクション単位の設定変更

<br></br>

### 4. Cacheサーバ
#### 4-1. 種類
- Memcached, Redis, Varnish cache, Squid, Apache httpd(mod_cache), Nginx
#### 4-2. 用途
- ページ全体のキャッシング(HTML) 
- ページのパーツのキャッシング(HTML)
- caching query results(objects)
- ...
- cache everything w/ high costs

<br></br>

### 5. OS
#### 5-1. チューニング
- SELinuxを切る
- ほか、だいたい途中で必要になる系
  - ソケット再利用間隔の設定など sysctl系
  - プロセスがopenできるディスクリプタ数など limits.conf系

<br></br>

### 6. アプリケーション
#### 5-1. チューニング1
- 複数サーバをきちんとうまく使う
  - CPU、メモリ、Disk I/O、ネットワーク帯域
- データの正規化/非正規化により計算量を減らす
- 無駄なデータベース問合せを減らす
- レスポンスを待たせてもいいリクエストのハンドラに処理をまとめる
#### 5-2. チューニング2
- キャッシュ
- 処理の非同期化
- 画像・動画・CSS/JSファイルなどデータの最適化
- レスポンス変更によるHTTPリクエストの削減
#### 5-3. チューニング3(適切な分散処理構成の設計とデプロイ)
- ネットワーク帯域を稼ぐ(Webサーバを分散する)
- 分散できるCPU処理をできるだけ分散する
- 分散できない処理は適度にまとめる
- キャッシュしたコンテンツを即座に返す
- 表裏のネットワークがあるなら活用する
- 何度も返すコンテンツは確実にキャッシュする
- Failにならない程度にデータに手を入れる
- HTTPのプロトコルを知る
  - keepalive, redirect, cookie, cache-control, ...

<br></br>

### 参考文献
- https://www.slideshare.net/tagomoris/isucon20151
- https://www.slideshare.net/tagomoris/isucon20152

---

<br></br>

## サーバのリソースの種類
### CPU
- 計算する人。脳みそ。
- 無駄にループが走っていて計算回数が多かったりするとここがネックになる。
- 基本的には、CPUが最終的なネックになって来る。
- ハード的にはコア数がどんどん増えているのでマルチコアを考慮した使い方をしていく事が大事。
### Memory
- プログラムをロードしておくところ。机の広さに例えられる。
- 一つのプロセスを立ち上げるのに大量にメモリを使ったりするとコスト効率が悪くなる。
- また、出来るだけプロセス間でメモリを共有出来るようにすると多くのプロセスが立ち上げられるようになる。
- CPUにネックが無い場合、プロセス数の上限は大抵メモリで決まり、どのくらいリクエストがさばけるのかはプロセス数で決まるのでそこの見積もりは重要。
### Disk IO
- Diskの読み取り速度。
- メモリに乗らない情報はDiskに書き出したり読み出したりするがそこの速度差は比較にならないほどDiskに書く方が遅いため、大量のIOが発生する様な処理を行うとそこで処理が詰まったりする。
### Network
- NetworkもDisk IOと同じ一面があり、Networkで詰まった結果、全体の処理が詰まったりする。
- また、無駄に転送量が多い場合にはそこでも余計なコストが発生する。

---

<br></br>

## ボトルネック一覧(一部)
- HTTPD? connections? cpu? memory? 
- Application? connections? cpu? memory? 
- RDBMS? read? write? 
- Network? data size? latency? 
- ボトルネックは解決するたびに移っていく

## プログラマが知るべき全レイテンシ一覧
- レイテンシが短いところをチューニングし続けても効果は低い

![Us34eGovK2mazpAtfrCuzk](https://user-images.githubusercontent.com/53253817/101480066-7ffb8600-3996-11eb-922b-cbf7458a9da0.png)

### 参考文献
- https://logmi.jp/tech/articles/323295

---

<br></br>

## Webアプリケーションのチューニングで行うこと
### レスポンスタイムが小さい
- レスポンスタイムとは
  - 「1リクエスト -> 1レスポンス」の時間
- リトルの法則により、安定した系において、レスポンスタイムが小さくなればスループットは向上するため、レスポンスタイムとスループットは相関
### スループット (req/s) が大きい
- 1秒に返せるレスポンスの数
- 短いレスポンスタイム + 高いスループット = 良いパフォーマンス
### CPUやメモリなどリソース消費量が小さい
- リソース消費量の改善は、レスポンスタイムに寄与するというよりは、サーバ管理にまつわる人的または金銭的なコストを下げる
- そういった無駄を省くことで、アプリケーションの処理効率がよくなり、結果としてレスポンスタイムが良くなることはある
### 頻度とレスポンス時間
- ｢重たいところが優先｣とは限らない
### 高速なWebサーバアプリケーションを構築するための6つの経験則
1. 時期尚早な最適化を回避する
  - とりあえずアプリケーションを組んでみてから、あとでプロファイラを使って最適化する
  - 「二重引用符で囲んだ文字列は単一引用符で囲んだ文字列より遅いのか?」などという、くだらないことを心配する必要は一旦しない
2. 最小限の作業で問題を解決する
3. 今すぐやらなくてもいい作業は延期する
4. 使えるときはキャッシュを使う
5. リレーショナルデータベースのN+1問題を理解し、回避する
6. 可能ならアプリケーションに水平スケーラビリティをもたせる
- https://postd.cc/6-rules-of-thumb-to-build-blazing-fast-web-server-applications/

---

<br></br>

## 事前準備
### デプロイの自動化のスクリプトを書いておく
- CI/CDとかを使うという話ではなくて、チューニングする際に設定変更した後にDBやnginxを全てrestartして、繋ぎ直すから
- restartはバックエンドから行う
### チートシートの準備
- middlewareの設定項目など
- https://gist.github.com/south37/d4a5a8158f49e067237c17d13ecab12a
### 使うツールの選定
- 業務だとAmazon X-Rayを使うことが多いらしい

---

<br></br>

## オペレーション
### 0. チューニングの大まかな方針
- **「計測 -> 改善」のサイクルを回し続けるのが重要**
- とりあえずベンチマークを動かしてから深掘りしていく
- ベンチマークはnginxとかapacheでリクエストを大量送れるのでそういったものを使う
- まずは以下のチューニングに沿って行ってみる
  - https://www.prime-strategy.co.jp/resource/pdf/DevelopersSummit2020.pdf
  - https://postd.cc/6-rules-of-thumb-to-build-blazing-fast-web-server-applications/
### 0-1. ボトルネック解析
#### 0-1-1. リソース利用率の把握とログの確認
- nginxでアクセスログを解析
  - URLごとに解析するために行う
- サーバの負荷確認なども
#### 0-1-2. MySQLでスロークエリログ
- SQLの発行状況を見てN+1問題などが起きていないか解析する
- pt-query-digestを使う
#### 0-1-3. アプリケーションのプロファイリング
- プロファイラでコードレベルの実行時間解析
  - コードレベルでボトルネックになっているところはないかを解析する
  - golangならpprofが便利
### 0-2. サーバ構成の確認
### 0-3. Opsチューニング
- OS
- MySQL
- nginx
- memcached
- redis
- アプリケーションのwebまわり
### 0-4. Webサーバの選択
- Apache v. Nginx
- Nginx v. h2o
  - Nginx: プロセス､設定は色々できる
  - h2o: スレッド､コンテキストスイッチが有利
### 0-5. Webアプリケーションのチューニング
- わかりやすい重い処理をチューニングする
  - 外部プロセス起動
  - HTMLテンプレート
  - テキスト､画像の変換
  - RDBMS/Cacheとの接続
  - N+1問題

#### 参考文献
- https://blog.yuuk.io/entry/web-operations-isucon

<br></br>

### 1. リソース利用率の把握とログの確認
- リソース消費量を把握しておくことはボトルネック特定のヒントになる
- ここを参考にしてまとめた
  - https://blog.yuuk.io/entry/linux-server-operations
- iperfを使ったベンチマーク
  - https://blog.yuuk.io/entry/linux-networkstack-tuning-rfs
- ここで紹介していない色々なコマンドが載っている
  - https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55

- あとでまとめるコマンド
  - 異常を発見したあとのオペレーション
    - strace...システムコールレベルでアプリケーション動作確認
    - gdb...デバッガ
    - tcpdump...通信内容のキャプチャ
  - サーバ負荷の確認(どれかに使い慣れる)
    - top
    - iftop: Network
    - iotop: Disk I/O
    - dstat

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

#### 1-2-2. iostat
- ディスクI/O状況を確認できる
- `-d`でインターバルを指定できて、だいたい5秒に設定する
  - ファイルシステムのバッファフラッシュによるバーストがあり、ゆらぎが大きいので、小さくしすぎないことが重要 
- `-x`で表示する情報を拡張できる

```bash
$ iostat -dx 5
Linux 3.10.23 (blogdb17.host.h)     02/18/16    _x86_64_    (16 CPU)

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
xvda              0.00     3.09    0.01    3.25     0.13    36.27    22.37     0.00    1.45    1.59    1.45   0.52   0.17
xvdb              0.00     0.00    0.00    0.00     0.00     0.00     7.99     0.00    0.07    0.07    0.00   0.07   0.00
xvdf              0.01     7.34   49.36   33.05   841.71   676.03    36.83     0.09    8.08    2.68   16.13   0.58   4.80

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
xvda              0.00     3.20    0.40    2.80     2.40    30.40    20.50     0.00    0.25    0.00    0.29   0.25   0.08
xvdb              0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
xvdf              0.00     5.00  519.80    4.00  8316.80    96.00    32.12     0.32    0.61    0.60    1.40   0.52  27.36
```

- iostatの注意点
  - 1度目の出力はディスクデバイスが有効になってから現在まのの累積値
  - 現在の状況を知る場合は、2度目以降の出力をみる

- この情報の見方
  - `IOPS(r/s、w/s）`と`%util`に着目することが多い
  - 上記の場合、`r/s`が519と高めで、`%util`が27%なので、そこそこディスクの読み出し負荷が高いことがわかる

#### 1-2-3. netstat / ss
- `netstat`はネットワークに関するさまざまな情報をみれる
- TCPの通信状況をみるのによく使う
- `-t`でTCPの接続情報を表示
- `-n`で名前解決せずIPアドレスで表示
  - `-n`がないと連続して名前解決が走る可能性があり、接続が大量な状況だとつまって表示が遅いということがありえる(-n なしでも問題ないことも多いので難しい）
- `-l`でLISTENしているポートの一覧をみれる。
  - 下記の場合、LISTENしているのは`2812, 5666, 3306, 53549, 111, 49394, 22, 25`

```bash
$ netstat -tnl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:2812            0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:5666            0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:53549           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:49394           0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN
tcp6       0      0 :::54282                :::*                    LISTEN
tcp6       0      0 :::111                  :::*                    LISTEN
tcp6       0      0 :::22                   :::*                    LISTEN
tcp6       0      0 :::53302                :::*                    LISTEN
tcp6       0      0 :::25                   :::*                    LISTEN
```

- TCPの全部のステートをみるには`-a`を指定
- `-o`はTCP接続のタイマー情報
- `-p`はプロセス名の表示 (`-p`にはroot権限が必要)

```bash
$ sudo netstat -tanop
...
tcp        0      0 10.0.0.10:3306         10.0.0.11:54321        ESTABLISHED 38830/mysqld keepalive (7190.69/0/0)
tcp        0      0 10.0.0.10:3306         10.0.0.12:39150       ESTABLISHED 38830/mysqld keepalive (7157.92/0/0)
tcp        0      0 10.0.0.10:3306         10.0.0.13:49036         TIME_WAIT  38830/mysqld timewait (46.03/0/0)
tcp        0      0 10.0.0.10:3306         10.0.0.14:41064         ESTABLISHED 38830/mysqld keepalive (7223.46/0/0)
tcp        0      0 10.0.0.10:3306         10.0.0.15:34839        ESTABLISHED 38830/mysqld keepalive (7157.92/0/0)
...
```

- 一番、よくみるのは、このホストはどのホストから接続されているか
  - なぜか本番サーバなのに、ステージングサーバから接続されているというようなことがわかったりすることもある

- 他にも、単にやたらと接続が多いなとかざっくりした見方もする
  - そのときに、TCPのステートでESTABLISHED以外がやたらと多くないかなどをみたりする

### 1-3. ログ調査
- いうまでもなくログ調査は重要
- ログをみるためには、OSや、各種ミドルウェア、アプリケーションが吐くログがどこに吐かれているかを知る必要がある
- **基本的には`/var/log`以下を眺めてそれっぽいものをみつけて`tail`**
- **自分が担当して開発しているシステムのログの位置は確認しておいたほうがよい**

#### 1-3-1. /var/log/messages or /var/log/syslog
- まずはここを見る。カーネルやOSの標準的なプロセスのログをみることができる。
- 他にもcron実行するコマンドの標準出力や標準エラー出力を明示的に`logger`にパイプしている場合などはここにログが流れる

#### 1-3-2. /var/log/secure
- ssh 接続の情報がみれる
- 他の人がssh接続しているのに接続できない場合、ここに吐かれているログをみると原因がわかることがある

#### 1-3-3. /var/log/cron
- cronが実行されたかどうかがわかる
- ただし、cronが実行したコマンドの標準出力または標準エラー出力が`/var/log/cron`に出力されるわけではなく、あくまでcronのスケジューラが動いたかどうかがわかるだけ
- cronが実行したコマンドの標準出力または標準エラー出力はどこに出力されるか決まっているわけではなく、crontab内でloggerコマンドにパイプしたり、任意のログファイルにリダイレクトしたりすることになる

#### 1-3-4. /var/log/nginx, /var/log/httpd, /var/log/mysql
- ミドルウェアのログは`/var/log/{ミドルウェア名}`以下にあることが多い
- 特によくみるのはリバースプロキシのアクセスログやDBのスロークエリログ
- 自分が開発しているシステムのログの位置は確認しておいたほうがよい

#### 1-3-5. /etc
- `/var/log`以下にログを吐くというのは強制力があるものではないので、ログがどこにあるのか全くわからんということがある
- ログファイルのパスは設定ファイルに書かれていることもある。設定ファイルは`/etc`以下にあることが多いので、`/etc/{ミドルウェア名}`あたりをみて、設定ファイルの中身を`cat`してログファイルのファイルパスがないかみてみる

#### 1-3-6. lsof
- `/etc`をみてもわからんというときは最終手段で、`lsof`を使う。`ps`や`top`でログをみたいプロセスのプロセスIDを調べて、`lsof -p <pid>`を打つと、そのプロセスが開いたファイルディスクリプタ情報がみえるので、ログを書き込むためにファイルを開いていれば、出力からログのファイルパスがわかる
- 他には例えば`daemontools`を使っていると、`/service`、もしくは`/etc/service`以下に`multilog`が吐かれているなど、使用しているスーパーバイザによっては、特殊なディレクトリを使っている可能性があります。

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
  - 回数が多いクエリを見つけることが可能
- pt-query-digestで集計するのが便利
- 本番のベンチマークではオフにするのを忘れずに
- レスポンスタイムが悪いクエリから順番に対策をしていく
- レスポンスは悪くないけど、回数が多いクエリの対策
- アプリケーションそもそものデータの参照回数を減らす
  - キャッシュを活用してMySQLへのクエリ回数を抑える

<br></br>

### 5. アプリケーションのプロファイリング
- 実際に遅いリクエストが特定出来た場合に詳細を追う為のツール
- go言語のpprofというプロファイリングツールが便利
  - https://medium.com/eureka-engineering/go言語のプロファイリングツール-pprofのweb-uiがめちゃくちゃ便利なので紹介する-6a34a489c9ee


<br></br>

### 6. チューニング（大雑把に）
- Webサーバの選択
  - Apache v. Nginx
  - Nginx v. h2o
    - Nginx: プロセス､設定は色々できる
    - h2o: スレッド､コンテキストスイッチが有利
- わかりやすい重い処理をチューニングする
  - 外部プロセス起動
  - HTMLテンプレート
  - テキスト､画像の変換
  - RDBMS/Cacheとの接続
  - N+1問題
#### 6-1. 静的ファイルのReverse Proxyで配信
- Reverse Proxyは画像,CSS,JSを返す役割がある
#### 6-2. nginx化
- Webサーバ
- 高速に動作
- メモリ使用量が少ない

![2020-12-08 13 12のイメージ](https://user-images.githubusercontent.com/53253817/101439040-042e1900-3957-11eb-952c-65287a50cd51.jpeg)

#### 6-3. UNIXドメインソケット化
- 一つのサーバにミドルウェアが同居している場合に使える
  - 実務では分けると思うから使えないかな？？
- 「proxy <-> app <-> db」をTCPでやるのは無駄が多い
- TCPだと遅い
- run.iniを書き換えていた。やり方はよくわからんから調べる

![2020-12-08 13 20のイメージ](https://user-images.githubusercontent.com/53253817/101439659-50c62400-3958-11eb-9767-01f6b8ea7f21.jpeg)

#### 6-4. 外部プロセスの高速化
- 外部プロセスはメインのプロセス以外のプロセスのこと(多分)
- どのような外部プロセスを起動しているかを調べて、その外部プロセスを高速化するモジュールはないか調べる
  - 例えばmarkdownのparserを外部プロセスとして呼んでいたら、そのプロセスを高速化できるモジュールを調べて置き換えてみる

#### 6-5. N+1クエリ問題の解消
- SQLのログや実際のコードを見て無駄にfor文でSQLが発行されていないかを調べる
- https://qiita.com/massaaaaan/items/4eb770f20e636f7a1361

#### 6-6. index
- 値ごとに分岐していくようなB-Treeを構築して走査を高速化する手法(多分)
- indexを張るというのは、このことだと思う

![2020-12-08 15 57のイメージ](https://user-images.githubusercontent.com/53253817/101450607-24b59d80-396e-11eb-804a-c1534f82f669.jpeg)

![2020-12-08 15 57のイメージ](https://user-images.githubusercontent.com/53253817/101450608-254e3400-396e-11eb-83c0-b029011da280.jpeg)

#### MySQL、nginx、redis、memcachedチューニング
- https://kazeburo.hatenablog.com/entry/2014/10/14/170129

#### 参考文献
- https://www.slideshare.net/kazeburo/isucon-summerclass2014action2final

<br></br>

### 7. 詳細なチューニング（Nginxのパフォーマンステストの方法とチューニング）
#### 7-1. テストツールの種類と特徴

| テストツール | 説明                                                                    | 
| ------------ | ----------------------------------------------------------------------- | 
| httperf      | HPが開発した有名なオープンソース(Linux専用)                             | 
| Autobench    | httperfのラッパー。テストのメカニズムや詳細レポートの作りを改良している | 
| OpenWebLoad  | windowsもサポートしている小規模なオープンソース                         | 

#### 7-2. 利用するテストツール
- Autobenchを利用する
  - Autobenchはグラフで結果を確認することができるので見やすい
  - サーバが飽和状態になるまでリクエストを送り続けてくれる
  - テスト結果を.tsvファイルにエクスポートできる

#### 7-3. Autobenchを導入する
- Autobenchはhttperfのラップしてる為httperfを導入する

```bash
# httperfの導入
$ sudo wget http://httperf.googlecode.com/files/httperf-0.9.0.tar.gz
$ tar zxf httperf-0.9.0.tar.gz
$ cd httperf-0.9.0
$ ./configure
$ make
$ sudo make install
```

```bash
# Autobenchの導入
$ wget http://www.xenoclast.org/autobench/downloads/autobench-2.1.2.tar.gz
$ tar zxf autobench-2.1.2.tar.gz
$ cd autobench-2.1.2
$ make
$ sudo make install
```

#### 7-4. Autobenchの使い方
- autobenchのあとにスイッチを記述していく
- スイッチの値を変えながらサーバに負荷をかけてパフォーマンスを計測し改善する
- 主なスイッチは以下

| スイッチ    | 意味                                           | 
| ----------- | ---------------------------------------------- | 
| --host1     | テストしたいwebサイトのホスト名                | 
| --uri       | ダウンロードされるファイルパス                 | 
| --quiet     | 画面にhttperfの情報を出さない                  | 
| --low_rate  | テストの最初の段階での1秒あたりの接続数        | 
| --high_rate | テストの終わりの段階での1秒あたりの総接続数    | 
| --rate_step | 毎回のテスト後に増やす接続数                   | 
| --num_call  | 1つの接続あたりいくつのリクエストを送るか      | 
| --num_conn  | 接続総数                                       | 
| --timeout   | リクエストが失われたとされる秒数               | 
| --file      | 指定したファイルに結果をエクスポートする(.tsv) | 

#### 7-5. デフォルトのパフォーマンスを計測してみる
- 以下サンプルのスイッチを付けて計測を開始する

```bash
$ autobench --single_host --host1 192.168.33.11 --uri1 /index.html --quiet --low_rate 20 --high_rate 200 --rate_step 20 --num_call 10 --num_conn 5000 --timeout 5 --file ~/results.tsv
```

- 待つこと数分`results.tsv`に計測結果が記録されていく

#### 7-6. results.tsvの見方

![2020-12-08 19 27のイメージ](https://user-images.githubusercontent.com/53253817/101472269-bd0e4b00-398b-11eb-8a92-f953ae87995a.jpeg)

#### 7-7. 実際に結果を見てみる

![2020-12-08 19 28のイメージ](https://user-images.githubusercontent.com/53253817/101472270-bda6e180-398b-11eb-90fd-5ce4b0c644d2.jpeg)

- どんなに性能上げてもエラーがあれば意味なさそうなので気をつけたい
- 以上がデフォルトのNginxのパフォーマンステストの方法

#### 7-8. Autobenchの何がいいか
- httperfより見やすい
- tsvで結果が作られるのでグラフ化することもできるので良い
- httperfをラップしているので信頼度が高い

#### 7-9. Nginxをチューニングする際に覚えておくこと
- 以下を変更しながらチューニングするといいらしい

![2020-12-08 19 29のイメージ](https://user-images.githubusercontent.com/53253817/101472272-bed80e80-398b-11eb-9554-d76dc6a682a3.jpeg)

#### 7-10. メモ

```
cat /usr/include/linux/posix_types.h
#ifndef _LINUX_POSIX_TYPES_H
#define _LINUX_POSIX_TYPES_H

#include <linux/stddef.h>

/*
 * This allows for 1024 file descriptors: if NR_OPEN is ever grown
 * beyond that you'll have to change this too. But 1024 fd's seem to be
 * enough even for such "real" unices like OSF/1, so hopefully this is
 * one limit that doesn't have to be changed [again].
 *
 * Note that POSIX wants the FD_CLEAR(fd,fdsetp) defines to be in
 * <sys/time.h> (and thus <linux/time.h>) - but this is a more logical
 * place for them. Solved by having dummy defines in <sys/time.h>.
 */

/*
 * This macro may have been defined in <gnu/types.h>. But we always
 * use the one here.
 */
#undef __FD_SETSIZE
#define __FD_SETSIZE    1024

typedef struct {
    unsigned long fds_bits[__FD_SETSIZE / (8 * sizeof(long))];
} __kernel_fd_set;

/* Type of a signal handler.  */
typedef void (*__kernel_sighandler_t)(int);

/* Type of a SYSV IPC key.  */
typedef int __kernel_key_t;
typedef int __kernel_mqd_t;

#include <asm/posix_types.h>

#endif /* _LINUX_POSIX_TYPES_H */
```

#### 7-11. Nginxのチューニングをさらに極限まで引き上げる方法
- https://qiita.com/iwai/items/1e29adbdd269380167d2
- https://lincolnloop.com/blog/tracking-application-response-time-nginx/

#### 参考文献
- http://raichel.hatenablog.com/entry/2015/11/23/Nginxのパフォーマンステストの方法とチューニング

---

<br></br>

### 8. Webフロントエンドの表示速度、最速化手法
- https://qiita.com/zaru/items/51ee8a5be22b75a42927


---

<br></br>

## トラブルシューティング
### トラブルシューティング手法6パターン
#### 1.トップダウン方式...OSI参照モデルの上位レイヤから調査
#### 2. ボトムアップ方式...OSI参照モデルの下位レイヤから調査
#### 3. 分割統治方式...OSI参照モデルの中位レイヤから調査
- ネットワーク層から徐々に上の層(トランスポート層、セッション層...)を調査していく
- 例えばpingやtracerouteコマンドを用いた場合
  - 問題がない => トランスポート層を調べていく
  - 問題がある => ネットワーク層、データリンク層、物理層のいずれかで起きている障害
- 参考文献
  - http://eno0514.hatenadiary.jp/entry/20150507/1430934856
#### 4. トラフィックパス追跡方式...どこからどこまでつながっているかを調査
- 問題の切り分けの流れ

![nwts12m](https://user-images.githubusercontent.com/53253817/101201367-fe141000-36aa-11eb-8b6c-87d4fc5e38df.png)

- 参考文献
  - https://www.itbook.info/network/trableshooting03.html
#### 5. 設定比較方式...他の正常な機器と設定を比較、過去の正常な状態での設定と比較
#### 6. コンポーネント交換方式...ケーブルなどを交換してみる
#### 参考文献
- https://www.cisco.com/c/dam/global/ja_jp/training-events/es/cy11/pdf/cisco3-20110610interop.pdf

### ネットワーク層、トランスポート層のトラブルシューティング(ネットワークのトラブルシューティング)
- https://made.livesense.co.jp/entry/2016/05/10/083000

### Webサーバのトラブルシューティング
- curlコマンドがよく使われるが、telnetやnmapもかなり便利
  - https://www.itbook.info/network/http03.html
