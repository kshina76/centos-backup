# A Tour of Goのメモ

- go言語で自作パッケージのモジュールを参照する
    1. パッケージ名の設定をする
    2. funcの名前の最初を大文字にする
        - 大文字にすることでエクスポートされる
            - エクスポートは「外部参照を許可する」という意味

```go
package mypkg

func Hello() string {
    return "Hello"
}
```

```go
package main

import (
    "fmt"
    m "mypkg"
)

func main() {
    fmt.Println(m.Hello())
}

```

---

- 関数

```go
//ベーシックな関数定義
func add(a int, b int) int {
    return a + b
}

//同じ型の引数を複数指定
func add(a, b int) int {
    return a + b
}

//返り値の型を複数指定
func swap(a, b string) (string, string) {
    return b, a
}

//返り値を事前に指定
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}
```
---

- 変数宣言

```go
var a, b, c int

//初期化を行う場合は型を省略できる
var i, j int = 0, 1
var i, j = 0, 1
var a, b = 0, "hello"

//「:=」を使うとvarも省略できるが、関数内でないと使用できない
func main() {
    i, j := 0, 1
}

//初期化をしなかった場合は0が代入される
var i int
fmt.Printf("%d¥n", i)

//キャスト
i := 3
f := float(i)

//定数(:=は使えない)
const world = "World"
```

---

- for if switch

```go
sum := 0
for i := 0; i < 10; i++ {
    sum += i
}

sum := 0
for ; sum < 1000; {
    sum += sum
}

// goでwhileを表現するにはこのようにする
sum := 0
for sum < 1000 {
    sum += sum
}

//無限ループ
for {

}
```

```go
//条件の前に簡単な式を書くことができる
func pow(x, n, lim float64) float64 {
    if v := math.Pow(x, n); v < lim {
        return v
    }
    return lim
}

//if-else
func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
	return lim
}

```

```go
//breakがいらない、caseは整数である必要がないので柔軟
func main() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
}

//変数を書かなければ、if-elseをスマートに書ける
func main() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}
```

---

- defer
    - deferに書かれたものは評価されるけど、関数の終わりが来るまで実行されない

```go
func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}
```

```go
//deferはLIFOなので、9,8,7...の順で表示される
func main() {
    for i := 0; i < 10; i++ {
        defer fmt.Println(i)
    }
}
```

---

- ポインタ
    - ポインタは型を「*T」のように宣言する
    - goにはポインタ演算がないので、そんなに毛嫌いする必要はないと思う

```go
//ポインタ型の宣言
var a *int = 0

//別の変数にアドレスを格納して、中身を変えると、元の変数の値も変わる
func main() {
	i, j := 42, 2701

	p := &i         // point to i
	fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see the new value of j
}

```

---

- 構造体
    - フィールドの集まり

```go
type Vertex struct {
    X int
    Y int
}
func main() {
    v := Vertex{1, 2}
    fmt.Println(v)  //{1 2}
    fmt.Println(v.X)  //1
    fmt.Println(v.Y)  //2
}
```

```go
type Vertex struct {
	X int
	Y int
}

//structのポインタを使うときに(*p).Xとするのは大変なので、goではp.Xでアクセスできる
func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)
}
```

```go
type Vertex struct {
	X, Y int
}

//structは初期化するたびに新しい領域を確保する
//&を頭につけると、新しく割り当てられたstructへのポインタを返す
var (
	v1 = Vertex{1, 2}  // has type Vertex
	v2 = Vertex{X: 1}  // Y:0 is implicit
	v3 = Vertex{}      // X:0 and Y:0
	p  = &Vertex{1, 2} // has type *Vertex
)
func main() {
	fmt.Println(v1, p, v2, v3)  //{1 2} &{1 2} {1 0} {0 0}
}
```

---

- 配列、スライス
    - 配列の宣言方法とスライスの宣言方法がある

    ```go
    //配列の宣言方法
    array0 := [3]int {1, 2, 3}
    array1 := [...]int {1, 2, 3, 4}
    
    //スライスの宣言方法
    slice0 := []int {1, 2, 3}  //初期化を含めるなら、makeで作らなくていい
    slice1 := make([]int, 3, 5)  //とりあえず領域だけ確保したいならmakeで作る。初期化はゼロで行われる
    var slice2 []int  //長さと容量が0ならとりあえず宣言できる
    ```

    - 配列とスライスの違い
        - 配列
            - 要素を後から追加することができない
            - 配列は値渡し
                - 配列を丸ごと他の配列の変数にコピーするときは値渡し
                - アドレスが違うのでコピー先を変更しても、元の値は変わらない
        - スライス
            - appendで要素を後から追加することができる
            - スライスは参照渡し
                - スライスをコピーするとアドレスがコピーされるので、コピー先を変更すると元の値も変更される
                - もし値渡ししたい場合は、copy()を使うと実現できる

```go
//配列の宣言
var a [10]int

//配列の基本と初期化
func main() {
    var a [2]int
    a[0] = "Hello"
    a[1] = "World"
    fmt.Println(a[0], a[1])  //Hello World
    fmt.Println(a)  //[Hello World]

    primes := [6]int{2, 3, 5, 7, 11, 13}
    fmt.Println(primes)  //[2 3 5 7 11 13]
}
```

```go
//配列からスライスを作成
//primes[:2]とかprimes[4:]なども可能
func main(){
    primes := [6]int{2, 3, 5, 7, 11, 13}
    s := primes[1:4]
    fmr.Println(s)  //[3 5 7]
}
```

```go
//スライスは配列を参照しているだけ。新しく領域を確保しているわけではないので、値を変えると元の配列も変わる
func main() {
	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
	fmt.Println(names)

	a := names[0:2]
	b := names[1:3]
	fmt.Println(a, b)

	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)
    /*
    [John Paul George Ringo]
    [John Paul] [Paul George]
    [John XXX] [XXX George]
    [John XXX George Ringo]
    */
}
```

```go
//スライスの宣言方法
//長さを指定しない
func main() {
	q := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(q)

	r := []bool{true, false, true, true, false, true}
	fmt.Println(r)

	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println(s)
}
```

```go
//makeを使った配列の動的確保
//makeの動作としては、cap分ゼロ化された配列を何個か作って、その配列への参照をするスライスを第二引数のlenの個数分返す
func main() {
    a = make([]int, 5)
    b = make([]int, 5, 10)  //10個分メモリを確保して、5個のスライスを返す
}
```

```go
//スライスのスライス(多次元配列)
//go言語では多次元配列のことをスライスのスライスという
func main() {
	// Create a tic-tac-toe board.
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	// The players take turns.
	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"
}
```

```go
//スライスに新しい要素を追加
func main() {
    var s []int  //len:0, cap:0
    s = append(s, 0)  //len:1, cap:1
}
```

```go
//rangeの使い方
/*
スライスをrangeで繰り返す場合、rangeは反復毎に2つの変数を返します。 1つ目の変数はインデックス( index )で、2つ目はインデックスの場所の要素のコピーです。
*/

var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
}
```



## 気になったこと
- なぜ変数を宣言する時に「<変数名> <型>」という順番なのか？
    - https://blog.golang.org/declaration-syntax

## わかったこと
- typeは既存の型に新たな名前をつけることができる
	- キャストしなければいけない場面
		- 例えば、type Hex int はHex型になるので、他のint型の変数から代入したいときにはHexでキャストしないとだめ
	- 構造体やインタフェースだけでなくて以下のような型にも使える

	```go
	// 配列型
	[10]int

	// 構造体型
	struct {
   		// フィールドリスト
	}

	// ポインタ型
	*int

	// 関数型
	func(s string) int

	// インタフェース型
	interface {
    	// メソッドリスト
	}

	// スライス型
	[]int

	// マップ型
	map[string]int

	// チャネル型
	chan bool
	```


- メソッド
	- レシーバはそのメソッドが属するクラスのようなイメージ
		- この考えを頭に入れておくとわかりやすい
	- レシーバを伴うメソッドの宣言は、レシーバ型が同じパッケージにある必要がある
		- 他のパッケージに定義している型に対して、レシーバを伴うメソッドを宣言できません 
	- ポインタレシーバの用途
		1. メソッドがレシーバが指す先の変数を変更するため
		2. メソッドの呼び出し毎に変数のコピーを避けるため

- メソッドはインタフェース型でなければどんな型にでも定義できる
	- よく構造体に定義されているから、他の型だとできないと考えられがち
	
	```go
	type Hex int
	func (h Hex) String() string {
    	return fmt.Sprintf("0x%x", int(h))
	}
	```

- インタフェース
	- **型にメソッドを実装**していくことでインタフェースを満たす
	- インタフェースの中身を定義する際は暗黙的
		- javaのようにimplementsキーワードがいらない
	- インタフェースの実装パターン
		- https://qiita.com/tenntenn/items/eac962a49c56b2b15ee8

- 空のインタフェース
	- 任意の型を代入することができる
	- 未知の型の値を扱うコードで使われる

	```go
	func main() {
	var i interface{}
	describe(i)

	i = 42
	describe(i)

	i = "hello"
	describe(i)
	}

	func describe(i interface{}) {
		fmt.Printf("(%v, %T)\n", i, i)
	}
	```

- インタフェース型の変数には、そのインタフェースを満たした型を代入することができる
	- 下記の例だと「p=&l」の部分で、Literal構造体は、Printerのインタフェースを満たしているから代入できる
	- ちなみに、インタフェースは「接地面」といった意味があるので、接地面が適合すれば代入できると覚えておけばいい
	- https://qiita.com/peketamin/items/6a65cd9fec0205026afe
	- https://qiita.com/k-penguin-sato/items/885a61d819cc431304f5

```go
//インタフェースを定義
type Printer interface {
	PrintVal()
	PrintStr()
}

type Literal struct {
	val int
	str string
}

//インタフェースを実装
func (l *Literal) PrintVal() {
	fmt.Println(l.val)
}

//インタフェースを実装
func (l *Literal) PrintStr() {
	fmt.Println(l.str)
}

func main() {
	//Printer型(interface型)の変数を定義
	var p Printer

	//インスタンス化みたいなもの
	l := Literal{3, "hello"}

	l.PrintVal()

	//PrintStrとPrintValの両方を実装していないとエラーになる
	p = &l
}
```

- 型アサーション

- 型switch

- Stringer

- error




## 読んだ方がいい記事
- goの特徴や細かい仕様の部分を解説している
	- https://cybozu.atlassian.net/wiki/spaces/pubjp/pages/6422530/Go
- effective go
	- http://golang.jp/effective_go
- 