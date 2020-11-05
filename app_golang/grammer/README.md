# go学習memo
- go言語はpackageにmainと記述されたものを最初にrunする
    - mainパッケージ内のmain関数が最初に実行される

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

```bash
//main.goがmainパッケージでない場合はエラーになる
$ go run main.go
```

<br></br>

- ソースを整形する
    - goでは標準でソースコードを整形する機能がついている

```bash
$ gofmt <src>
```

<br></br>

- Print, Println, Printfの違い
- 主に出力が違う
    - Print
        - 改行無し、引数間に空白無し、フォーマット無し
    - Println
        - 改行有り、引数間に空白有り、フォーマット無し
    - Printf
        - 改行無し、空白無し、フォーマット有り（C言語と同じ感じ）

```go
num := 123
str := "ABC"

fmt.Print("num=", num, " str=", str, "\n")	// 改行無し、引数間に空白無し、フォーマット無し
fmt.Println("num =", num, "str =", str)	// 改行有り、引数間に空白有り、フォーマット無し
fmt.Printf("num=%d str=%s\n", num, str)	// 改行無し、空白無し、フォーマット有り
```

```
//実行結果
num=123 str=ABC
num = 123 str = ABC
num=123 str=ABC
```

- さらに接頭辞や接尾辞にFやSがつくことで挙動が変わる
    - 覚え方
        - https://qiita.com/taji-taji/items/77845ef744da7c88a6fe

<br></br>

- 変数, 定数
    - 「var 変数名 型名」で定義
    - :=は定義、=は代入
        - 定義されていない変数に=で代入しようとするとundifinedエラーになる
    - 定義も代入もまとめてできる

```go
//変数を定義
var a1 int
var a2 int = 123
var a3 = 123
a4 := 123
var (
    a5 int = 123
    a6 int = 456
)

//変数に代入
a1 = 456
name, age = "Yamada", 26

//定数を定義
const foo = 123
const {
    foo = 123
    baa = 456
}
```

<br></br>

- 型に名前をつける

```go
type UtcTime string		// string型の別名 UtcTime を定義
type JstTime string		// string型の別名 JstTime を定義
var t1 UtcTime = "00:00:00"  //UtcTimeはstring型と定義したから、string型を代入している
var t2 JstTime = "09:00:00"
t1 = t2				// 型が異なるので代入エラー
```

<br></br>

- 配列
    - コンパイル時に個数が決まるため、個数が変更不可能

```go
a1 := [3]string{}
a1[0] = "Red"
a1[1] = "Green"
a1[2] = "Blue"
fmt.Println(a1[0], a1[1], a1[2])

//初期化も一緒に
a1 := [3]string{"Red", "Green", "Blue}

//初期化の個数に配列の要素数を合わせる
a1 := [...]string{"Red", "Green", "Blue"}
```

<br></br>

- スライス
    - 個数を変更可能にした配列
    - make(スライス型, 初期個数, 初期容量) 

```go
a1 := []string{}			// スライス。個数不定
a1 = append(a1, "Red")
a1 = append(a1, "Green")
a1 = append(a1, "Blue")
fmt.Println(a1[0], a1[1], a1[2])

//初期容量を決めておく確保の仕方
bufa := make([]byte, 0, 1024)
```

## 環境構築
- dockerインストール
    - https://qiita.com/kurkuru/items/127fa99ef5b2f0288b81
- go環境構築
    - https://qiita.com/uji_/items/8c9eda89526abe0ba900

## 学習ロードマップ
- 書籍やサイトを紹介
    - https://qiita.com/tenntenn/items/0e33a4959250d1a55045
- golang標準ライブラリでwebアプリ開発
    - Goプログラミング実践入門 標準ライブラリでゼロからWebアプリを作る(書籍)

