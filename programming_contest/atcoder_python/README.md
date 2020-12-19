# pythonでatcoder


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
- 式を導けたり、使えそうなアルゴリズムが思いついたらライブラリを使って解く
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

### mapの使い方

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
