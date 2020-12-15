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
