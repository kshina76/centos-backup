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
### 設計
1. ユースケース図(箇条書きでも可)
    - 「誰が何をするか」ということを明確にして書いていく
2. 画面遷移設計、デザイン
    - 「figma」というUI/UXツールでページのデザインを作成
    - Frameを意識することで、HTMLタグの付け方が頭に浮かんできて、後々のコーディング作業で楽になるという付加効果もある
    - 一つのページにFrameを分割して矢印を書けば、画面遷移図になる
    - 画面遷移設計は漏れが無いようにするためにユースケース図を参考にしながら進める
3. URL設計
    - ユースケース図を参考にしながらURLを考えていく
4. DB設計
    - 本でしっかり学ぶ
5. アーキテクチャ設計、クラス設計
    - アーキテクチャ設計はMVCとかクリーンアーキテクチャとか
    - クラス設計は
6. システム構成設計
    - インフラとか

### 開発
1. コーディング
    1. テンプレートタグとかを使うなら、テンプレートのパースと簡易サーバの部分のコーディングは作っておく
    2. HTMLを全てコーディングする(HTML設計)
        - タグ付けはデザインを作った時のFrameを参考にすると良い
        - 後のCSSのことを考えながらタグづけを行っていく
    3. CSSでデザインをする
        - HTMLのコーディングが終わったらデザインをする作業に入っていく
        - 簡単なところはfigmaのcssをコピペ
    4. バックエンドのロジックを考えていく
        - アーキテクチャの型(MVCとか)に当てはめながらコーディングを進めるとスラスラ書ける
2. インフラ構築

---

## クラス設計
- 以下の手順でクラスを抽出していく
    - https://github.com/kshina76/centos-backup/tree/master/OOP/oop_design
- 「オブジェクト指向でなぜ作るのか」にクラスの抽出のコツの話があったかもしれない

---