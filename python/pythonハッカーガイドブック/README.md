# Pythonハッカーガイドブック 書籍メモ
## 第2章
### pythonの参照渡し
- pythonは全て参照渡しだけど、再代入した時に、操作したオブジェクトがミュータブルかイミュータブルかで挙動が変わる
  - 例えばlistはミュータブルなので再代入しても同じアドレスを指す。異なるアドレスにしたい場合はcopyライブラリやスライスを使う
  - strやintの場合はイミュータブルなので再代入すると異なるアドレスを指す
- 参考文献
  - https://qiita.com/Kaz_K/items/a3d619b9e670e689b6db
  - https://qiita.com/ponnhide/items/cda0f3f7ac88262eb31e

### collectionsとitertools
- 積極的に使ったほうがいいっぽい
- https://qiita.com/apollo_program/items/165fb01b52702274936c

### 外部ライブラリを選定するときのチェックリスト
- 外部ライブラリの安全性チェックリスト(技術選定に加える)
  - p28-30

### APIラッパーを使ってコードを保護する
- 外部のAPIを使うときは色々な変更との戦いになるから、ラッパーを作っておくことで変更箇所が限定できる
- 有名どころのAPIのラッパーがまとめてある
  - https://github.com/realpython/list-of-python-api-wrappers
- 日本人が作ったAPIラッパー
  - https://qiita.com/sh1ma/items/008eaf2e8b96bf76eda8

### pythonのデバッガpbd、pudb
- pdbはCLI上で対話的にデバッグ出来るライブラリ
- pudbはCLI上でグラフィカルにデバッグ出来るライブラリ
- 個人的にはpudbが操作が簡単で便利だと感じた
- https://qiita.com/Kobayashi2019/items/98e74110d74e4c60f617

### ジェネレータやitertools
- for文とlistのアンチパターンはジェネレータに置き換えろ、リストを組み合わせないでitertoolsのchainを使え
  - p40

### ドキュメント作成
- sphinx

### タイムスタンプとタイムゾーンの処理
- dateutilモジュール

### 関数型プログラミング
- map,filter,zip
- functools
  - functools.partial関数はlambdaよりいい方法
- operator
