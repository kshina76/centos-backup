# 自作技術ブログ

## 作成手順
1. ワイヤーフレームの作成
<br></br>

2. djangoの初期設定を終わらせる
    - adminはあとでいいかな？？
<br></br>

3. model(データベースの作成)
    - データベースのフィールドをいったん決める
    - 開発用に二つほどコンソールから記事をデータベースに挿入
<br></br>

4. htmlを書き始める(cssはhtmlがある程度出来上がってからでいい)
    1. header
        - 一番上のタイトル部分
            - ホームに飛ばせるようにタイトルにリンクを貼る(index.htmlに飛ばす。indexの実体は、base.htmlを継承したpost_list.html)
        - nav
            - ナビゲーション
                - home, profile, blog というナビゲーションを作成する
    2. main
        - 最近の記事を並べるところ
    3. 
<br></br>

5. htmlに合わせてdjango関連のところを開発
<br></br>

6. ある程度のところでcssでデザイン

## 気づいたこと
- ブログのホームに飛ばすときは、indexに飛ばす
    - htmlの名前はindexである必要はないけど、urlconfigのnameでindexにしておくとわかりやすいかも

<br></br>

- djangoではずっと表示が変わらない部分をbaseにして、表示が変わるページをblockタグでカプセル化していくイメージ

<br></br>

- タイトルの背景色の周りの余白を無くす
    - headerとbodyのmarginを0にする必要がある
        - headerだけmarginを0にしてもbodyのmarginが残っているから、完璧には余白を消せない
    - safariにおいて、bodyのpaddingは0にしなくてもデフォルトで0だから関係ないが、ブラウザによって違うので0に設定しておく
        - リセットCSSを使うとブラウザ毎の実装を考えなくてもいいかもしれないから要調査

```css
body {
    margin: 0px;
    padding: 0px;
}

.page-title {
    background-color: #041E32;
    margin: 0px;
    padding: 20px;
}
```

<br></br>

- djangoにmarkdownを実装する場合は、adminサイトからブログを書くときにmarkdownで書くことになる
    - デフォルトだとhtmlで記述することになる
    - 以下を参考にして実装した
        - https://zerofromlight.com/blogs/detail/52/
        - 画像をドラックアンドドロップで投稿できるようにするにはメディアファイルの設定が必要

## やること
- 以下のサイトがdjangoでブログを作っていてわかりやすい
    - https://medium.com/@kjmczk/blogsite-django-747046b453f9
- modelの見直し
    - tag
    - category
- サイドバーを実装
    - search, tag, profile, recently
- ページネーション実装
    - 下にある1,2,3,,,100 といったページを遷移できるやつ
- 詳細なプロフィールページの作成
- markdownにメディアファイルを実装
- post_listでカテゴリとtagの表示（データベースにcatとtagを追加しないとダメ）
- 記事のリスト表示の時に表示する本文の量に制限をかける
- データベースの種類を変更
    - PostgreSQLがいいかも

## やったこと
- markdown実装