# pythonメモ
- プログラミング言語に標準で用意されている組み込み関数とかに渡せる引数はパターンを覚えるのではなくて、公式のドキュメントを見て判断するようにする
  - 例えばmap関数なら、第一引数にクラスとか関数とかを渡すことができるが、第一引数はcallableということを覚えておくだけで、クラスとか関数が渡せるのだなと判断することができる

## Pythonのアンダーバーまとめ
- https://qiita.com/kiii142/items/6879cb065ad4c5f0b901

## Pythonの特殊メソッドまとめ
- http://www.ops.dti.ne.jp/ironpython.beginner/method.html

## lambdaの使いかた
- https://qiita.com/nagataaaas/items/531b1fc5ce42a791c7df
- `lambda 引数: 返り値`で定義する
- lambdaは定義した後は関数と同じように使用する

```python
# 普通に関数を定義する方法
def double(n):
    return n * 2

# lambdaを使った方法
lambda n: n * 2
```

## mapの正しい使い方
- https://qiita.com/conf8o/items/0cb02bc504b51af09099

## クラス変数とインスタンス変数
- クラス変数はクラス直下に`self`を付けずに宣言する
- クラス変数はクラス自体に結びついているので、「クラス.クラス変数」のように呼び出す
- クラス変数にアクセスする場合は、特別な理由がない限り「インスタンス.クラス変数」や「self.クラス変数」のようにアクセスすることは避けるべき

```python
class MyClass:
    value = "abc"             # クラス変数を宣言
 
if __name__ == "__main__":
    print MyClass.value       # abc
```

- インスタンス変数は`__init__()`の中で`self`をつけて宣言する

```python
class MyClass:
    def __init__(self, text): # 初期化： インスタンス作成時に自動的に呼ばれる
        self.value = text     # インスタンス変数 value を宣言する

if __name__ == "__main__":
    a = MyClass("123")        # インスタンス a を作成
    b = MyClass("abc")        # インスタンス b を作成
    
    print(a.value)            # 123
    print(b.value)            # abc
```

## 静的メソッドとクラスメソッド 
- https://qiita.com/motoki1990/items/376fc1d1f3d59c960f5c

## 文字列、リスト、タプル、辞書、集合の定義
- リストとタプルの使い分け
  - 内容を変更する可能性があるものはリスト、可能性がないものはタプル
  - タプルの方が速度が速い
- https://www.atmarkit.co.jp/ait/articles/2001/21/news012.html

![2021-01-04 23 32のイメージ](https://user-images.githubusercontent.com/53253817/103545714-4b231600-4ee5-11eb-8e20-2ee5edfdafe8.jpeg)

## 最速でリスト生成
- よく見る内包記法の`[i for i in range(num)]`より`list(iter(range(num)))`で生成した方が速い

```python
num = 10000000
start = time.time()
list(iter(range(num)))
end = time.time() - start
print(end)  # 0.5557906627655029

start = time.time()
[i for i in range(num)]
end = time.time() - start
print(end)  # 0.7848813533782959
```

<br></br>

## プログミング用語
### Iterator
- next関数を使って次の要素を取得することができるインタフェース
- for文で回せるオブジェクトのこと
### Generator
- イテレータの一種であり、1要素を取り出そうとする度に処理を行い、要素をジェネレートするタイプのもの。Pythonではyield文を使った実装を指すことが多い
### Callable
- `()`をつけて呼び出せるオブジェクトのこと
  - `something()`、`x = something()`、`something(1, 2)`
- クラス、関数、lambda...
- intクラス、strクラス、...
### Iterable
- イテレータになれるオブジェクトのこと
  - イテレータはfor文で回せるオブジェクトのこと
- list、tuple、dict、str、ジェネレータ、mapオブジェクト、fileオブジェクト、rangeオブジェクト...
- イテレータとiterableの違い
  - next関数を使って次の要素を取得することができるものをイテレータ
  - iter関数でイテレータに変換することができるのがiterable
    - 例えば、listならiter(list)でイテレータになるからiterable
### Generics
- listにgenericsでstrを指定すると、listに格納できる型をstrに制限することができる
- ListだけではなくMap、Set、自作のクラスやメソッドなどでも使える
- https://qiita.com/taumax/items/2af451a2c331e8ded892
### ミュータブルとイミュータブル
- ミュータブル: 可変
- イミュータブル: 不変
### シャローコピー(浅いコピー)とディープコピー(深いコピー)
- シャローコピー
  - オブジェクトを複製する際に、コピー元のオブジェクトとコピー先のオブジェクトがメモリ上の同じデータ(インスタンス変数)を参照
- ディープコピー
  - オブジェクトのみのコピーではなく、オブジェクトとメモリ上のデータ(インスタンス変数)の両方をコピー
  - 二つのオブジェクトが参照しているデータは別のもの
### コンストラクタとデストラクタ
- コンストラクタ: インスタンスが生成された時に実行されるメソッド
  - pythonだと`__init__()`で実装
- デストラクタ: インスタンスが削除される時に実行されるメソッド
  - pythonだと`__del__()`で実装
### 第一級オブジェクト
- その言語で値として扱えるデータのこと
- 値として扱えるというのは、代入できたり関数の引数にできたり、戻り値にできたりするという意味
  - Cは関数自体を関数の引数や戻り値にできないので、Cにおいて関数は第一級オブジェクトではない
  - PythonやJavaScriptでは関数を変数に代入したり、関数に渡したりすることができるので、関数は第一級オブジェクトとなる
- 代入したり引数にしたりできるということは、当然関数を値として生成する方法がある
- オブジェクト指向のオブジェクトとはまた別の意味を持つ
- ここでいうオブジェクトは「対象物」とか「値」くらいのふわっとした意味でとらえる
### クロージャとは
- 他の関数によって動的に生成される関数で、その関数の外で作られた変数の値を覚えておいたり、変えたりすることができる。
  - inner関数は外側のローカル変数であるval1とval2の値を参照することができ、outerはinnerを返り値にする。この仕組みをクロージャという

```python
def outer(val1):
    val2 = 2
    def inner():
        val2 = 4
        return val1 * val2
    return inner
```

- クロージャは関数内関数の一種。関数内関数だけどクロージャでは無い例としては以下のようなもの
  - in_funcで外側の変数を参照していないから

```python
def out_func(val1):
    def in_func(val2):
      return val2 * 2
    return in_func(val1)
```

- https://www.nooozui.com/entry/20191108/1573147328#クロージャとは
- https://pg-chain.com/python-closure

### 無名関数、ラムダ、クロージャの違い
- 無名関数は関数名がないもの
- ラムダ(ラムダ式)は無名関数を簡潔に書く方法
- クロージャは関数とその中にある変数、内部関数で構成され、内部関数が関数の戻り値となる(厳密な定義は上で説明している)
  - クロージャは、モノというよりは性質を表す

  ```
  関数 {
    変数
    return 内部関数
  }
  ```

- lambdaをクロージャの性質を満たすように定義したら、lambdaはクロージャになる

  ```python
  def outer(y):
      x = 2
      return lambda x: x*y

  l = outer(2)
  print(l(2))
  ```

- 無名関数もクロージャの性質を満たすように定義したら、無名関数はクロージャになる
### モジュール、関数、オブジェクトの違い
- モジュールは複数のクラスや関数をまとめて一つのpyファイルなどに詰め込むこと
- 関数は関数
- オブジェクトはデータと関数がまとまったもの
- https://blog.pyq.jp/entry/Python_kaiketsu_180220
