# pythonでatcoder

## atcoder進捗状況
- AtCoder Beginner Contest
  - 187のA~Dまで

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
- pythonとPyPyどっち
  - https://qiita.com/OKCH3COOH/items/f0c5c4681bc30dddf7f4
- PyPyでnumpyがダメな理由(pypyでのnumpyは追加ライブラリなので、atcoderだと使えない)
  - https://qiita.com/ponnhide/items/c919f3bc549d1228c800
- Pythonでatcoderをするときに見るといい
  - https://nagiss.hateblo.jp/entry/2019/03/12/012944

## atcoderルール
- WA(Wrong Answer)をしてしまうと一回につき5分のペナルティがつくのでローカルでテストする環境が必要
  - 計算量を見積もる能力が必要な理由は多分これ。(TLEはペナルティつくんだっけ？)

## 環境構築
1. pyenvのインストール
  - atcoderは標準ライブラリだけだからpipenvはいらないと思うが、後にWeb開発をすることを考えてインストールしておいていいと思う
  - dockerだと環境の切り替えで時間がかかるから
2. pypy3.6-7.3.0をpyenvでインストール
  - pypyを使う場合、atcoderが7.3.0なので
  - pypyはJITコンパイラで、普通のpythonより速く動作することが期待できる(モノによるが)

  ```bash
  # インストール
  $ pyenv install pypy3.6-7.3.0

  # 環境に適用
  $ cd <開発するディレクトリ>
  $ pyenv local pypy3.6-7.3.0
  ```

3. Python3.8.2をpyenvでインストール
  - atcoderの環境では3.8.2が使われているため
  - scipyとかnumpyとかを書いたプログラムを使いたいならPyPyは使えないのでこっちの環境を使う

4. vscodeでテストを自動化する設定
  - https://qiita.com/chokoryu/items/4b31ffb89dbc8cb86971

5. vscodeでpythonの拡張機能を入れる
  - pythonとかで検索すればmicrosoftのやつが出てくる

6. 入出力のテンプレを用意しておく
  - https://nagiss.hateblo.jp/entry/2019/03/12/012944

7. Pythonで競プロを行うときのtipsに目を通して使うべき標準ライブラリと使わないほうがいいものを認識する
  - https://medium.com/finatext/lets-do-competitive-programming-with-python-9c8b834769f6

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
- pythonだからといってライブラリばかり使うのではなく、自分で実装してみてから、ライブラリを学ぶようにする

## 解き方
### 手順
1. 具体的な数字を使って紙に書いていく
2. 愚直な方法を考えて、計算量を計算してみる。もし愚直な方法で行けそうなら提出する。だめそうなら3に進む
3. 高速化を考えてみて(DPを使う方法とか)、計算量を計算してみる。行けそうなら提出する。だめそうなら4に進む
4. 3の方法にさらに高速化を施してみる
5. 繰り返し
### 探索問題の手順
1. 「どうしたらすべての場合を調べつくせるか」を検討すること。つまり全探索
  - 問題への深い理解をすることで、効率のいい解法が思いつくかもしれないから
2. 全探索を少しでも早くするにはどうしたら良いかを検討する
  - 深さ優先探索での全探索、bit全探索など色々
  - `k - a - b`のような方法での高速化(1個と残りのn-1個に分けて考える方法)
3. 二分探索などを使えないかを検討
4. 半分全列挙を使えないか検討
  - n/2個とn/2個に分けて考える方法
- 参考文献
  - https://qiita.com/e869120/items/25cb52ba47be0fd418d6#5-1-今回扱う問題
### ポイント
- 紙に書くことに心理的障壁があるが、なんでもいいから書いてみるのがいいと思う。その中から思いつくことが多いから
- 実装に入る前に書いて数学的考察を進める
- 場合分けをしっかりできるかどうかは問われる
- atcoder日本4位の人は、具体的な数字を使って考察を進めていた
  - 例えば、変数が3の時はギリギリ満たす。とか、4になるとだめとか、その時の和はどうなるかとか色々な具体例を出して考察して行っている
- 式を導けたり、使えそうなアルゴリズムが思いついたらライブラリを使って解く
- 1時間考えて解けなかった場合は解説見てる
- 解き終わった後に復習することは大事。もっと最適化したコードを書いてみるとか
- まずは全探索で解けるかを考える
  - https://qiita.com/e869120/items/25cb52ba47be0fd418d6#2-すべての基本全探索

---

## pythonメモ
### 内包記法
- [counter for counter in iterator]と記述する

```python
# Lに0,1...Nが格納される
L = [i for i in range(N)]

# int(input())がN回繰り返されて、Lに格納される
# iはカウンタとして使っているだけで、格納はされない
L = [int(input()) for i in range(N)]

# 123がinputだったら[1, 2, 3]というリストに変換する
x = [int(c) for c in str(input())]
```

### mapの使い方: listの全要素に対して同じ処理を行う
- `map(<関数オブジェクト>, <iterable>)`
- iterableなオブジェクトの全ての要素に指定した関数型オブジェクトを適用する
- 返り値はiteratorになるので、listとして扱いたかったらlistでキャストする
- lambdaと一緒に使われることが多い
  - `map(lambda x: x - 2, A)`

### sum, min, maxはイテラブルを受け取る
- `min([1, 2, 4])`は1を返してくれる

### str型はイテラブル
- `if "7" in "720`とかも判定できる

### setを使用した有無判定の高速化
- setを使うと重複を除いた集合を作成できる
- pythonにおける`set`は`hashset`という要素の重複を許可しない集合構造を表す
- https://atcoder.jp/contests/abc187/tasks/abc187_c

### 小数点以下切り捨て
- `a // b`

### 数字の「各桁の〜」の問題の解き方
- int型をstr型に変換してlist型に変換してから、各桁を処理する
  ```python
  n = 2021
  print(list(str(n))) # ["2", "0", "2", "1"]
  ```

### 絶対値を外すことを考えてみる
- ソートしてから組み合わせを引き算することを考えると絶対値が外れたり
- https://atcoder.jp/contests/abc186/tasks/abc186_d

### 累積和
- https://qiita.com/drken/items/56a6b68edef8fc605821

### 「選ぶ」系の問題に帰着
- コンビネーションが使える
- 本体ではなくて「仕切り」をコンビネーションの対象にしたり

### 「Aの数 vs Bの数」でAを勝たせたい時
- Aが勝ちに近くには、以下の方法で近く
  - Aを増やす
  - Bを減らす
- https://atcoder.jp/contests/abc187/editorial/486

### アルファベットだけ抽出
- ^a-zA-Z_ はアルファベット以外を表す

```python
def re_compile(pattern):
    repattern = re.compile(pattern)
    return repattern
# アルファベット以外を空文字にしてから、小文字に変換
text = re_compile('[^a-zA-Z_]').sub('', str(input()))
```

### 文字列の出現回数カウント
- collectionsのCounterを使うと楽にできる

```python
# ライブラリを使わない場合
def str_count(text):
    dic = {}
    for i in text:
        dic[i] = text.count(i)
    return sorted(dic.items())  # keyでソートして返す. valueでソートしたい場合はlambdaで.
```

```python
# ライブラリを使う場合
import collections
dic = collections.Counter(text)
print(sorted(dic.items()))
```

### 文字列の比較は辞書順で大小が決まる

```python
>>> 'python' == 'python'
True
>>> 'Python' == 'python'
False
>>> 'aka' < 'ao'
True
>>> 'yellow' < 'blue'
False 
```

### ビットシフトの使い方
- 2進数において左へ1ビットシフトするとうことは数値が2倍になることを表している
- 右へ1ビットシフトするということは数値が1/2になることを表している
- 例
  - 1 << 0 は 0001を左に0ビットシフトするので、0001を10進数にした数の1が出力される
  - 1 << 1 は 0001を左に1ビットシフトするので、0010を10進数にした数の2が出力される
  - 1 << 2 は 0001を左に2ビットシフトするので、0100を10進数にした数の4が出力される
  - つまり、1をビットシフトすることは2^nを計算していることになる

### zipの使い方
- for文で複数のリストから値を取り出すことができる
- 以下は内積を計算するのにzipを使った例
- https://www.lifewithpython.com/2014/04/python-operate-or-combine-2-lists.html

```python
naiseki = [k * l for (k, l) in zip(list_a, list_b)]
```

<br></br>

## 競プロテクニック
### 計算量
- 計算量の計算ができると、「全列挙するのか」、「動的計画法を使うのか」といった方針を絞ることができる
- 例えば、階上でも10!くらいまでなら全列挙で回しても問題なかったりする
### DP(動的計画法)
- 考え方
  - まずdpテーブルというものを全て埋めてから、指定された箇所をdpテーブルから取り出すと、最適化された値を取得できるという考え方
  - 「dp配列」は指定された添字に関する「最適値」が入っているということを常に頭に入れておかないと余計なことを考える可能性がある
- 思考方法
  - 情報が足りなかったら配列の添字を増やす
  - とりあえずdpテーブルを紙で書いて埋めてみる
  - 一箇所を適当に選んできて、そこを最適化する時のパターンを考える
    - 一個前の添字の値を使ってどのように最適化するかを考える
  - 実際に式に起こしてみる
  - 式を一般化する(漸化式とか)
  - あとはコードに落とし込む
- 0-1ナップサック問題
  - 「選ぶ可能性がある」と「選ぶ可能性がない」に着目する
  - 「選ぶ可能性がある」場合は、選んだものの重さを引いた状態を最適化したものと、選ばなかった場合での最適化を比べて大きい方を選ぶ
  - 「選ぶ可能性がない」場合は、重さを引かない状態を最適化する
- ナップサック問題の思考過程(以下を参考にするとDPの動きがわかる)
  - https://o-treetree.hatenablog.com/entry/DPL1B
  - https://wakabame.hatenablog.com/entry/2017/09/10/211428
### 累積和
- 「区間」系の問題は累積和を考えるようにするとうまくいくことが多い
  - 累積和を求めておいて後で引き算する
- 手順
  - 区間系の問題かどうかを確認する
  - 区間ごとの累積和を紙に記述してみて、どのような操作をすると欲しい答えが求まるかを考察する
- 一見すると累積和を使う問題に見えないこともある
- https://qiita.com/drken/items/56a6b68edef8fc605821
### DP + 累積和
- https://qiita.com/drken/items/56a6b68edef8fc605821#dp-の高速化
### エラトステネスのふるい
- あとで
### 全探索パターン
- 普通に全探索するパターン
  - 愚直にfor文を回すだけ
- すでにわかっているものは探索しないパターン
  - 例えば答えにi,j,kが必要な時にi,jを使ってkの値を求めることはできないかといったことを考える
  - https://qiita.com/e869120/items/25cb52ba47be0fd418d6#パターン-a-既に分かっているものは探索しない
- 探索の通り数を絞り込むパターン
  - よく観察して減らせないかを考える
- 別の視点から全探索する
  - 本体をfor文で回すのではなくて、違う方をfor文で回してマッチングさせていくという方法
  - https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
- bit全探索を使うパターン
  - https://qiita.com/e869120/items/25cb52ba47be0fd418d6#3-1-bit-全探索
- 順列全探索
  - 順列を作ってforで回すだけ
- 深さ優先探索
  - 後述
  - 列挙、探索で使う感じかな？
- 幅優先探索
  - 幅優先探索は最短経路問題を解くにあたって使われることが多い
  - 「全通り数え上げる」系の問題にはあまり使われない
- bit全探索の拡張
  - 2bitではなく3bit以上にも適用できる
- メモ化再帰
  - 深さ優先探索のアイデアを少し変えるだけで、メモ化再帰というDPの仲間のアルゴリズムになる
  - 再帰関数で処理を書くと何回も同じ関数を呼び出すことがあるので、一度登場した関数を全てmemoという配列に保存しておいて、再度登場したら、そこから返すようにするもの
### 効率的な探索パターン
- 二分探索
  - 原理も簡単なので、ライブラリでやってしまうのがいいと思う
  - https://qiita.com/e869120/items/25cb52ba47be0fd418d6#4-1-二分探索アルゴリズム
  - https://qiita.com/T_Wakasugi/items/c979e977f56531942de4
- 二分法
  - x-y平面の関数を思い浮かべて、絵を書いて、1/2をして範囲を縮めながら求める方法。絵を書きながらやればできる
  - https://qiita.com/maskot1977/items/2d409313e52e353e580d
- ニュートン法
  - https://qiita.com/maskot1977/items/2d409313e52e353e580d
- 三分探索
  - https://qiita.com/DaikiSuyama/items/84df26daad11cf7da453
- 枝刈り全探索（IDA*, A* など）
### 深さ優先探索
- 753問題は`itertools.product`で解こうと思ったけど、桁数が違うものも列挙しないといけないから
- 深さ優先探索の書き方がわかる画像
  
  ```python
  # dfsのイメージ
  def dfs(今の状態):
    ret = 0
    for(...)ret += dfs(次の状態)
    return ret
  ```

  - 矢印がreturnを表す感じ

  ![image0](https://user-images.githubusercontent.com/53253817/104353338-206f3800-554b-11eb-998d-b876ea3d9b5f.jpeg)

  ![2021-01-13 2 57のイメージ](https://user-images.githubusercontent.com/53253817/104353245-07ff1d80-554b-11eb-9257-55f4a550a687.jpeg)

- 753問題の解答

  ```python
  n = int(input())
  def dfs(s):
      if int(s) > n:
          return 0
      ret = 1 if all(s.count(c) > 0 for c in "753") else 0  # 7,5,3全てを含んでいたら1、含まない場合は0
      ret += dfs(s + "7")
      ret += dfs(s + "5")
      ret += dfs(s + "3")
      return ret
  print(dfs("0"))
  ```

- 深さ優先探索を使った解き方の手順
  - 1: 問題文をdfsの形に置き換える
    - 例えば、「M個のりんごを、N人で分けるとき、分け方が何通りあるか」というものに対しては、dfs(N, M)と置き換えるとか
  - 2: 深さ1がルート、深さ2のところは1人目、深さ3のところは2人目...のように続く
    - 文字列の探索の問題なら左から1文字目、2文字目...となる
  - 3: ノード毎に、dfsの中身と状態の値を記述する
    - 深さ2のところに、`[dfs(4,2), 0]`、`[dfs(3,2),1]`...のように
  - 4: dfsの添字を一般化して、処理を書いていく
    - 以下の順番に沿って

    ![image0](https://user-images.githubusercontent.com/53253817/104353338-206f3800-554b-11eb-998d-b876ea3d9b5f.jpeg)

- 深さ優先探索と幅優先探索の違い
  - https://www.slideshare.net/chokudai/wap-atcoder2

- 参考文献
  - https://atcoder.jp/contests/abc114/tasks/abc114_c
  - https://www.slideshare.net/chokudai/wap-atcoder2

### いろいろな種類の最短経路問題
- https://qiita.com/ageprocpp/items/cdf67e828e1b09316f6e
