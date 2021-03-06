# インフラエンジニアの教科書 書籍メモ

## 1.インフラエンジニアの仕事
### インフラ設計
- 要件に見合うインフラの設計を行う
- サーバスペック選定
  - CPU、メモリ、ディスク、RAID、NIC、パワーサプライユニット冗長化要否、保守の年数、保守レベル、拡張性、物理サイズや重量
- ネットワーク構成
  - 各スイッチのキャパシティはどのくらいにするのか
  - 採用するベンダー
  - 保守年数
  - ネットワークインタフェースごとの通信量や冗長化の要否
- データベース設計
  - RDBMSの選定
  - 必要容量算出
  - データベーススキーマと物理的なデータ配置の決定
- 運用体制
  - インフラ監視ツールを使って、障害を検知した時だけ社員が対応するといったもの
### インフラ構築
- 機器のインストールや設定、動作テスト、負荷テスト
### インフラ運用
- 障害対応
  - アクセス増への対処
  - 不適切な権限設定によってアクセスできない場合の対処
- キャパシティ
  - アクセス数やデータ数の増大時のインフラのキャパシティの見直し
  - 逆にオーバースペックになっていないかどうかも
- インフラ起因でない原因の切り分け
  - 内部ネットワークの問題なのか、外部ネットワークの問題なのかといった切り分け

<br></br>

## 2.サーバ
### サーバの選定
#### サーバ要件

![f11ad982aa1fe8ed2ca4272bf4771c53](https://user-images.githubusercontent.com/53253817/101117094-a5e8f980-3629-11eb-9536-495c76978c50.jpeg)

#### サーバスペックの決め方(3パターン)
- 実際の環境を試験的に構築し、測定結果から判断する
  - 基幹系といった重要なシステムの場合の決め方
- 仮決めしたサーバスペック機器を本番投入し、実際のハードウェアリソース利用状況を測定した上でサーバやサーバのパーツを増減していく
  - オンラインゲームのように事前にアクセス数が想定できない場合の決め方
- 消去法でスペックを絞り込んでいく
  - サービスの性質が特定されている場合
  - 例えば、Webサーバはメモリの消費だけ多いから、メモリを多く積むとか
#### スケールアウトとスケールアップ
- サーバのキャパシティを向上させるアプローチ
- スケールアウト
  - 性能が足りなくなったら、サーバを増やす方法
- スケールアップ
  - 性能が足りなくなったら、メモリを増設するとかのようにパーツを増やす方法

### CPU
#### CPU用語
- ソケット数
  - CPUの個数
- コア数
  - CPUの主要計算部分
- スレッド数
  - 一つのコアが処理できる数
  - ハイパースレッディングありだと、コア数が倍になる
- 動作周波数
  - 一秒間に刻むクロックの数
  - 動作周波数が高ければ高いほど処理が速くなるが、電力効率が悪くなり、発熱も増える
- キャッシュ
  - CPUとメインメモリの間にキャッシュメモリという高速なメモリを用意し、ここに頻繁にアクセスするデータを置くことで、低速なメインメモリへのアクセスを減らしてCPUの性能をあげる
- ハイパースレッディング
  - 一つのコアで二つの処理を実行できる技術
- ターボブーストテクノロジー
  - CPUを自動的に定格の動作周波数より高速で動作させる機能
#### CPU選定のポイント
- パフォーマンス
- 価格対比
  - CPUによって価格差が大きいから
- 使うソフトウェアのライセンス体系
- 消費電力

### メモリ
- 短期記憶領域、電源が停止すると全てのデータが消える
#### パフォーマンス
- DDR3-1600
  - 「3」は世代を表す数字
  - 「1600」は大きければ大きいほど読み書きの速度が速い
  - 1600MHz*8Byte=12.8GB/秒 がデータ転送速度という意味
#### DDR3メモリの種類
- P41の画像
#### メモリ用語
- スロット数
  - マザーボードに挿せるメモリの数
- ECC memory
  - ビット反転エラーが発生した時に自動補正・検知できるように、誤り訂正符号(ECC)と呼ばれるパリティ情報が追加されているメモリ
- チャネル
  - CPUとマザーボードが複数チャネルに対応している場合、チャネルごとに同一種類のメモリを搭載することでデータ幅を増やし、パフォーマンスを向上させることができる
  - P42の画像
- ランク
  - メモリコントローラがメモリ上のDRAMからデータを入出力する単位のこと
  - シングルランク(1R)、デュアルランク(2R)、クアッドランク(4R)がある
  - メモリコントローラが扱えるランク数は決まっているため、スロット数が余っていても使えなくなる場合があるので注意
  - P43の画像
- UDIMM
- RDIMM
- LRDIMM
- LV(低電力)
#### メモリ表記の見方
- P44
#### メモリの挿し方
#### メモリ選定

### ディスク
#### ディスクの種類
- SATAハードディスク
- SASハードディスク
- FCハードディスク
- ニアラインハードディスク
- SSD
- エンタープライズフラッシュメモリストレージ

### RAID
#### RAIDレベル
- P50画像
#### RAIDのパフォーマンス
- RAIDを用いるとディスクI/O性能を向上させることができる
  - I/O性能とは、サーバとストレージ間の間でやりとりされるデータの読み書き性能のこと
- ストライピング本数とは
  - 複数のディスクを並列に用いる場合の本数のことをストライピング本数という

#### RAID5 vs RAID10
- 大量のディスクが必要な場合にこの二つがよく検討される
- RAID5
  - 実容量を多く取れる半面、パフォーマンスが遅い
- RAID10
  - 実容量が少なくなる半面、パフォーマンスが速い
#### RAID5 vs RAID6
- P52,53参照

### 仮想化
#### 物理サーバと仮想サーバの特性
- 物理サーバ
  - CPU使用率、ディスクI/O負荷、もしくはディスク使用量が大きい用途に向く
  - 主な用途は、データベースサーバ、アプリケーションサーバなど
- 仮想サーバ
  - CPU使用率、ディスクI/O負荷、および、ディスク使用量が小さい用途に向く
  - 仮想サーバの主な用途は、Webサーバ、開発サーバ、メモリDBなど

#### 物理サーバを仮想化する場合のメリットとデメリット
- メリット
  - コストダウンが可能
  - ゲストOSのハードウェアリソース増減を容易に行える
  - 物理サーバの場合、ハードウェアが老朽化するので一定期間が経過した後でハードウェア交換が必要なのに対して、ゲストOSは他の新しい物理サーバに仮想化環境を用意し、そちらに簡単に移行ができる
- デメリット
  - 他のゲストOSがリソースを大量に使うと、他のゲストOSが不安定になる
  - 一度作られたゲストOSがその後使われなくなっても残りがち


### クラウド
#### SaaS、PaaS、IaaSの違い
- P61の画像
#### クラウド vs 自社でのサーバ運用
- クラウドは仮想化技術を使って提供しているため、通常だと使われないような大量のリソースのスケールアップには向かない
- クラウドの物理サーバが故障したら、クラウドベンダーの障害対応を待つしかない
- クラウドベンダーの手違いで重要なデータが消失するケースがある
#### クラウドに向かない用途
- 機密情報を置くこと
- 大容量ファイルの転送
  - クラウドはインターネットを流れてファイルの転送を行うから、社内サーバに比べて遅い
- 大規模システム
  - ある程度大規模になったら自社で持ったほうが安くなる

<br></br>

## OS
### Linux

### Windows Server

### Unix

<br></br>

## ネットワーク
### ルータを選ぶポイント
- ISPやデータセンターなど、ルータを接続する先から提供される上位回線のインタフェースと一致したWAN側インタフェースを持つこと
- WAN側での通信帯域
- スループット
- セキュリティ機能をルータにも求めるか
- 導入コスト

### L2/L3スイッチの役割
#### L2スイッチ
- L2スイッチにフレームが入ってくる
- L2スイッチは宛先となるMACアドレスを見て適切なポートにフレームを転送する
- L2スイッチのARPテーブルに該当するMACアドレスが存在しない場合はLAN内全体にブロードキャストを飛ばし、応答があったポートに転送します
#### L3スイッチ
- L3スイッチにパケットが入ってくる
- L3スイッチは適切なポートにパケットを転送
- ルーティングテーブルに該当するIPアドレス、もしくはネットワークアドレスが該当しない場合は、デフォルトゲートウェイに転送する
#### L4スイッチ(ロードバランサー)
- 宛先となるVIPとTCP/UDPポートを見て適切なサーバにパケットを転送する
- ポート番号を基準に負荷分散する感じか
  - 「80と443のサーバ」、「22のサーバ」の二種類に負荷分散するとか
#### L7スイッチ(ロードバランサー)
- 宛先となるURLを見て適切なサーバに転送する

### ネットワークのトポロジー
#### フロントエンド/バックエンド2階層構造
- フロントエンド層
  - インターネットから近いところに配置される
  - AWSでいうパブリックサブネット付近に設置される
- バックエンド層
  - インターネットから遠いところに配置される
  - DBとか配置する
  - AWSでいうプライベートサブネット付近に設置される
- P88の画像
#### 3階層構造
- コア層
- ディストリビューション層
- アクセス層
- P89の画像

<br></br>

## ストレージ
P102-113の画像をまとめる
### ローカルストレージ
- サーバ内にディスクを搭載して用いる記憶領域
- 外部ストレージを使わない分、設置場所がコンパクト
- ディスクの本数や拡張性が少ない
### 外部ストレージ
- サーバ外に設置するストレージ領域
#### DAS
- サーバに直結するストレージ機器
- ストライピング数の多いRAID構成にすることでディスクI/O性能を大幅に高めることができる
#### NAS
- ネットワーク経由で複数のサーバからアクセス可能なストレージ
- サーバとNAS間は、NFS、SMB/CIFS、もしくはAFPといったプロトコルで通信を行う
- 複数のサーバ間でデータを共有する場合や、複数のサーバで発生するバックアップやログファイルを一箇所にまとめる用途に使われる
#### SAN
- FC-SAN
- IP-SAN
### 外部ストレージの利用用途
#### 記憶領域を大きく取りたい
- ローカルストレージでは不十分な場合
#### ディスクI/O性能の向上
- ローカルストレージのI/O性能が不十分な場合
#### ストレージ統合・集中管理
- サーバごとにデータが分散しているとストレージの管理が難しい
- サーバごとにストレージが分散していると、余っている部分のストレージがもったいないから統合したい場合
#### 複数サーバ間でのデータ共有
- いずれのサーバからも同一のデータやソースコードを読み書きしたい場合
### ストレージの高度な機能
#### シンプロビジョニング
#### 自動階層化
#### デデュープ
#### スナップショット

<br></br>

## インフラ運用
### ボトルネックを解消する
- トラブルシューティングする時に使うコマンドまとめ(よくまとまっていると思う)
  - https://qiita.com/hana_shin/items/25f7d0c53bbf55d0f963
#### よくボトルネックが起こる部分
- コアスイッチのキャパシティ
- L2スイッチのキャパシティ
- Webサーバのキャパシティ
- データベースサーバのCPUやメモリ不足
- データベースサーバのディスクI/O
#### ネットワーク機器のボトルネック解消
- 各ポートの物理インタフェースの速度にトラフィックが収まっているか
  - 調べ方
    - 1Gbpsのインタフェースであれば、実際のIN/OUTトラフィックがそれぞれ1Gbps未満に収まっているか
  - 対策
    - サーバを分散してトラフィック分散するか、インタフェースをより高速なものに置き換える
- ネットワーク機器の転送能力に限界はないか
  - 調べ方
    - パケットドロップが発生していないか。転送能力不足を示すようなログが残っていないか
  - 対策
    - ネットワーク機器を上位機種に入れ替えや、キャッシュメモリ追加などが可能であれば実施する
#### サーバ機器のボトルネック解消
- フロントエンドのレスポンスが低下していないか
  - 調べ方
    - 書くサーバのレスポンスタイムを定期的に取得し、極端な低下がないか。もしくはユーザサポートにレスポンス関連の問い合わせがないか。
  - 対策
    - まずは、フロントエンドサーバの問題か、データベースなどのバックエンドサーバの問題かを特定する
    - バックエンドサーバでは、CPU、メモリ、ネットワーク、ディスクI/Oのリアルタイム利用状況をみて、異常に使われていればバックエンドサーバの問題を疑う
    - 同じくフロントエンドサーバでも同じ部分のリアルタイム利用状況を見て判断する
    - 次に、ハードウェアのリソースが足りないのか、アプリケーションの問題なのか、ハードウェアの故障かを調べる

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
