# プログラミングTypeScript 書籍メモ

## TypeScriptの利点
- テキストエディタで入力した段階でエラーがあった場合に知らせてくれる
  - 実行する前に知らせてくれるということ
  - TSCがTypeScriptからJavaScriptにコンパイルする前に型チェックをするのであって、コンパイルする瞬間に形をチェックするわけではない
- 2種類の型システムを採用していて、適宜プログラマが選択していい
  - コンパイラに型推論をさせる方法(型を省略する)
  - 明示的にアノテーションをしてコンパイラに伝える方法(型を明示する)

## TypeScriptのセットアップ
- P11~16

## TypeScriptの文法
- 型システム
  - アノテーションは必要なときにだけ使用する

  ```TypeScript
  //明示的に型をアノテーションする
  let a: number = 1
  let b: string = 'hello'
  let c: boolean[] = [true, false]

  //型推論させる
  let a = 1
  let b = 'hello'
  let c = [true, false]
  ```
