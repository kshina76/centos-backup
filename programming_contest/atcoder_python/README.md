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
