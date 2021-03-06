# 競技プログラミングAOJ

## goで行うときの注意点
- 複数のファイルにmainを作りたい時
  - 以下を無視したいファイルの先頭につける
  - ビルドされないらしい
  - http://toqoz.hateblo.jp/entry/2013/11/04/215910

```go
// +build ignore
```

## 準備
### よく使う関数をコピペ
### よく使うライブラリをコピペ


## tips
### 変数を固定して、エッジパターンを調べてみる

### とにかく図に表してみる
- 選んでくる系のものとか、簡単な例を使ってどのように選んでくるかを図示すると法則性が見えてくる

### 二値で表せるかを考える(0,1で)

<br></br>

## わかったこと
### Go言語でLIFO(スタック)
- deferはスタックと同じ動作をする
- deferを使うとその関数がreturnする直前にスタックからpopしていく

### 多次元スライスの宣言と初期化

```go
//n * m配列
graph := make([][]string, n)
for i:=0; i<n; i++{
    graph[i] = make([]string, m)
}
```

### 要素数がわかっているときはmakeではなくて直接要素数を指定する(初期化もしてくれる)

```go
var B [4][3][10]int
```

### 標準入力がScanfの方が楽？？

```go
fmt.Scanf("%d", &n)
fmt.Scanf("%d%d%d%d", &b, &f, &r, &v)
```

### 行列の掛け算

```go
// [i,k] = [i,j]*[j,k] となるところがポイントで、覚えておけばすぐに出てくる
for k := 0; k < l; k++{
		for i := 0; i < n; i++ {
			for j := 0; j < m; j++ {
				result[i][k] += A[i][j]*B[j][k]
			}
		}
	}
```

<br></br>

## もう一度やる問題
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_C


<br></br>

## 参考
- Goで標準出力から標準入力
  - https://qiita.com/tnoda_/items/b503a72eac82862d30c6
- print系のまとめ
  - https://qiita.com/taji-taji/items/77845ef744da7c88a6fe
- いろいろ入出力
  - https://qiita.com/sun_bacon/items/1370b2364fb808024ab4
- 競技プログラミングで使うGo言語基礎
  - https://qiita.com/sun_bacon/items/1370b2364fb808024ab4
- 文字列操作まとめ
  - https://qiita.com/tchnkmr/items/b3d0b884db8d7d91fb1b
- 正規表現
  - https://ashitani.jp/golangtips/tips_regexp.html
- go言語のrune型
  - https://qiita.com/seihmd/items/4a878e7fa340d7963fee
