# コードリーディング
- 開発はボトムアップ
- コードリーディングはトップダウン
- 後述する1つ目と2つ目の方法を組み合わせ行う

## 1つ目の方法
https://medium.com/launch-school/how-to-read-source-code-without-ripping-your-hair-out-e066472bbe8d

1. 自分が興味のある機能(メソッド)に絞る
2. 実際にその機能を使った小さいプログラムを書いて動かせるようにする
3. その機能(メソッド)にbreakpointを打つ
4. その機能をトレースしてみる
  - コールグラフを表示するまたは、トレース状況をコマンドラインに表示する
  - これによって所属しているクラスやスーパークラスがわかる
  - この時点ででは深くまで調査しないで、どのような繋がりで呼ばれているかということが分かればいい
5. GitHubの検索で、4で調査したクラス名やメソッド名を繋げて検索してみて該当のクラスを割り出す
  - vscodeの定義にジャンプを使えば済む話だと思ったので、vscodeを使った方法でいいと思う
6. 5で到着したメソッドがどのようなものかを調査する。その際に、他のメソッドの呼び出しなども書いてある場合があるが、他のメソッドに関しては基本的には返り値だけ見ればいい気がする。必要ならドリルダウンするって感じで。コールグラフ的なのは図に書きながら残すといい。

## 2つ目の方法
https://towardsdatascience.com/the-most-efficient-way-to-read-code-written-by-someone-else-cb1a05102b76

1. まずそのコードが何をするコードなのかを調べる
  - 入力と出力はなんなのか
2. main関数、開始地点を見つける
  - CやJavaならmain関数
  - pythonならインデントで判断
  - 外部のライブラリを使っている場合は、クラスを呼び出すのがほとんどだからmainとかは関係ない気がする
3. エディタのデバッガを使いながら調査
  - 各行の入力と出力を確認してコメント
  - 変数がどのように変化するかをコメント
  - 何をする行かわかったらコメント
4. マインドマップを作成する
  - 真ん中は自分が調査を始めた機能のメソッド名またはファイル名として、コールグラフを完成させていく。
  - その際に3で調査した変数名と中身と説明を書き残していく
  - さらに、入力と出力、型や期待される型も書き残す
5. 1〜4の情報を使って解き明かす

## 3つ目の方法
- https://qiita.com/zizynonno/items/3a14fe6cbf52451a366c

## デバッガ
- pbd
  - pythonのCLIベースのデバッガ
https://qiita.com/Kobayashi2019/items/98e74110d74e4c60f617
http://uokada.hatenablog.jp/entry/2016/06/04/180841
https://stackoverflow.com/questions/26812150/debugging-flask-with-pdb

- IDEを使ったデバッグを使う場合は、言語のデバッグ機能と再起動をオフにしないといけない
https://www.subarunari.com/entry/2018/03/10/いまさらながら_Flask_についてまとめる_〜Debugger〜
