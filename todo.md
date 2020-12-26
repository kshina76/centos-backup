# todo

## 残り97日(12/24更新)

# to do
- コードリーディングを読み、実践をする
  - vscodeにはdebugpyというプラグインが最近出たらしい
  - fastapiのデバッグはuvicornをコード内で走らせてからvscodeのデバッグツールを動かすらしい
    - https://fastapi.tiangolo.com/tutorial/debugging/
- 知らないセキュリティ関連の知識
  - https://speakerdeck.com/kurochan/ca20xin-zu-yan-xiu-sekiyuriteibian?slide=44
- フレームワークの勉強をするときに、それぞれのトピックを頭に入れておくと、やるべきことがわかる気がする(dockerで報告書のテンプレを作っておくと後々楽かもしれない)
  - フレームワークで実現されているかのチェック項目のテンプレートを作って、新たに学ぶ時はそのテンプレートにサンプルを埋めるようにして、開発中のリファレンスに使うと便利かもしれない。上司に技術選定の資料を送るときにも、このテンプレートは有用になると思うので用意しておくといい。目次をつけて気になるところにすぐ飛べるようにするのも便利だし、喜ばれそう
    - セッション管理はどのように書くのか
    - POST, GETされたデータのバリデーションはどうするのか
    - ディレクトリ分割
    - DBのマイグレーションはどうするのか
      - マイグレーションの機能としては、初期のテーブルを定義したり、テーブルの定義が変更になった時もマーグレーションを行えば、テーブル定義のバージョン管理もできるようになる
      - Djangoでは組み込まれているが、FastAPIではAldemicというライブラリをインストールすることになっている
    - DB操作はどうするのか
      - ORMを使う場合はどうするのか、クエリビルダを使う場合にはどうするのか
      - コネクションの管理はどうするのか
      - トランザクションの管理はどうするのか
    - etc
    - https://qiita.com/tmknom/items/08b69594e32a92bccee5
- webapiの開発フローをまとめる
  - 技術選定
    - 選定理由をテンプレートを使って埋める
    - https://github.com/kshina76/centos-backup/blob/master/web_application/framework選定/tmp.md
  - 設計
    - DB設計
    - エンドポイント設計(URL設計)
      1. 対象となるデータを認識する
      2. 対象となるデータをリソースに分ける
      3. リソースにURLで名前を付ける
      4. URLに対してPOST,GET,PUT,DELETEを付ける
    - ディレクトリ設計と依存設計
      - 依存設計は、ディレクトリ同士がどのような依存関係になっているかを図示する(クラス設計みたいなもの)
        - 自分がバカだからこれがないと混乱する
      - https://note.com/yusugomori/n/n9f2c0422dfcd
      - https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
    - ルーティング設計
      - 大きいアプリケーションになった時にエンドポイントを階層化して分けることで、分割できるようにするもの
      - URI毎にディレクトリを分けて階層化することでルーティングを管理する感じかな
        - articlesのURIならarticlesディレクトリに
        - usersのURIならusersディレクトリに
      - https://qiita.com/tmknom/items/08b69594e32a92bccee5#ルーティング定義とエンドポイント設計
      - https://fastapi.tiangolo.com/tutorial/bigger-applications/
    - リクエスト設計: ユーザからの入力に対しての設計
      - クエリパラメータ、リクエストボディ、パスパラメータの設計と使い分け
        - https://github.com/kshina76/centos-backup/tree/master/web_application/web_api#2-5検索とクエリパラメータの設計
        - https://github.com/kshina76/centos-backup/tree/master/web_application/web_api#2-6-フィルタソート検索はリクエストパラメータでやろう
        - https://github.com/kshina76/centos-backup/tree/master/web_application/web_api#2-7-レスポンスのフィールドを絞れるようにしよう
      - HTTPヘッダの設計
    - レスポンス設計
      - レスポンスボディの設計
      - ステータスコード設計
      - HTTPヘッダの設計
    - 正常系の設計
    - 異常系の設計(例外設計)
      - https://qiita.com/tmknom/items/08b69594e32a92bccee5#例外ハンドリング
      - https://nekogata.hatenablog.com/entry/2015/04/11/135231
    - ロギング設計
      - https://qiita.com/tmknom/items/08b69594e32a92bccee5#例外ハンドリング
  - 開発
    - Docker環境構築
      - DBコンテナのセットアップ
      - APIコンテナのセットアップ
    - モデルの実装
      - DBのコネクションのコード実装
      - ORMのモデルを定義
        - リレーションの設定はどのように行うのか(many to manyの実現方法は)
    - マイグレーションの設定
      - FastAPIの場合は、`alembic`というライブラリを使ってマイグレーションを行う
      - その他は`SQLAlchemy-Migrate`というライブラリもある
    - シードの設定
      - シードとはデータベースにあらかじめ入れておくデータのこと
      - ブログならadminを設定しておくのがいいと思う
      - djangoのadminページを作るような感じかな
    - APIの実装
    - https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
  - 全体の参考文献
    - https://www.slideshare.net/t_wada/restful-web-design-review
## 入社後の日課
- 入社後の日課
  - 自己嫌悪に陥らないようにマインドを保つ方法
    - https://engineer.dena.com/posts/2020.07/20-new-graduates-training-retrospective-5/
  - 英語(TOEFL)
  - atcoder, leetcode, kaggle
  - システム設計をよく読んで、アーキテクトの知見を取り入れる
    - https://github.com/donnemartin/system-design-primer/blob/master/README-ja.md
  - ソースコードリーディング
    - https://developers.freee.co.jp/entry/how-to-read-source-code-of-middleware
  - 日本語と英語で書評ブログ(読書感想ブログ)を運営してみる
    - newtonとか読むのがいいかも
  - エンジニアの情報収集
    - https://qiita.com/nesheep5/items/e7196ba496e59bb2aa28
  - Udemy
    - 酒井さんのPythonの講座
    - 酒井さんのデータ構造とアルゴリズムとコードテスト対策のやつ
    - vigneshのOSの講座
  - 定期購読
    - WEB+DB PRESS
      - webアプリケーションエンジニアに一番近い情報を連載しているかも
      - これ読んでみたい
    - Software Design
      - 同じくwebアプリケーションエンジニアに一番近い情報を連載しているかも
      - これ読んでみたい
    - 日経Network
      - これ読んでみたい
    - 日経ソフトウェア
    - 日経Linux
    - Newton
      - 知的好奇心を満たす
    - 参考文献
      - https://qiita.com/kusokamayarou/items/ff7e835b80e52957113f

## エンジニアとしてやるべきこと 
- 仕事を任せられるエンジニアとは
  - https://tech.tabechoku.com/entry/2019/05/02/182457
- エンジニアのスタートダッシュ、習慣など
  - https://qiita.com/suy0n9/items/d1bfbd823d8b6dc562be
- 読むべき本
  - https://qiita.com/tmknom/items/67dbfcf5194aee5c6e61
  - https://qiita.com/JunyaShibato/items/3aa5f7f3fc991de17f3f
- 入社1,2年目で意識すること
  - https://qiita.com/rf_p/items/34f92d4e9d4398f2f969
  - https://qiita.com/cocoa_dahlia/items/2e6b25e166058936eceb
  - https://qiita.com/musclemikiya/items/8d7befa6f7fade842a2a
  - https://qiita.com/shunsuke227ono/items/36723b9c19c25d545aa1
  - https://qiita.com/soyanchu/items/d1cb9785fc211941a009
  - https://qiita.com/enta0701/items/a6faabbecd6786642d76
  - https://qiita.com/hand12/items/89f62ad51a51f596d259
- 50代以降のキャリアに備える
  - https://qiita.com/poly_soft/items/dbca28f166d07070e8eb

## エンジニア情報収集まとめ
- https://qiita.com/nesheep5/items/e7196ba496e59bb2aa28

## 次に気になっている本(https://qiita.com/JunyaShibato/items/3aa5f7f3fc991de17f3f)
- プログラミング関連
  - Webアプリケーション設計・実装のためのフレームワーク活用の技術
  - レガシーコード改善ガイド (Object Oriented SELECTION)
- インフラ関連
  - Webエンジニアが知っておきたいインフラの基本
- ネットワーク関連
  - ネットワーク仮想化～基礎からすっきりわかる入門書～
  - 3分間NetWorking　＊書籍ではなくWebサイトです。 
    - http://www5e.biglobe.ne.jp/%257eaji/3min/
- Linux関連
  - https://linuc.org/textbooks/security/
  - 試して理解Linuxのしくみ ~実験と図解で学ぶOSとハードウェアの基礎知識
- AWS
  - Amazon Web Services パターン別構築・運用ガイド 改訂第2版
  - Amazon Web Services 業務システム設計・移行ガイド (Informatics&IDEA)
- データ分析
  - データ解析の実務プロセス入門
    - データ分析の手法を実際に実務で使うにはどうすればいいのかといったところの説明
    - データ分析を実務で使う上での全体像などの最初の一歩に良い
- 仕事関連
  - ロジカル・シンキング (Best solution) 
  - 報・連・相の技術がみるみる上達する!


## 直近todo
- キーボード操作を効率化(vim形式でできるのかな？？)
  - 移動キーの割り当て
  - 定義を表示
  - 定義に飛ぶ
  - 画面分割
  - 一気に行の後ろまで飛んだり、一行を全削除したり
  - ファイラ関連
    - コマンドでファイルを新たに作成したり、簡単に削除できたり
  - 置換とか、正規表現で検索したり
- 入社前の最低限の勉強
  - git
    - SourceTreeなどのクライアントツールについても
    - 日頃の開発からgitでブランチ切って、マージをするなどしたほうがいいかも
  - HTTPなどのIT知識
    - 暇な時に色々本を読んでおくといいかな
  - Linux
  - SQL
    - ミックの書籍を3冊読む
    - できるならばアンチパターンも
    - クライアントツール
  - NoSQL
    - DynamoDBを使っていたから
  - Docker
  - markdownでの文書作成
  - AWSで簡単にネットワークを組んで、サブネット分割して環境を整える練習とかLambdaとかの本とか
    1. 図解即戦力　Amazon Web Services
      - 借りた
    2. Amazon Web Servicesインフラサービス活用大全
      - 借りた
    3. Amazon Web Services 基礎からのネットワーク＆サーバー構築　改訂3版 
      - kindleにある
    4. 基礎から学ぶサーバレス設計開発
      - 借りた
    5. Amazon Web Serviceネットワーク入門
      - kindleにある
      - もう一回読む
    6. 実践terraform
      - kindleにある
- ソニーはマイクロサービスを構築しているらしい
  - https://aws.amazon.com/jp/solutions/case-studies/sony/
- 色々な技術のチートシートがまとめられている
  - https://wikiwiki.jp/bankura/IT系/チートシート・コマンド集
- 以下のことについてまとめる
  - ISUCONのREADEMEに表示に関する最適化手法をまとめる
    - https://qiita.com/zaru/items/51ee8a5be22b75a42927
    - https://capitalp.jp/2016/12/29/http2/
    - https://qiita.com/saboyutaka/items/1f528ec3ce85476d7561
    - https://note.com/airis0/m/m7c39abf9072a
    - webapiの最適化を探して学ぶ
  - どこかに基礎知識(かなり重要)をまとめたREADMEを作って、以下の内容をまとめる(勉強の仕方なども同じとこにまとめていいかも)
    - https://qiita.com/yamadar/items/bfdfc58cec49bf2690e1
    - devops,バックエンドのロードマップをまとめる
      - https://qiita.com/poly_soft/items/fb649573c19b7a5c0227
      - https://qiita.com/poly_soft/items/8dd105341869f93b129c
  - LINE式コードの可読性をまとめる
    - https://engineering.linecorp.com/ja/blog/tag/codereadability/
  - linux系のこと
    - Linuxパフォーマンス調査などで使うコマンドメモ
      - https://qiita.com/toshihirock/items/0e0b20064730469e93e6
    - いまさら聞けないLinuxとメモリの基礎＆vmstatの詳しい使い方
      - https://qiita.com/kunihirotanaka/items/70d43d48757aea79de2d
  - ガチ勢のwebアプリケーションチューニング
    - https://www.prime-strategy.co.jp/resource/pdf/DevelopersSummit2020.pdf
  - dockerの全体像の解説(networkなども込みでかなり詳しい)をまとめる
    - https://qiita.com/etaroid/items/b1024c7d200a75b992fc
    - https://qiita.com/etaroid/items/88ec3a0e2d80d7cdf87a
    - https://qiita.com/etaroid/items/40106f13d47bfcbc2572
  - FastAPIでアプリケーションを作っている(結構ちゃんとしているもの)
    - https://shinyorke.hatenablog.com/entry/fastapi
- WebAPIをOOPで開発するってことはあるのか？
  - flask_restfulとかflask_classみたいなライブラリはあった
  - プレゼンテーション層がHTMLではなくてJSONに変わっても同じ。というような記事を見たことがあった気がするから開発することはあるのかなと思った

- 題目・概要の確認(sgsotは1/8まで、教員は1/9)
- SEATUC(1/15に合格かどうかがくる)
- 本論(1/29~2/6)
- Web API Good Parts(12/19,20で)
- 認証・認可周りの本を読む(OAuth、OpenID Connect、AWS Cognite)
  - https://booth.pm/ja/items/1550861
  - https://booth.pm/ja/items/1296585
  - https://booth.pm/ja/items/1560273
- golangまたはPythonでwebに関連するもの全てをフルスクラッチで書いてみる(real world httpを参考に)
  - HTTP/1.1、HTTP/2、HTML5、ロードバランサー
- ハイパフォーマンスpythonを以下をベースにまとめる
  - 2015年の本なので、古い書き方に注意。調べながら
  - https://showa-yojyo.github.io/notebook/gorelick14.html
- 「新しいpythonの書き方」と「ハイパフォーマンスpython」と「AWS Lambda」と「chromeのdevtool」を使ってwebapi開発(12/21から始めたい)
- LINE式コードの可読性をまとめる
  - https://engineering.linecorp.com/ja/blog/tag/codereadability/
- Lambdaの書籍とデザインパターンをまとめる
- READMEの統合
  - 社会人としてやっていく際のノウハウなどもまとめたい
  - 新しい技術を学ぶ際の情報収集のやり方など(下の方にまとめているからあとでどっかに移行する)
    - 日課でまとめる練習をするために、Qiitaにアップするといいかも(aws developers blogの最新記事とか)
      - 他のエンジニアブログを色々見て、紹介する際のテンプレートを作成しておくといいかも(READMEにmarkdownでまとめておいて、すぐに引き出せるように)
      - 自分の思考順にまとめるといい文章になるかも
      - どのような題材に取り組んだか->パフォーマンス計測->どこに問題があったか->どのような方針で行くことに決めたか->方法の詳細->結果
      - https://note.com/licodeenar/n/n0e87fb648342
- モチベーションにプラスになる動画
  - https://www.youtube.com/watch?v=RO3gGJokzdg
- vscodeショートカット
  - 移動系
  - 実行
- tmux
  - https://qiita.com/nl0_blu/items/9d207a70ccc8467f7bab

## 入社前todo
- AWSを使いながらWebアプリケーションのAPI開発
  - フロントエンドはとりあえず後回し
  - 少なくともLambdaのパターンは色々やっておく
  - トラブルシューティングは手当たり次第ではなく、体系的な方法で行うようにする。
  - アプリケーションの最適化を行う(ISUCONの手法を洗練させていく)
  - ユニットテスト書けるように
  - ついでにライブラリやフレームワークの知識を付けていく
- DB関連の勉強
  - SQLの書き方
  - RDBMSのCRUDなど
  - NoSQLのCRUDなど
  - Redis
- ミドルウェアの知識
  - RDBMS、Nginxなどの設定知識
  - 負荷試験
  - 監視　入門
  - 監視ツール
- セキュアプログラミングの知識
  - 徳丸本
- git
- Linuxコマンドのまとめ(開発に集中できない時に都度行う)
- その他気になる部分の書籍

## 日課
- 昼寝
  - 午後1時〜午後3時の間で30分
- 一週間ごとのルーティーンを意識する
  - 毎日同じルーティーンで行うと生産性は下がる
  - 月曜日は軽い仕事
    - 事務作業とか
    - 
  - 火曜、水曜
    - 多くの人が仕事モード
    - 一番厳しい仕事を入れる
  - 木曜
    - 午後からエネルギーが後退し始める
    - 夜は仕事を詰めすぎない
    - ミーティング、会食多め
  - 金曜
    - かなり疲れている状態
    - 重い仕事は入れない
  - 土日
    - 仕事を忘れてエネルギーをチャージする
    - 本を読むとかでもいいかも
- マルチタスクをやめる
  - 人間の脳はマルチタスクができないようになっている
  - todoリストを作って、一つずつやっていく
  - スマホが気になってしまうこともマルチタスクを行っているからやめる
  - どうしても集中できないならレンタルルームに必要なものだけを持って行って作業する
- バカがバレる質問
  1. 目的がない質問
    - それ聞いてどうなるの？ってなる質問
    - 「〜〜を明らかにする質問なのですが」という前置きをするとか
  2. ザックリしすぎている
    - 仮想通貨ってどうですか？だったり
    - 不動産投資ってどうですか？のような質問
  3. 前置きが長い
    - 質問をする前に近況報告が始まったり
    - 自分の聞きたいことを整理してから質問をする
  4. 聞く相手を間違えている
    - 誰に聞いても同じ答えが返ってくる質問はするべきではない
    - 相手を活用するような質問をする
  5. ググればわかる質問

## 新しい技術を学んでいく方法
- https://aws.amazon.com/jp/blogs/developer/

## 研修課題
- いろいろな企業のテックブログで紹介しているだろうから調べる
- インフラの負荷を削減できるとコストを減らせるという目標を立てても面白いかも
  - https://www.slideshare.net/kazeburo/isucon-yapcasia-tokyo-2015
- DeNAで行われた研修
  - CS基礎（加算器 → レジスタ → CPU → アセンブリ → C）
  - Go
  - Flutter
  - AWS
  - システムデザイン
  - チーム開発(インフラ、サーバ、クライアントの設計から実装までを行う)
  - テックトーク(各々が技術トピックについて調べて発表をする)
  - https://engineer.dena.com/posts/2020.07/20-new-graduates-training-retrospective/
- BFF(Backend for Frontend)
  - https://kamihikouki.hatenablog.com/entry/2018/07/20/134307
  - https://engineer.dena.com/posts/2020.07/20-new-graduates-techtalk/
- ウェブ会議システムをAWSで作ってみる(動画が無理なら音声だけでも)
  - コロナネタとクラウドサービスを組み合わせると面白そう
  - webRTCという技術が必要らしい
  - https://engineer.dena.com/posts/2020.07/20-new-graduates-techtalk/
- 会社のサービスをDDoS攻撃からまもる
  - ファイアーウォールで弾く(WAF)
  - ブラックホールルーティング
  - AWS CloudFrontを使う方法
  - https://speakerdeck.com/kurochan/ca20xin-zu-yan-xiu-sekiyuriteibian?slide=28
  - https://engineer.dena.com/posts/2020.07/20-new-graduates-techtalk/
- 従来のWebアプリ開発をさらに効率よく進める方法
  - フロントエンドが主体で開発を進められる
  - https://engineer.dena.com/posts/2020.07/20-new-graduates-techtalk/
- AWSアカウント作成自動化
  - https://engineer.dena.com/posts/2020.03/improved-public-cloud-accounts-creation/
- マイクロサービスの次に来るもの
  - https://www.infoq.com/jp/news/2020/04/multi-runtime-microservices/
- HTTP3の凄さ
  - https://www.urban-project.jp/blog/recommended/1551/
  - https://http3-explained.haxx.se/ja/why-quic
- Slackをつかったサーバレスのマイクロサービス監視アプリケーション
  - https://www.cview.co.jp/cvcblog/2020.08.20.QmzQcRnZpnnmd-Dnx-fIo
- AWS資格3冠達成
  - https://dev.classmethod.jp/articles/new-grads-ojt-korean/

## 競プロ
- ライブラリを駆使するのではなくて、まず自分で考察を進めて解くことを意識する
- ライブラリは理解したものしか使わない

## ISUCON
- Webアプリケーションのチューニング大会
- コンピュータの色々な知識が必要になるから勉強になる
- 「入門　監視」を読む
  - https://a-mochan.hatenablog.com/entry/2020/01/19/223030
  - https://qiita.com/tsurumiii/items/27f22b38215e37518c7c
- 監視ツールを学ぶ
  - netdataとか
  - https://blog.adachin.me/archives/3446
- 色々な監視ツールをdockerにまとめて作っておくといいかも
- ISUCONチートシートをまとめる
  - https://gist.github.com/south37/d4a5a8158f49e067237c17d13ecab12a
- 学習ロードマップにあるlinuxのコマンドを学習する(nmapとか色々あった)
- 以下の動画を見てまとめる
  - https://www.youtube.com/watch?v=vl1mYTq1ZYI&t=1604s
  - https://www.slideshare.net/kazeburo/isucon-yapcasia-tokyo-2015
- 各プログラミング言語のプロファイリングツールをまとめる
- goで学ぶISUCONの書籍をまとめる
- ISUCONで有効だった方法を学ぶ(調べれば出る)
- AWS Lambdaのパフォーマンスチューニング手法

## 書籍
- JavaScriptの本全般
  - 4種類くらい予約したからつまみ学習していく
- pospomeさんのアーキテクチャを読んでまとめる
- AWS Lambdaを読む
- フロントエンドパフォーマンスチューニング
  - https://www.amazon.co.jp/dp/B0728K5JZV/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1
- 超速！ Webページ速度改善ガイド
- HTMLコーダー＆ウェブ担当者のための Webページ高速化超入門

## サイト
- システム設計を学ぶ
  - https://github.com/donnemartin/system-design-primer/blob/master/README-ja.md
- エンジニアの勉強法
  - https://ne-tabase.com/freelance/704
- バックエンドエンジニアに必要な知識
  - https://blog.innotamago.com/entry/2018/01/12/150347

## 個人開発
- vanill-jsでDOM操作とajaxを学びつつ、バックエンドのAPIを拡張機能として開発する(flaskとかでwebAPIを作る)
  - https://vanillawebprojects.com
  - https://github.com/bradtraversy/vanillawebprojects
  - https://qiita.com/katsunory/items/9bf9ee49ee5c08bf2b3d

- FlaskでTechBlog開発

## 今後やらないといけないこと
- 英語
