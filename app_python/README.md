# flask+postgresqlでtechblog開発

## 開発環境
- https://ameblo.jp/kazusa-g/entry-12592477686.html
### 1.docker
#### Dockerfile動作確認
- pythonコンテナ

```dockerfile
FROM python:latest
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# CMD [ "python", "./your-daemon-or-script.py" ]
```

```bash
$ docker build -t python .
$ docker container run -it --rm --name python python /bin/bash
```

- postgresqlコンテナ

```dockerfile
FROM postgres:latest
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG en_US.UTF-8
COPY ./project/data/*.sql /docker-entrypoint-initdb.d/
```

### 2.python
#### pythonバージョン
- python3.9.0
#### 今時のpythonの書き方
- https://qiita.com/nicco_mirai/items/c1810ed2a6fc8c53c006
#### インストールするパッケージ
- コード規約が強い順に「pep8 < flake8 < pylint」らしい
- black+flake8はflake8のエラーの解消など色々やってくれる(今後デファクトになる可能性が高いらしい)
  - https://www.macky-studio.com/entry/2019/07/04/152323

```bash
# requirements.txt
flask == 1.1.2
psycopg2 == 2.8.6
flake8 == 3.8.4
black == 20.8b1
```

#### flask
- 以下テストコード

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def func_1():
    return "Hello world"


@app.route("/test")
def func_2():
    return "Test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

```

#### blueprint
- urlルーティングを分散させる感じかな？djangoにも似たようなのが標準で搭載されていた
- https://qiita.com/shimajiri/items/fb7d1d58de0b0d171c88

### 3.vscode
- blackとflake8を有効化、pylintを無効化、一行あたりの最大値をflake8の88行に合わせる
  - 以下を.devcontainer.jsonのsettingに書く

```json
// リンタの設定
"python.linting.pylintEnabled": false,
"python.linting.flake8Enabled": true,
"python.linting.lintOnSave": true,
"python.linting.flake8Args": [
	"--max-line-length",
	"88",
	"--ignore=E203,W503,W504"
],
// フォーマッタの設定
"python.formatting.provider": "black",
"editor.formatOnSave": true,
"editor.formatOnPaste": false
```

- 参考文献
  - https://www.macky-studio.com/entry/2019/07/04/152323
  - https://qiita.com/tsu_0514/items/2d52c7bf79cd62d4af4a

<br></br>


## to do
### まず日課の競プロ
### flaskでアプリを書いてみる(HTMLは流用するが、templateエンジンが変わっているから注意)
### pythonのファイル分割を学ぶ
### pythonの各種ライブラリ
- https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4
- https://qiita.com/hoto17296/items/0ca1569d6fa54c7c4732
- https://www.sukerou.com/2019/04/sqlalchemysqlsql.html
- https://qiita.com/kotamatsuoka/items/a95faf6655c0e775ee22
### pythonでレイヤードアーキテクチャをやってみる(各種ライブラリの使い方は学びながら。techblogでいいかな)
- https://qiita.com/yu-sa/items/e0033ae312669256cd8a
- 疑問点
  - DIはどこで行う？
    - if mainのところで行う
  - golangでいうハンドラ関数はどこで定義するの？
    - pythonだとflaskでURLルーティングと一緒に書くことになる
  - interfaceはどうするの？
    - ABCなんたらでできる
- プレゼンテーション層
  - View(テンプレートエンジン)...jinja2
  - Controller(urlルーティンングとハンドラ)...flask
- ユースケース層
- インフラ層
  - SQL...psycopg2
    - https://qiita.com/hoto17296/items/0ca1569d6fa54c7c4732
  - ORM...flask-SQLAlchemy
    - ORMでも生のSQLでもどっちでもかけるらしい
    - https://www.sukerou.com/2019/04/sqlalchemysqlsql.html
  - 簡易なORM...dataset
    - https://dev.classmethod.jp/articles/python-orm-dataset/
### SQLをブラウザ上でサクッとテスト
- http://sqlfiddle.com
