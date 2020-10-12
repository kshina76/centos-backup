# 簡単なブログ作成

##  django memo
- viewは「templateとmodelを繋ぐ架け橋」と「viewを生成する」機能を持つ
<br></br>
- 他のurlで何度も登場するhtmlの文はテンプレート拡張を使って、カプセル化みたいなことをする
<br></br>
- データベースの各レコードにはプライマリキー(pk)という連番の値が自動で割り当てられている。
    - urlのpath内に<int:pk>や<int:info_id>を書くと、pkやinfo_idという変数がviewに渡される
        - viewが関数ベースなら引数にpkのように指定しておけば使えるようになる
        - クラスベースなら、get_context_dataのkwargsに格納されている

```python
# ユーザがpost/2/edit/にアクセスしたらpk=2となってview内の関数(クラス)の引数になる
path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
```

- urlのpathでnameを指定しておくと、htmlのハイパーリンクでurlを待ち受けることができる

```python
path('post/new/', views.post_new, name='post_new')
```

```html
このハイパーリンクがクリックされたら、post_newというnameのviewを使って描画するという意味
<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
```

## 静的ファイルとは
- cssや画像ファイルといった動的な変更がされないファイルのこと
- どのユーザでも同じものが使われることから静的と呼ばれている

## CSSセレクタ
- cssでどの部分にレイアウトを適用するかを選択する時に使われる記法
    1. タグ名で判別する
    2. classやidで判別する
- 例えば、bodyタグを指定したら、bodyで囲まれている要素全てにレイアウトを適用することができる。余白とか。

# 参考文献
- https://tutorial.djangogirls.org/ja/