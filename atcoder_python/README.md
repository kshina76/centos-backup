# pythonでatcoder

## to do
### atcoderのpythonバージョンと使えるライブラリとバージョンで環境構築する
- 調べながら(公式とかに書いてあるのかな)
### Lambdaの記事をサッとまとめる
- とりあえずバイト先で読んだところまででいいかな
### pythonのwebアプリケーション開発環境を整える
- dockerで整える
### pythonのファイル分割を学ぶ
### pythonの各種ライブラリ
- https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4
- https://qiita.com/hoto17296/items/0ca1569d6fa54c7c4732
- https://www.sukerou.com/2019/04/sqlalchemysqlsql.html
- https://qiita.com/kotamatsuoka/items/a95faf6655c0e775ee22
### pythonでレイヤードアーキテクチャをやってみる(各種ライブラリの使い方は学びながら。techblogでいいかな)
- https://qiita.com/yu-sa/items/e0033ae312669256cd8a
- 疑問点
  - DIはどこで行う？
    - if mainのところで行う
  - golangでいうハンドラ関数はどこで定義するの？
    - pythonだとflaskでURLルーティングと一緒に書くことになる
  - interfaceはどうするの？
    - ABCなんたらでできる
- プレゼンテーション層
  - View(テンプレートエンジン)...jinja2
  - Controller(urlルーティンングとハンドラ)...flask
- ユースケース層
- インフラ層
  - SQL...psycopg2
    - https://qiita.com/hoto17296/items/0ca1569d6fa54c7c4732
  - ORM...flask-SQLAlchemy
    - ORMでも生のSQLでもどっちでもかけるらしい
    - https://www.sukerou.com/2019/04/sqlalchemysqlsql.html
  - 簡易なORM...dataset
    - https://dev.classmethod.jp/articles/python-orm-dataset/



### SQLをブラウザ上でサクッとテスト
- http://sqlfiddle.com

## pythonを使う理由
- 業務で使うから
  - 配列操作や文字列操作がパッと書けると重宝すると思う
- 標準ライブラリが充実しているから

## pythonでatcoderをやるときに見るところ
- いろいろなアルゴリズムの実装(標準ライブラリでないやつ)
  - https://kato-hiro.github.io/AtCoderClans/libraries
- 競プロ用自作ライブラリ
  - https://tabisukelog.com/competition-programming-my-library/
- atcoderの新環境のまとめ
  - https://it-for-pharma.com/atcoder-pythonの新環境についてまとめていく-1-組み込み関数
- atcoderでよく使うpython手法
  - https://qiita.com/chun1182/items/ddf2b6cba932b2bb0d4e
- 競プロで使える標準ライブラリ
  - https://qiita.com/__ynyn__/items/9e75cc37c4b4541a8dd2
  - https://qiita.com/Kentaro_okumura/items/5b95b767a2e691cd5482
- 競技プロを勉強する手順
  - https://maspypy.com/atcoder-橙2400になりました

## 環境構築
- dockerだと色々面倒だから、ローカルの環境を使っていいと思う。バージョン管理ライブラリとかは使うように。
- atocoderと同じバージョンで環境構築する

## 勉強する手順
1. AOJのintroductionで言語に慣れる
  - 文字列操作や配列の扱いなど
  - 標準ライブラリや人が作ったライブラリを積極的に使って、使いこなせるようになる
  - atcoderで使いそうなimport文をコメントアウトして溜めていく
2. Project Euiler
  - 時間制限などがないからとっかかりやすい
  - 標準入力や標準出力の形式がないので、自分でatcoderに合わせた標準入力や標準出力を練習する
  - 一気に終わらせる必要はなく、区切りがいいところで3に進んだり戻ったりする
  - 標準ライブラリや人が作ったライブラリを積極的に使って、使いこなせるようになる
  - atcoderで使いそうなimport文をコメントアウトして溜めていく
3. 「レッドコーダーが教える」に沿って学習していく
  - https://qiita.com/e869120/items/f1c6f98364d1443148b3#1-5-茶色コーダーで要求される-4-つのこと

## 解き方
1. 実装に入る前に書いて数学的考察を進める
2. 式を導けたり、使えそうなアルゴリズムが思いついたらライブラリを使って解く
