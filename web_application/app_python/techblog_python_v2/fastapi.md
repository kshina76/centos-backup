# fastapiチュートリアル
- 基本的に以下のサイトで入門して、追加でSQLを使いたいなら公式を読むって感じでいいと思う
  - https://qiita.com/bee2/items/75d9c0d7ba20e7a4a0e9
<<<<<<< HEAD
  
=======
  - 
>>>>>>> 102643de1dcca9efa79a1f1f618881fe2cf4a701

## Swaggerのドキュメントの見方
- 上段のレスポンスが返ってきたもの
- 下段のresponsesはレスポンスとして定義されているものを一覧表示している

<br></br>

## パスパラメータ、クエリパラメータ、リクエストボディのまとめ
- パラメータがパスで宣言されている場合は、優先的にパスパラメータとして扱われます。
- パラメータが単数型 (int、float、str、bool など)の場合はクエリパラメータとして解釈されます。
- パラメータが Pydantic モデル型で宣言された場合、リクエストボディとして解釈されます。

<br></br>

## パスパラメータ
### Pythonの型宣言(アノテーション)を使用することで、FastAPIはデータのバリデーションを行う
- `/items/hoge`のように違う型のリクエストが飛んできたらエラーのしてくれる

```python
@app.get("/items/{item_id}")
def item(item_id: int):
  return {"id": item_id}
```

### 順序
- どちらのルーティングも`/users/me`に該当するが、順番に評価されるため上のパスだけが合致する

```python
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

### enum
- パスパラメータの有効な値を事前に設定したい場合は、Enumを使う
- Enumと同時に設定したい型(今回の場合はstr)を継承しておくと、Swaggerでドキュメントを作るときに正しくレンダリングしてくれる
- Enumに関しては以下を参考
  - https://www.lifewithpython.com/2018/08/python-enum-type.html

```python
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

### パス変換
- `{file_path:path}`としておくことで、パスが入ってきても問題なく動作する。
- `/files/home/johndoe/myfile.txt`にリクエストがきても問題ない

```python
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

<br></br>

## クエリパラメータ
- `/items/?skip=10&limit=20`のようなパスを受けることができる
- `skip: int = 0, limit: int = 10`でクエリパラメータのデフォルト値を設定している

```python
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### オプションのパラメータ: デフォルト値をNoneにすることでオプションを表現
- python標準のOptionalを使うとstr型にNoneが入れることができる
  - mypyだとOptionalを使わないとエラーになるらしい
- boolも宣言できる

```python
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

### 必須のパラメータ
- デフォルト値を与えなければいいだけ

```python
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
```

<br></br>

## リクエストボディ
- pydanticで、辞書オブジェクトのバリデーションやキャスト、またSQLAlchemyのORMとの組み合わせなどもできる
- pydanticは飛んできたデータを所定の型に埋め込む感じかな？？
### 基本
#### pydanticを使った方法: postで飛んでくるjsonのフォーマットが一定な場合
- `item_dict = item.dict()`のようにするとモデルにアクセスできる

```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
async def create_item(item: Item):
    return item
```

#### Bodyを使った方法: postで飛んでくるjsonのフォーマットが一定でない場合に使う
- `body=Body(...)`でリクエストのボディ部から取得することができる

```python
from fastapi import Body, FastAPI

@app.post("/items")
def create_items(item: dict = Body(...)):
    return item
```

- 参考文献
  - https://sig9.hatenablog.com/entry/2020/03/08/000000
  - https://fastapi.tiangolo.com/ja/tutorial/body-multiple-params/#singular-values-in-body

### リクエストボディ + パスパラメータ
- `item_id: int, item: Item`と二つ宣言をしても、pydanticBodyで宣言されているものはリクエストボディから取得する
- 「** + 文字列」はpythonだと辞書型を表す
- 「* + 文字列」はタプル

```python
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
```

<br></br>

## クエリパラメータの検証

### クエリパラメータに制限をつける: 色々あるからvscodeで引数を見ながら使えそうなのを使う
- `Query(None, max_length=50)`で50文字制限
- `Query(None, min_length=3, max_length=50, regex="^fixedquery$")`で正規表現で制限
- `Query("hoge", max_length=50)`でデフォルト値
- `Query(..., min_length=3)`で値を必須にする(...の部分)
- ただの`None`は内部的に`Query(None)`に書き換えられて実行されている

```python
@app.get("/items")
def get_items(q: Optional[str] = Query(None, max_length=50)):
    return {"q": q}
```

### クエリパラメータに複数の値を渡す
- `q: Optional[List[str]] = Query(None)`
- `http://localhost:8000/items/?q=foo&q=bar`でリクエストが来ると、qにリストでfooとbarが格納される

```python
@app.get("/items")
def get_items(q: Optional[List[str]] = Query(None)):
    return {"q": q}
```

- デフォルトの値を渡す

```python
@app.get("/items")
def get_items(q: List[str] = ["foo", "bar"]):
    return {"q": q}
```

### エイリアス
- クエリパラメータの仕様は`item-query`だけど、pythonのlint的には`-`は使いたくないといった時の対処法
- `Query(None, alias="item-query")`
