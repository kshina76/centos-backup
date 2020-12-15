# ゼロから始めるデータベース操作

## 0. 環境構築
- アプリケーションを開発しながらSQLのクエリを試すといったことがあると思うが、そのような時に使える
- 実際のアプリケーション開発では、remote containerのdevcontainerに以下の拡張機能を選んで入れて使う
- postgresqlのdockerコンテナが、なぜかpythonなどと繋がないとSQLToolsで接続できなかった。なぜか。
### 0-1. vscodeのプラグイン
#### 0-1-1. SQLTools(mtxr.sqltools)
- vscodeをSQLクライアントとして、様々な種類のDBMS(DBのサーバ)に接続するプラグイン
- 多分入力補完とかもしてくれる
- RDBMS毎にドライバをインストールする必要がある
  - PostgreSQLの場合は、mtxr.sqltools-driver-pg
- 以下を参考にして構築した
  - https://obenkyolab.com/?p=1546
#### 0-1-2. PostgreSQL(ckolkman.vscode-postgres)
- SQLToolsをPostgreSQLに特化したようなもの。非公式らしいので、とりあえずSQLToolsを使えばいいかな

#### 0-1-3. SQL Server(ms-mssql.mssql)
- これはmicrosoftのSQL Serverという種類のSQLに接続する際に使用するプラグインなので、PostgreSQLやMySQLなどを使用する場合には使わないので注意

---

<br></br>

## 1. データベースとSQL
### 1-2. データベースの構成
- データベースはHDDなどに保存されて、RDBMSというサーバに対してSQLを発行することで、RDBMSがデータベースからデータに対して操作するといった感じ

#### 1-2-1. システム構造

![12216_06](https://user-images.githubusercontent.com/53253817/102182113-1415a200-3eef-11eb-91d7-81820fa4127b.jpeg)

#### 1-2-2. テーブルの構造

![12216_07](https://user-images.githubusercontent.com/53253817/102182295-5c34c480-3eef-11eb-973d-ed930dbd5439.jpeg)

### 1-3. SQLの概要
- SQLは句の順番が決まっていて、「WHEREを使うときはFROMより後にこなければいけない」といったルールがあることに注意する
#### 1-3-1. DDL : データベースやテーブル自体を作成したり削除したりするもの
- CREATE...データベースやテーブルを作成する
- DROP...データベースやテーブルを削除する
- ALTER...データベースやテーブルなどの構成を変更する
#### 1-3-2. DML : テーブルの行を検索したり変更したりするもの
- SELECT...テーブルから行を検索する
- INSERT...テーブルに新規行を登録する
- UPDATE...テーブルの行を更新する
- DELETE...テーブルの行を削除する
#### 1-3-3. DCL : データベースに対して行った変更を確定したり取り消したりする
- COMMIT...データベースに対して行った変更を確定する
- ROLLBACK...データベースに対して行った変更を取り消す
- GRANT...ユーザに操作の権限を与える
- REVOKE...ユーザから操作の権限を奪う
#### 1-3-4. SQLの記述ルール(上3つは、この本のルールなので、なんでもいいのかな？)
- キーワードは大文字
- テーブル名は頭文字のみ大文字
- そのほかは小文字(DB名やカラム名)
- 文字列と日付の定数はシングルクオーテーションで囲む
- 数値の定数は囲まないで、数値だけを書く
- 単語は半角スペースまたは改行で区切る

### 1-4. テーブルの作成
#### 1-4-1. 構文

```sql
CREATE TABLE テーブル名(フィールド,型,制約...)
```

#### 1-4-2. 例
  - PRIMARY KEYは指定したカラムをユニークな値として、DBMSがデータが挿入されるたびに自動的に挿入する

```sql
CREATE TABLE Shohin(
  shohin_id CHAR(4) NOT NULL,
  shohin_mei VARCHAR(100) NOT NULL,
  shohin_bunrui VARCHAR(32) NOT NULL,
  hanbai_tanka INTEGER,
  shiire_tanka INTEGER,
  torokubi DATE,
  PRIMARY KEY (shohin_id)
);
```

#### 1-4-3. 型の種類
- 配列とか真偽値とか
- https://www.postgresql.jp/document/7.3/user/datatype.html
#### 1-4-4. 制約の種類
- 検査制約 : CHECK
  - if文みたいなものをテーブル定義に含めれる
- 非NULL制約 : NOT NULL
- 一意性制約 : UNIQUE
- プライマリーキー : PRIMARY KEY
- 外部キー : REFERENCES
- https://www.postgresql.jp/document/8.3/html/ddl-constraints.html
#### 1-4-5. CHARとVARCHARの使い分け
- 郵便番号などのように決まっているものはCHAR
- 変動する可能性があるならVARCHAR
- http://cafe.76bit.com/creative/web-design/2139/

### 1-5. テーブルの削除と変更
- 削除したテーブルのデータは復元できないので注意
#### 1-5-1. 構文

```sql
DROP TABLE <テーブル名>
```

#### 1-5-2. 例

```sql
DROP TABLE shohin;
```

#### 1-5-3. 構文
- 変更はALTER TABLE構文を使用

```sql
ALTER TABLE <テーブル名> ADD COLUMN <追加したいカラム名> <追加したいカラムの型> <追加したいカラムの制約>;
ALTER TABLE <テーブル名> DROP COLUMN <削除したいカラム名>;
ALTER TABLE <変更前のテーブル名> RENAME TO <変更後のテーブル名>
```

#### 1-5-4. 例

```sql
ALTER TABLE shohin ADD COLUMN shohinmei_kana VARCHAR(100);
```

### 1-5. テーブルへのデータ登録
#### 1-5-1. 構文

```sql
INSERT INTO <テーブル名> VALUES (データ1, データ2,...);
```

#### 1-5-2. 例

```sql
BEGIN TRANSACTION;

INSERT INTO shohin VALUES ('0001', 'Tシャツ', '衣服', 1000, 500, '2009-09-20');
INSERT INTO shohin VALUES ('0002', '穴あけパンチ', '事務用品', 500, 320, '2009-09-11');
INSERT INTO shohin VALUES ('0003', 'カッターシャツ', '衣服', 4000, 2800, NULL);
INSERT INTO shohin VALUES ('0004', '包丁', 'キッチン用品', 3000, 2800, '2009-09-20');
INSERT INTO shohin VALUES ('0005', '圧力鍋', 'キッチン用品', 6800, 5000, '2009-01-15');
INSERT INTO shohin VALUES ('0006', 'フォーク', 'キッチン用品', 500, NULL, '2009-09-20');
INSERT INTO shohin VALUES ('0007', 'おろしがね', 'キッチン用品', 880, 790, '2008-04-28');
INSERT INTO shohin VALUES ('0008', 'ボールペン', '事務用品', 100, NULL, '2009-11-11');

COMMIT;
```

---

<br></br>

## 2. 検索の基本
- FROMを省略するとダミーデータを作ることができる(テクニック)
- 記述順序
  - SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY
- SELECT文の内部的な実行順序
  - FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
### 2-1. 基礎となる検索

```sql
SELECT <カラム名> from <テーブル名>;
```

### 2-2. カラムに別名をつけて検索結果を表示

```sql
SELECT <カラム名> AS <カラムの別名> FROM <テーブル名>;
```

### 2-3. 定数を出力
- レコードの数だけ同じ定数で埋められて出力される

```sql
SELECT shohin_id AS id, '包丁' AS shohin_name, 1000 AS price FROM <テーブル名>;
```

### 2-4. カラム内で重複しているところを排除して表示する
- DISTINCTに複数のカラムを指定した場合は、二つのカラムどちらも一致している場合に排除する

```sql
SELECT DISTINCT <カラム名> FROM <テーブル名>;
```

### 2-5. WHERE句で条件つき検索
- 条件式なので、等価を表す「=」を使ったり、大小関係を表す「<, >」を使う。特殊なのは「<>」で`!=`を表す
- charやvarcharを比較する際は、辞書順で比較される
- ANDやORなどの優先順位を変えたかったらプログラミング言語と同じで「()」を付ければいい
- ANDやORでNULLを判定すると`真`でも`偽`でもない`不明`という値になるので注意
  - テーブル定義でNOT NULLを使う理由にはこのような理由がある

#### 2-5-1. 構文

```sql
SELECT <カラム名> FROM <テーブル名> WHERE <条件式>;
```

#### 2-5-2. 例

```sql
SELECT * FROM shohin WHERE shohin_tanka < 1000
```

- `AND句`や`OR句`を使うと複数の条件を書ける

```sql
SELECT * FROM shohin
WHERE hanbai_tanka > 1000 
AND shohin_bunrui = 'キッチン用品';
```

- `NOT句`で否定できる

```sql
SELECT * FROM shohin
WHERE NOT hanbai_tanka > 1000;
```

- 条件式には計算式を書くこともできる

```sql
SELECT * FROM shohin WHERE shohin_tanka - 200 < 1000
```

- NULLの判定は、`IS NULL`または`IS NOT NULL`で行う

```sql
SELECT *
FROM shohin
WHERE torokubi IS NULL;
```

### 2-6. 算術演算子
- SELECT句には定数だけでなくて、計算式も書ける
- ASで`""`を使ったり使っていないのは、「*」を文字としてみなしたいときに囲っている

```sql
SELECT hanbai_tanka, hanbai_tanka * 2 AS hanbai_tanka2
FROM shohin;
```

```sql
SELECT hanbai_tanka, hanbai_tanka * 2 AS "hanbai_tanka*2"
FROM shohin;
```

---

<br></br>

## 3. 集約と並べ替え
- 集約は「複数の行を一つの行にまとめる」という意味がある
### 3-1. テーブルを集約して検索する
- SQLでデータに対して何らかの操作や計算を行うには「集約関数」というものを用いる
- 集約関数は並べると複数表示できる「SUM(A), SUM(B)」

#### 3-1-1. COUNT: テーブルの行数を数える
- NULLはカウントされない
- NULLを以外のところをカウントしたかったら、NULLを含むカラムを選択することでカウントできる
  - NULLはカウントされないから
- 「*」を指定できるのは集約関数の中でもCOUNTだけ

```sql
SELECT COUNT(*) FROM shohin;
```

#### 3-1-2. SUM: 合計を求める
- NULLは計算式に含めないので気にしなくていい

```sql
SELECT SUM(hanbai_tanka)
FROM shohin;
```

#### 3-1-3. AVG: 平均値を求める
- NULLは数に含まれないので注意

```sql
SELECT AVG(hanbai_tanka)
FROM shohin;
```

#### 3-1-4. MAX, MIN: 最大値・最小値
- MAX,MINは日付型や文字列型にも使用できる

```sql
SELECT MAX(hanbai_tanka),
  MIN(hanbai_tanka)
FROM shohin;
```

#### 3-1-5. DISTINCT: 重複値を除外して集約関数を使用

```sql
SELECT AVG(DISTINCT hanbai_tanka)
FROM shohin;
```

### 3-2. GROUP BY: テーブルをグループに切り分ける
- GROUP BYで指定したものを基準にグループ分けをする
- NULLもグループ分けされる

#### 3-2-1. 構文

```sql
SELECT <カラム名1>, <カラム名2>...
  FROM <テーブル名>
  GROUP BY <カラム名1>, <カラム名2>;
```

#### 3-2-2. 商品の種類ごとにカウントをして表示

```sql
SELECT shohin_bunrui, COUNT(*)
  FROM shohin
  GROUP BY shohin_bunrui;
```

#### 3-2-3. WHEREと一緒に使うことも可

```sql
SELECT shiire_tanka, COUNT(*)
  FROM shohin
  WHERE shohin_bunrui = '衣服'
  GROUP BY shiire_tanka;
```

#### 3-2-4. 集約関数とGROUP BYを使うときの注意点
- GROUP BYを使った時にはSELECTに以下のものしか書けない
  1. 定数
  2. 集約関数
  3. GROUP BYで指定した列名
- SELECTでASを使って別名にしたものをGROUP BYで使ってはいけない
  - GROUP BYがSELECTより先に実行されるから

  ```sql
  SELECT shohin_bunrui AS sb, COUNT(*)
    FROM shohin
    GROUP BY sb;
  ```

- GROUP BYの結果はソートされているわけではなく、ランダム

- WHERE句に集約関数を書いてはいけない
  - 集約関数をかける場所は「SELECT, HAVING, ORDER BY」だけ

  ```sql
  SELECT shohin_bunrui, COUNT(*)
    FROM shohin
    WHERE COUNT(*) = 2
    GROUP BY shohin_bunrui;
  ```

### 3-3. HAVING: 集約した結果に条件を指定する
- GROUP BYしたものを一回表示してテーブルの状態を確認してから、HAVINGで条件を絞るとわかりやすい

```sql
SELECT <カラム名1>, <カラム名2>...
  FROM <テーブル名>
  GROUP BY <カラム名2>, <カラム名2>...
  HAVING <グループの値に対する条件>
```

- GROUP BYした結果でcountが2のものを表示する

```sql
SELECT hanbai_tanka, COUNT(*)
  FROM shohin
  GROUP BY hanbai_tanka
  HAVING COUNT(*) = 2;
```

#### 3-3-1. HAVING句を使うときの注意点
- HAVING句に書ける要素
  - 定数
  - 集約関数
  - GROUP BY句で指定した列名

#### 3-3-2. WHERE句とHAVING句の使い分け
- 集約関数だけはどちらで書いても処理できるが、使い分けはどうするか
- 集約キーに対する処理はWHEREで書くべき理由二つ
  - 実行速度の問題
  - 責務が違うから
    - WHERE句は行に対する条件指定
    - HAVING句はグループに対する条件指定

## 3-4. ORDER BY: 検索結果を並べ替える(ソート)
- カラム名を指定して、指定されたカラムを基準に昇順降順で並び替える
- 複数のキーを指定すると、左から優先的に並び替えられる。優先されたキーが同じだったら二つ目以降のキーの判定が行われる
- ソートキーにNULLがあったら、末尾にまとめて表示される
- 実行順序的に、SELECTにASで名前を付けれる
- 集約関数も使える
- ORDER BYは列番号を指定してソートできるが、見にくいのでやってはいけない
- 記述順序
  - SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY
- SELECT文の内部的な実行順序
  - FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

```sql
SELECT <カラム名1>, <カラム名2>, ...
  FROM <テーブル名>
  ORDER BY <並び替えの基準となる列1>, <並び替えの基準となる列2>, ...
```

- ASC: 昇順
  - 省略可

```sql
SELECT *
FROM shohin
ORDER BY hanbai_tanka;
```

- DESC: 降順

```sql
SELECT *
FROM shohin
ORDER BY hanbai_tanka DESC;
```

- 複数のキー

```sql
SELECT *
FROM shohin
ORDER BY hanbai_tanka, shiire_tanka DESC;
```

- 集約関数を使う

```sql
SELECT *, COUNT(*)
FROM shohin
ORDER BY COUNT(*) DESC;
```

## 4. データの更新
