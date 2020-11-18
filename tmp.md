# 重要な事柄をかき集めてきたもの

## 絶対読む書籍
- git
    - GitHub実践入門 ~Pull Requestによる開発の変革

- vim
    1. vimをインストールしたら、「vimtutor」というコマンドを打ってチュートリアルをやってみる
    2. 「実践vim」という書籍でtipsを学ぶ。画面分割とかいきなりやると、「こいつできるんじゃね？」ってなる

- リーダブルコード

- オブジェクト指向
    1. オブジェクト指向でなぜ作るのか
    2. Java言語で学ぶデザインパターン入門

- データベース
    1. 達人に学ぶSQL徹底指南書
    2. 達人に学ぶDB設計徹底指南書
    3. 基礎からのMySQL    
    4. SQLアンチパターン

- HTML/CSS
    1. HTML&CSSとWebデザイン
    2. CSS設計完全ガイド　～詳細解説＋実践的モジュール集

- プログラミング言語
    - python
    - javascript/typescript

- web技術、web開発の基本を網羅
    1. Web技術の基本
    2. プロになるためのWeb技術入門
    3. Webを支える技術
    4. 体系的に学ぶ 安全なWebアプリケーションの作り方 第2版 脆弱性が生まれる原理と対策()

- AWS
    1. Amazon Web Services 基礎からのネットワーク&サーバー構築
    2. 実践terraform
    3. IAMの基本、設計
        - https://booth.pm/ja/items/1563844

- 文字コード
    - プログラマのための文字コード技術入門

- テスト

- Docker/Kubernetes
    1. Docker/Kubernetes 超入門
    2. Docker実践ガイド 第2版 impress top gearシリーズ
    3. Kubernetes完全ガイド 第2版 impress top gearシリーズ

- IDE
    - vscode
    - IntelliJ

---

## 有用な記事、動画
### HTML/CSS
- CSSの効率的な書き方、tabUIの開発、便利なショートカットキー
    - https://www.youtube.com/watch?v=OSQ1LnU9SCw
- Googleが推奨するHTML/CSSのコーディング規則
    - http://detarame.moo.jp/2012/08/07/googleが推薦するhtmlとcssのコーディング方法/
- CSSのpx, em, rem, %, vw単位の違いと使い分け
    - https://note.com/takamoso/n/nde1275183086

- BEMとは
    - https://pikawaka.com/html-css/bem#BEMと親和性の高いSassを使用する
- SCSS/SASSの使い方
    - https://pikawaka.com/html-css/sass
- SASSを用いてBEMでCSSを設計
    - https://qiita.com/Takuan_Oishii/items/0f0d2c5dc33a9b2d9cb1

- HTMLからCSSセレクタを自動生成
    - https://css.miugle.info
- HTMLを省略記法で記述するツール
    - Emmet

### Python
- Pythonにおいての参照渡しはCの参照渡しとは違う
    - https://qiita.com/ponnhide/items/cda0f3f7ac88262eb31e

### golang
- オブジェクト指向をgolangで行うとき対応表
    - https://stackoverflow.com/questions/37510763/static-member-variable-such-as-oop-langage
- go言語におけるエラーハンドリング
    - https://qiita.com/nayuneko/items/3c0b3c0de9e8b27c9548
    - https://waman.hatenablog.com/entry/2017/09/29/011614

---

## WebAPIを勉強する手順
1. 基礎知識
    - https://qiita.com/NagaokaKenichi/items/df4c8455ab527aeacf02
    - https://www.slideshare.net/tmasao/web-api-49080729
2. WebAPIの活用を学ぶ(作りたいものが浮かぶかも)
    - http://www.soumu.go.jp/ict_skill/pdf/ict_skill_1_5.pdf
    - https://paiza.hatenablog.com/entry/2016/06/21/面倒な手続き不要！「Web_API」の超お手軽活用術をJavaScript
3. WebAPIを実装する
    - https://github.com/yosriady/api-development-tools
4. あとは以下の通り
    - https://kirohi.com/web_api_resources

- 自分のREADMEに色々書いてある
    - https://github.com/kshina76/centos-backup/tree/master/web_api
---

## ドメイン駆動設計を勉強する手順
1. まず基礎知識を頭に入れる
    - https://www.slideshare.net/TakuyaKitamura1/ddd-29003356
    - https://logmi.jp/tech/articles/310424

2. 体系的に学習する
    - https://nrslib.com/bottomup-ddd/
    - https://nrslib.com/bottomup-ddd-2/
    - ドメイン駆動設計入門 ボトムアップでわかる! ドメイン駆動設計の基本
        - 上の２つの記事を書籍化したもの

3. 実践的な書籍を読む
    - ドメイン駆動設計 モデリング/実装ガイド
        - https://little-hands.booth.pm/items/1835632

4. ドメインモデルとユースケースに絞った書籍を読む
    - モデルベース要件定義テクニック(RDRA)
    - ユースケース駆動開発実践ガイド(ICONIX)

5. とりあえず簡単なプログラムを作ってみる
    - https://qiita.com/APPLE4869/items/d210ddc2cb1bfeea9338
    - https://qiita.com/hirotakan/items/698c1f5773a3cca6193e

6. 最後の仕上げに難しめな本を読む
    - エリック・エヴァンスのドメイン駆動設計
    - 実践ドメイン駆動設計

---

## Webアプリ個人開発の手順

### 前準備
1. 技術選定
    - LGTMがいっぱいついていた記事があった気がする

### 設計
1. ユースケース図(箇条書きでも可)
    - 「誰が何をするか」ということを明確にして書いていく
2. シーケンス図
    - ユースケース図で書いたそれぞれの機能にフォーカスする作業
    - 一つ一つの機能の流れをシーケンス図を使って書いていく
    - もっと細かくフローチャートのようにしたかったらアクティビティ図も書いてもいいかもしれないけど、シーケンス図で大枠を掴めればいい気がする
3. 画面遷移設計、デザイン
    - 「figma」というUI/UXツールでページのデザインを作成
    - Frameを意識することで、HTMLタグの付け方が頭に浮かんできて、後々のコーディング作業で楽になるという付加効果もある
    - 一つのページにFrameを分割して矢印を書けば、画面遷移図になる
    - 画面遷移設計は漏れが無いようにするためにユースケース図を参考にしながら進める
4. URL設計
    - 画面遷移設計やユースケース図を参考にしながらURLを考えていく
5. DB設計
    - ER図
    - 本でしっかり学ぶ
6. アーキテクチャ設計、クラス設計
    - アーキテクチャ設計
        - 全体のレイヤー構成は、3層、4層、クリーンアーキテクチャなどから選択する
        - プレゼンテーション層は、MVC、MVP、MVVMから選択する
    - クラス設計
        1. ユースケース図とシーケンス図を参考にしてイベントフローやシナリオを文章で書き出す
        2. 固有名詞とかを抜き出してクラスにする
        - 詳しくは以下のREADME
            - https://github.com/kshina76/centos-backup/tree/master/OOP/oop_design
7. システム構成設計
    - インフラとか

### 開発
1. 開発環境構築
    - DockerとDocker-Composeで作成する
        1. オンプレミスでインストールするときの手順を調べて必要なコマンドを抜き出す
            - マルチステージビルドを駆使すればいらないかも
            - パッケージをインストールする際などは必要
        2. 公式イメージと使い方をドキュメントでみる
        3. Dockerで構築してみる
        4. Docker-Composeで構築する
2. コーディング
    1. HTMLを全てコーディングする(HTML設計)
        - タグ付けはBEMという設計方法に従う(後々のCSSデザインに関わる)
            - https://qiita.com/pugiemonn/items/964203782e1fcb3d02c3
            - https://qiita.com/Takuan_Oishii/items/0f0d2c5dc33a9b2d9cb1#blockにはmarginを指定しない
            - 具体的に付ける場所はデザインを作った時のFrameを参考にすると良い
    2. CSSでデザインをする
        - まず以下のURLのreset.cssを読み込む
            - http://html5doctor.com/html-5-reset-stylesheet/
        - googleフォントを使う
            - https://fonts.google.com/?sort=popularity
        - Sass記法を使って、BEMにしたがってデザインしていく
        - HTMLのコーディングが終わったらデザインをする作業に入っていく
        - 簡単なところはfigmaのcssをコピペ
    3. テンプレートタグを使ってHTMLを分割していく
    4. フロントエンド、バックエンドのロジックを考えていく
        - アーキテクチャの型に当てはめながらコーディングを進めるとスラスラ書ける
            - 全体の流れはレイヤードアーキテクチャで意識するとか
            - プレゼンテーション層を書くときはMVCを意識するとか
3. インフラ構築
    - AWS
    - terraform


### 開発の時に見ながら進めるとスラスラ書けるリンク
- Push-MVC、MVPなどアーキテクチャに関する詳しい説明と手順
    - https://github.com/kshina76/centos-backup/tree/master/app_architecture
    - https://light11.hatenadiary.com/entry/2019/01/23/231828
    - https://maku.blog/p/5wu6fbv/


- フロントでMVC、バック(API)でMVCとそれぞれ別のMVCとして構築するといいかも
    - https://qiita.com/ffggss/items/15943c6c3908a6f25cb5


---

## HTML/CSS

### メモ
- reset.cssを活用
    - marginの初期値などを消すために最初に読み込んでおくもの
        - https://pegaro.site/reset-css/
        - http://html5doctor.com/html-5-reset-stylesheet/

- 文字においてのline-heightとpaddingの使い分け
    - line-height...行間の余白の調整に使う
    - padding...段落の余白の調整に使う

- インライン要素とブロック要素
    - HTMLタグのほとんどはインライン要素とブロック要素に分類できる
    - インライン要素にはCSSでpaddingやmarginの上下が効かないので注意する
        - CSSから「display: inline-block」を指定するとインラインとブロック要素の中間としてみなしてくれるからpaddingなどが使えるようになる
        - なぜblockではダメなのかわからん

- paddingとmarginの違い
    - marginは外に余白をとるから、外に影響を及ぼすってことでいいのか？

- px, em, rem, %
    - px...ブラウザから文字サイズを変更しても一切変わらなくなる
    - em...自分の要素から親要素に向かって遡って、font-sizeを見つけたら、「そのfont-size*rem値」がpxの値となる
        - paddingでもmarginでもなんでもfont-sizeを基準に算出される
    - rem...「htmlのfont-size*rem値」がpxの値となる。親要素にどのようなfont-sizeが設定されていても影響を受けないでhtmlを参照する
    - %...emのfont-sizeじゃなくてなんでもいいバージョン。widthなら親要素のwidthを参照するといった感じ
    - 使い分け
        - メディアクエリ...em
        - font-size...em/rem
        - borderなど見た目が変わらない...px
        - それ以外...em/rem
    - 使い分け(remとem)
        - rem...親のfont-sizeに影響されたくなかったらこれ
        - em...それ以外

- px, em, rem, %の使い分けを詳しく
    - 最有力
        - https://daib-log.com/unit/
    - https://ferret-plus.com/12506
    - https://note.com/takamoso/n/nde1275183086

- ヘッダーのロゴを縦方向に中央揃える
    - https://haniwaman.com/vertical-align/
    - https://note.com/tell_me/n/n2a7fda543500

- reset.cssでfont-sizeが100%に設定されている理由
    - ブラウザのデフォルトの16pxやユーザが設定したfont-sizeを正しく表示できるから

- ブログで、記事の部分とサイドバーをきれいに分けるにはflexboxを使って横で2カラムに分ける

- widthとheightとpaddingとmarginの位置関係(絶対意識しながら実装したほうがいい)

    ![4-1024x793](https://user-images.githubusercontent.com/53253817/99183768-9ccee000-2781-11eb-8396-fa75c98118f5.png)

- widthプロパティはデフォルトだとauto(横幅いっぱい)に設定されている
    - つまり子要素のwidthプロパティでパーセント指定した場合、親要素のwidthに何も指定していない場合はauto(横幅いっぱい)に伸ばした値のパーセントをとることになる

- BEMでblockの中のblockの命名規則
    - こっちの方法でこれからはやっていく
        - https://qiita.com/Takuan_Oishii/items/0f0d2c5dc33a9b2d9cb1#blockにはmarginを指定しない
    - 今回はこっちでやってしまった
        - https://stackoverflow.com/questions/40265932/bem-blocks-inside-blocks
    - 個人的な理解
        - 「block__block」にはならない。なぜならblockは一つのファイルに一つだから。「block」と「block」にわけてネストすればいい
        - 「block__element」この場合はオッケー
        - BEMにおいてclass名は被ってはだめ。BEMに沿って命名していれば、被らないはず

- BEMでファイルを分けてコンパイルする方法
    - https://www.i-ryo.com/entry/2020/05/22/185144#importでパーシャルファイルをインポート

- flexboxで縦並びを実現するには、「flex-direction: column」を指定する

### HTML/CSSコーディング規約

- CSSはclassにのみ適用する
    - HTMLタグをCSSセレクタで指定してはいけないということ

- CSSプロパティはアルファベット順に書く
    
    ```css
    .block {
        background-color: #FFF;
        color: red;
        margin: 80px;
        width: 800px;
    }
    ```

- CSSプロパティはまとめて書く
    - padding-bottomとかpadding-rightとかまとめられるなら、まとめて書く

    ```css
    .cell {
        margin: 112px 39px 0 0;
        padding: 26px 0 84px;
    }
    ```

- そのほかの規約は以下から
    - https://qiita.com/pugiemonn/items/964203782e1fcb3d02c3

---

## クラス設計
- 以下の手順でクラスを抽出していく
    - https://github.com/kshina76/centos-backup/tree/master/OOP/oop_design
- 「オブジェクト指向でなぜ作るのか」にクラスの抽出のコツの話があったかもしれない

---