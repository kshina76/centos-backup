# 達人に学ぶSQL徹底指南書 初級者で終わりたくないあなたへ メモ

## 0. わかったこと
- 一番重要なのは、データベースは集合として捉えること。手続き型として考えると泥沼にハマるからダメ

  ![スクリーンショット-2019-02-14-18 38 05-1024x600](https://user-images.githubusercontent.com/53253817/102522225-56023c00-40d9-11eb-8188-a9d7205072e1.png)

- 参考文献
  - https://qiita.com/yuse/items/b7ed3d71eb9f35ace7f1

### 0-1. アプリ側から何度も小さいSQL vs 少々小難しいSQLで一発
- 一般的にはアプリ側からループで小さいSQLを繰り返し実行し、小難しい処理はプログラムで対処する。
- ただ、SQLで一発による対応は下記メリットがあるので、比較検討の上実装する。
  - チューニングポテンシャルが高い（複雑であればあるほど）
  - SQL実行時のオーバーヘッドが低い（繰り返し発行されないため）
  - DBの進化によって受けられる恩恵が高い（エンジンの進化によるもの）

### 0-2. union句に注意
- SQLとしては１つだが、実際には複数回テーブルへのアクセスが行われている。
- case式で代用できないか検討すること。

### 0-3. ビューはselect文をDBに保存しているだけ
- つまり、ビュー発行とは、内部的には２段階SQLを実行している。
  - サブクエリは使い捨てのビューなのでDBには保存されない

### 0-4. Group byはホールケーキのカット
- 集約とカットを行う
- 集約を行わないのがpartition by

![images](https://user-images.githubusercontent.com/53253817/102522465-9c579b00-40d9-11eb-93b4-0d2a47a926a1.jpeg)

### 0-5. GROUPBYとPARTITIONBYの違い
- GROUPBYの方は集約までしてしまう

![2020-12-18 3 16のイメージ](https://user-images.githubusercontent.com/53253817/102527073-f65b5f00-40df-11eb-85ea-dafc68b5167b.jpeg)


### 0-6. サブクエリが遅い理由
- 一時的に結果をメモリに保持するためオーバーヘッドが生じる
- 実行時のみの発行のため、インデックスや制約の情報がなく、DBエンジンによる最適化が受けられない
- 相関サブクエリは結果行数分、実行されるためさらにパフォーマンスが悪い

### 0-7. Window関数の使い方(めっちゃわかりやすい)
- https://chopesu.com/sql/はじめてのsql⑨（ウィンドウ関数）/

---

<br></br>

## 1. 魔法のSQL
### 1-1. CASE式のススメ
- CASE式が行っていることは、「振り分け」と考えると応用が思い浮かびやすい
  - 神奈川->関東、東京->関東、高知->四国...県を地域に分ける
  - 0~10->幼少期、11~20->思春期、21~->成人...年齢で括って分類
- CASE式は式なので、どこにでもかけるから、かなり柔軟性があるのでどんどん使っていこう
#### 1-1-1. 単純CASE式と検索CASE式
- 検索CASE式が使われるので、そっちを覚えておけばいい
- 評価式が成り立ったらTHENの式が実行される
- 最後まで成り立たなかったらELSEの式が実行される
- ELSEは省略できるけど、絶対に書くようにする
- SELECTのカラムの指定のところに書いたら、CASE~ENDまでが一つのカラムとして振舞う
  - カラムなので、ASで名前をつけることもできる
- CASEは式なので、式をかけるところに書くこともできる

```sql
CASE WHEN <評価式> THEN <式>
     WHEN <評価式> THEN <式>
     ...
     ELSE <式>
END
```

#### 1-1-2. 既存の体系を他の体系に変換

- 例

```sql
SELECT CASE
    WHEN hanbai_tanka > 500 THEN 'A :' || shohin_bunrui
    ELSE 'B :' || shohin_bunrui
  END AS shohin_grade
FROM shohin;
```

- CASE式に名前をつけて、GROUP BYで使い回す
  - 同じことを書かなくて済む

```sql
select CASE
    WHEN hanbai_tanka > 500 THEN 'A :' || shohin_bunrui
    ELSE 'B :' || shohin_bunrui
  END AS shohin_grade
FROM shohin
GROUP BY shohin_grade
```

#### 1-1-3. 異なる条件の集計を一つのSQLで行う: WHERE句で条件分岐させるのは素人のやること。プロはSELECT句で分岐させる 
- 複数のSQLを一つにまとめることで実行パフォーマンスと可読性の二つを得ることができる
- UNIONでまとめても、結局二つのSQLが発行されるので実行コストは変わらない

- 改善前

```sql
SELECT pref_name, SUM(jinko)
  FROM Poptbl2
  WHERE sex = '1'
  GROUP BY pref_name;

SELECT pref_name, SUM(jinko)
  FROM Poptbl2
  WHERE sex = '2'
  GROUP BY pref_name;
```

- 改善後

```sql
SELECT pref_name,
       SUM(CASE WHEN sex = '1' THEN jinko ELSE 0 END) AS cnt_male
       SUM(CASE WHEN sec = '2' THEN jinko ELSE 0 END) AS cnt_female
  FROM Poptbl2
  GROUP BY pref_name;
```

#### 1-1-4. CHECK制約で複数のカラムの条件関係を定義
- よくわからん

#### 1-1-5. 条件を分岐させたUPDATE
- WHEREを使って複数のSQLで書くより、CASE式を使って一括で書いたほうがミスもないし、パフォーマンスもいい

#### 1-1-6. テーブル同士のマッチング
- よくわからん

#### 1-1-7. CASE式の中で集約関数を使う: HAVING句で条件分岐させるのは素人のやること。プロはSELECT句で分岐させる
- 集計結果に対する条件はHAVING句を使うが、CASEとSELECTで書くと一つのSQLで書くことができる
  - HAVING句を使いたくなったら、CASEとSELECTで書けないか考えてみる

<br></br>

### 1-2. 必ずわかるウィンドウ関数
- ウィンドウ関数を学んでからやる

<br></br>

### 1-3. 自己結合の使いかた
- CROSS JOINはわかりにくいから敬遠していたから、学んでからやる

<br></br>

### 1-4. 3値論理とNULL
- SQLは他のプログラミング言語と違って、「true, false, anknown」の3つの論理値を持っている
- この仕様によってエンジニアが困ることがあるので、後で見返す

<br></br>

### 1-5. EXISTS述語の使い方
- 述語は「返り値が真理値の関数」
- 述語には、BETWEEN,LIKE,IS NULL など色々ある
- EXISTSだけ特異な存在で、複数の行を入力にとる
  - 他の述語は単一の行を入力にとる
#### 1-5-1. 論理学で捉える
- EXISTSは存在量子化を意味する
  - 存在量子化で全称量子化を表すことができる
- 例
  - 「全ての教科が50点以上である」を二重否定して、同値変換すると「50点未満の教科が存在しない」

<br></br>

### 1-6. HAVING句の力
- HAVING句に書ける要素
  - 定数
  - 集約関数
  - GROUP BY句で指定した列名
- リファレンスがP131

#### 1-6-1. データの欠番を探す
#### 1-6-2. 最頻値を求める
#### 1-6-3. NULLを含まない集合を探す
#### 1-6-4. HAVING句で全称量化
#### 1-6-5. まとめ
1. 行は順序を持たないのでソートは行わない
2. ロジックを考えるときは、フローではなくて、円で集合を書く
3. GROUPBYは過不足のない部分集合を作る
4. WHERE句は集合の要素の性質を調べるもの。HAVING句は集合自身の性質を調べるもの。
5. 検索条件の設定は、検索対象が集合なのか、集合の要素なのか見極めることが大事

<br></br>

### 1-7. ウィンドウ関数で行間比較を行う
- 従来の方法だと、相関サブクエリを使って行間比較を実現していた
  - アプリケーション側で実装する場合もあったらしい
- 参考文献
  - https://chopesu.com/sql/はじめてのsql⑨（ウィンドウ関数）/
  - https://qiita.com/YumaInaura/items/5ed5e8d63f325a1837fb
#### 1-7-1. 相関サブクエリを使った方法
- 相関サブクエリとはサブクエリの一種であり、外側のクエリの値をサブクエリ内で使用する
- 着目する行を一つずらすことで比較する

```sql
SELECT year, sale
  FROM Sales AS S1
  WHERE sale = (SELECT sale
                  FROM Sales AS S2
                  WHERE S2.year = S1.year - 1)
ORDER BY year;
```

![907_02](https://user-images.githubusercontent.com/53253817/102528002-4a1a7800-40e1-11eb-9b4f-bf68c202fcba.gif)

#### 1-7-2. ウィンドウ関数を使った方法
- https://chopesu.com/sql/はじめてのsql⑨（ウィンドウ関数）/

<br></br>

### 1-8. 外部結合の使い方
