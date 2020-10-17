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

8. モデルの変更を保存(モデルの変更があるたびに行う)

```bash
$ python manage.py migrate
```

9. urlconfigからアプリケーションディレクトリのurlconfigにincludeする

10. admin.pyにモデルを登録

11. superuserを作る

```bash
python manage.py createsuperuser
```

12. adminサイトでモデルにデータを追加してみる

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
    - djangoの公式チュートリアルのq.choice_setの意味
        - questionオブジェクトに関連づけられたchoiceオブジェクトのこと
        - choiceで直接createしてしまうと、questionに結び付けられない。なので、choice_set.createとすることで、questionに関連づいたchoiceを作成できる
    - https://pyhaya.hatenablog.com/entry/2018/10/30/224851#choice_setとは
    - https://docs.djangoproject.com/ja/3.1/ref/models/relations/

<br></br>

- モデルのフィールドはクラス変数みたいに思えばいい
    - フィールドの値の初期化をしたければ、class_name(引数=1, 引数=2, ...)のように本来のpythonの使い方のように行えばいい。

<br></br>

- html内でpython構文を用いる際の注意
    - pythonで関数を呼び出すときall()のように呼び出すが、djangoを使ったhtml内ではallと記述して、()は付けない

<br></br>

- 機能を実装する時は、ヘルパー関数がないか調べる
    - 例えば404 not foundを実装したい時の例

<br></br>

- templates内にそのままhtmlを置いてはいけない理由
    - 一つのdjangoプロジェクトに複数のアプリケーションが作られる可能性があるから
    - pollsアプリとblogアプリを作りたかったらtemplates内にpollsディレクトリとblogディレクトリを作るようにする

<br></br>

- テンプレート内にurlをハードコードしない
    - ハードコードしないことによって、開発中にurlを変更したいときにurlファイルをいじれば簡単に変更できるようになる
    - ダメな例は、/polls/{{ question.id }}/ のようにurlがそのまま書かれてしまっている
    - 良い例は、{% url 'detail' question.id %} のようにurlファイルに書かれているurlを参照するように処理している

```html
//リンクを複数生成するプログラム(questionの個数分だけリンクが生成される)

//ダメな例
{% for question in latest_question_list %}
    <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
{% endfor %}

//良い例
{% for question in latest_question_list %}
    <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
{% endfor %}
```

```python
//urlファイルの設定(name='detail'とすることが重要)
path('<int:question_id>/', views.detail, name='detail')
```

<br></br>

- URLの名前空間
    - 一つのdjangoプロジェクトの中に複数個のアプリケーションが作られることがある場合に必要になる
    - 例えば、blogアプリとpollsアプリがあって、どちらのアプリにもdetailというviewがあった場合にdjangoがどちらのviewかを認識出来るようにする

```python
# urlファイルにapp_nameで設定する
# これによって、pollsのdetailとdjangoが認識できるようになる
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]
```

```html
//テンプレートも変更する

//変更前
{% url 'detail' question.id %}

//変更後
{% url 'polls:detail' question.id %}
```

<br></br>

- djangoにおいてhtml内でforループのカウンターを使う
    - forloop.counter を使う
    - 0からカウントさせたかったら、forloop.counter0 を使う
    - https://opendata-web.site/blog/entry/17/

```html
{% for list in lists %}
    {{ forloop.counter }} : {{ list.name }}
{% endfor %}
```

```
  1 : name1
  2 : name2
  3 : name3
```

<br></br>

- formに入力されたものをdjangoで処理する方法
    - htmlのformのactionタグに記述されたviewは、postされた瞬間に動作する
    - ラジオボタンのname='choice'はviewでPOSTされた内容にアクセスする際にrequest.POST['choice']とアクセスするために必要
    - ラジオボタンのvalueは選択されて送信されたときに、request.POST['choice']に格納されるから必要
    - 以下の例の動作手順
        1. actionタグによってurlファイルに書かれているname=voteのviewが参照されて、post待ち状態になる
        2. ラジオボタンがchoiceの数生成される
        3. ラジオボタンの横のテキストをlabelによって生成する
        4. submitボタンを生成する
        5. submitボタンが押されたらpost待ちのviewが発火する

```html
<form action="{% url 'polls:vote' question.id %}" method="post">
    {% csrf_token %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
    <input type="submit" value="Vote">
</form>
```

<br></br>

- POSTが成功したあとは、HttpResponseではなくてHttpResponseRedirectを返す必要がある
    - django固有ではなくて、web開発の基本

<br></br>

- 汎用ビューの主なクラス変数とメソッド
    - model変数
        - モデル(データベースのクラス)を格納すると、クラス名を小文字にしてqueryset変数としてhtml(template)内で使えるようになる
    - template_name変数
        - 表示したいhtml(template)のパスを格納する
        - model変数で定義したqueryset変数が、このhtml(template)内で使用可能になる
    - context_object_name変数
        - model変数で自動的に登録されたqueryset変数に独自の名前をつけることができる
    - get_querysetメソッド
        - model変数を小文字にしたqueryset変数に格納したいオブジェクト(queryset型)をreturnする

<br></br>

- DetailViewとListView
    - DetailViewでオブジェクトをリスト表示(全件またはページに収まる程度)
    - ListViewでリスト表示した内の一つを詳細表示する
    - DetailView->ListView という遷移を開発することになると思う
    - DetailViewとListViewの違いの一つとして、pkがDetailViewにある。
        - list表示された内の一つ一つにはpkというidが振られていて、DetailView内の変数に格納されている
    - https://www.nblog09.com/w/2019/05/04/django-list-detail/
    - デフォルトのget_querysetメソッドは、model変数が定義されていると、model変数のobjects.all()を返す挙動。

<br></br>

- querysetとcontextの違い
    - 一言で言うと、持っている情報量が違う
    - contextは辞書型、querysetはqueryset型(リストみたいな)
    - querysetはcontextの中にも含まれている
    - https://codor.co.jp/django/difference-context-and-queryset

```
context
{
'paginator': None,
'page_obj': None,
'is_paginated': False,
'object_list': <QuerySet [<AppModel: データ1つ目>, <AppModel: データ2つ目>, <AppModel: データ3つ目>]>,
'appmodel_list': <QuerySet [<AppModel: データ1つ目>, <AppModel: データ2 つ目>, <AppModel: データ3つ目>]>,
'view': <app.views.AppListView object at 0x7f157824ab00>
}
```

```
queryset
 <QuerySet [<AppModel: データ1つ目>, <AppModel: データ2つ目>, <AppModel: データ3つ目>]>
```

<br></br>

- get_querysetとget_context_dataとgetの使い分け
    - get_querysetでできなそう->get_context_dataでできなそう->getをカスタマイズ
    - https://teratail.com/questions/118626

<br></br>

- djangoでのディレクトリ構造の参考
    - 開発がしやすいように色々と分けたほうがいい
    - staticやtemplates内でもpollsのようにアプリケーション毎にディレクトリを分ける
    - 画像はimagesに格納

```
polls_project
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── static
    │   └── polls
    │       ├── images
    │       └── style.css
    ├── templates
    │   └── polls
    │       ├── detail.html
    │       ├── index.html
    │       └── results.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

<br></br>

- modelにデータを登録する際のobjects.createとobjects.saveの違い
    - どちらもデータを登録するメソッド
    - createの方は一行で登録することができる
    - saveはモデルをインスタンス化してsaveするという二行になる
    - https://www.366service.com/jp/qa/71aa47b9ef06fb11fd9d963e8aee8966

<br></br>

- settings.pyに書いてあるBASE_DIR
    - プロジェクトのルートディレクトリを表している
    - djangoがファイルを探すときには、BASE_DIRからの相対パスでアクセスしている
        - from importするときもBASE_DIRをルートとして行うのかな？？

<br></br>

- ページリンクのURLにパラメータをつける
    - 二種類のやり方を紹介する
        - htmlだけの場合は、?の後に「変数=値」とするだけ
        - djangoの場合は、「url urlconfigのpathのname 変数=値」とする
        - https://forum.samuraiz.co.jp/samu06/01.html
        - https://qiita.com/tatamyiwathy/items/244d1bf10e585569213c

```html
//htmlだけで実装する方法
<a href="detail.cfm?empid=101">社員Ａ</a><br>
<a href="detail.cfm?empid=102">社員Ｂ</a><br>
<a href="detail.cfm?empid=103">社員Ｃ</a><br>
<a href="detail.cfm?empid=104">社員Ｄ</a><br>
```

```html
//djangoとhtmlで実装する方法
<a href={% url 'detail_cfm' empid=101 %}>
<a href={% url 'detail_cfm' empid=102 %}>
<a href={% url 'detail_cfm' empid=103 %}>
<a href={% url 'detail_cfm' empid=104 %}>
```

```html
//実際の使用例

//python
app_name = blog
urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='post_detail'),
]

//html
<h2 class="title"><a href="{% url 'blog:post_detail' pk=post.pk %}">{{ post.title }}</a></h2>
```

<br></br>

- 常に表示させておきたい内容は、blockでカプセル化しないでbaseのhtmlにそのまま書く
    - 例えば、タイトルとナビゲーションはどこのページにとんでも表示させておきたいからbaseに書く
    - 分割してしまうと、拡張部分のhtmlが反映されなかった
        - なぜかというと、テンプレート拡張は、カプセル化したテンプレートにurlディスパッチャでアクセスがないと表示されないから

```html[page_hrader.html]
<h1 class="page-title">
    <a href="{% url 'blog:index' %}">Kosuke's Tech Blog</a>
</h1>
```

## python memo
- クラスオブジェクトとインスタンスオブジェクトとは
    - クラスオブジェクトは、クラスの定義が終わると生成されるもの
    -  インスタンスオブジェクトは、インスタンス化された時に生成されるもの
    - https://python.ms/instance-and-class/#疑問-インスタンスオブジェクトって具体的に何のこと

<br></br>

## その他色々 memo
- 静的ファイルとは
    - cssや画像ファイルといった動的な変更がされないファイルのこと
    - どのユーザでも同じものが使われることから静的と呼ばれている

<br></br>

- CSSセレクタ
    - cssでどの部分にレイアウトを適用するかを選択する時に使われる記法
        1. タグ名で判別する
        2. classやidで判別する
    - 例えば、bodyタグを指定したら、bodyで囲まれている要素全てにレイアウトを適用することができる。余白とか。

<br></br>

- webアプリにapiを実装する必要性
    1. 他のプログラムからwebアプリの機能を使いたい場合
        - ただ単にサイトにcurlでアクセスしてもhtmlが返ってくるだけ
            - json形式で機械学習の結果を返したりしたい
        - apiの例としてgoogleの翻訳アプリを自分のwebアプリに組み込みたい場合にgoogleのapiにアクセスする
    2. 異なるフレームワーク間の連携
        - 例として、djangoとreactを連携させるには、django rest frameworkを使う
            - https://qiita.com/__init__/items/f5a5a64a05541fcda713

<br></br>

- rest api(restful api)とは

# やったこと
1. 勉強手順
    - https://www.arimakaoru.com/blog/django-beginner-recommendation
2. 簡単なブログ作成(django girls)
3. 投票アプリ作成(django公式tutorial)

# やること
1. 技術ブログを作成(自分のポートフォリオを拡張してもいいかも)
    - markdown
    - 目次の自動生成(横に目次をつけてもいいかもしれない)
2. djangoのadminからブログに記事投稿
3. ユーザ認証やメール送信といった色々な機能を追加
    - https://docs.djangoproject.com/ja/3.1/topics/
4. djangoのブログにmarkdown機能を実装
    - https://blog.narito.ninja/detail/102
5. dockerやaws連携

# 参考文献
- https://tutorial.djangogirls.org/ja/