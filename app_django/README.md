# webアプリ開発memo

## djangoでまずやること
1. djangoアプリのベースを生成
    - プロジェクトディレクトリを作成して、そこで以下を実行

```bash
mysiteというプロジェクトを生成
$ django-admin startproject mysite .
```

2. サーバを立てられるか確認

```bash
$ python manage.py runserver 8000
```

3. アプリケーションを作成

```bash
pollsというアプリケーションを作成
$ python manage.py startapp polls
```

4. データベースのセットアップ

```bash
$ python manage.py migrate
```

5. アプリケーションをdjangoに伝える
    - ルートディレクトリからの相対パスで指定する

```python
# pollsディレクトリの中にあるapps.pyにConfigのクラスが作成されているから、それを指定する
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

6. モデル（データベースの作成）

7. モデルの変更ファイルを作成

```bash
$ python manage.py makemigrations polls
```

8. モデルの変更を保存

```bash
$ python manage.py migrate
```


##  django memo
- viewは「templateとmodelを繋ぐ架け橋」と「viewを生成する」機能を持つ
<br></br>

- 他のurlで何度も登場するhtmlの文はテンプレート拡張を使って、カプセル化みたいなことをする
<br></br>
- データベースの各レコードにはプライマリキー(pk)という連番の値が自動で割り当てられている。
    - urlのpath内に<int:pk>や<int:info_id>を書くと、pkやinfo_idという変数がviewに渡される
        - viewが関数ベースなら引数にpkのように指定しておけば使えるようになる
        - クラスベースなら、get_context_dataのkwargsに格納されている
    - https://k-mawa.hateblo.jp/entry/2017/10/31/235640

```python
# ユーザがpost/2/edit/にアクセスしたらpk=2となってview内の関数(クラス)の引数になる
path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
```

<br></br>

- urlのpathでnameを指定しておくと、htmlのハイパーリンクでurlを待ち受けることができる

```python
path('post/new/', views.post_new, name='post_new')
```

```html
このハイパーリンクがクリックされたら、post_newというnameのviewを使って描画するという意味
<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
```

<br></br>

- modelの__str__()メソッドの意味
    - 管理画面で表示される文字列を定義する
    - このメソッドがないとオブジェクト名で表示されてしまうため、管理しにくくなってしまう
    - 管理画面で判別しやすいような文字列をreturnするようにする
    - 例えば、ブログのタイトルをreturnすると、そのブログがどのような内容かパッと見でわかるようになる
    - https://office54.net/python/django/model-str-self

<br></br>

- オブジェクト関連マッピング
    - ORMというdjango独自の記法
    - djangoの公式チュートリアルのchoice_setの意味
        - choiceで直接createしてしまうと、questionに結び付けられない。なので、choice_set.createとすることで、questionに関連づいたchoiceを作成できる
    - https://pyhaya.hatenablog.com/entry/2018/10/30/224851#choice_setとは
    

## 静的ファイルとは
- cssや画像ファイルといった動的な変更がされないファイルのこと
- どのユーザでも同じものが使われることから静的と呼ばれている

## CSSセレクタ
- cssでどの部分にレイアウトを適用するかを選択する時に使われる記法
    1. タグ名で判別する
    2. classやidで判別する
- 例えば、bodyタグを指定したら、bodyで囲まれている要素全てにレイアウトを適用することができる。余白とか。

# やったこと
1. 簡単なブログ作成(django girls)

# 参考文献
- https://tutorial.djangogirls.org/ja/