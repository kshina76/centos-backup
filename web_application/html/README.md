# webページの構成例
- webページはheader, footer, mainのように大きな枠組みに分けて開発していくことになる

![2020-10-06 22 29のイメージ](https://user-images.githubusercontent.com/53253817/95208343-e98ad700-0823-11eb-8e60-447ac2d40a45.jpeg)


- headerにはページのタイトルを配置する。(KOSUKE SHINAGAWA PORTOFOLIO の部分)
- footerにはサイトの情報を配置する。(コピーライトの部分)
- navにはサイト内で見たいページに一気に飛べるボタンの配置？ (works, feature, about, skill, contact の部分)
- mainでページの主要な部分を記述する
- articleで独立した記事を表す。sectionでセクションを表すことができる。

# webページを作成していく手順
1. header, navなどの構成を頭に入れながら、どこに何を配置するかをざっと一旦紙とかに書き出してみる
2. htmlファイルに文字コードなどの情報を記述していく
3. htmlファイルにmainやheaderなどの大きなタグはあらかじめ記述しておく
4. headerで題名や背景画像を適用する
5. navでcssのフレックスボックスなどを使って目次を作成する
6. mainでhtmlで文章などを書く->cssでデザイン->htmlで文章などを書く->...繰り返し
7. footerなど
8. レイアウトを検討していく
    - PCで見やすいマルチカラムといった部分
9. レスポンシブデザインを検討する
    - 端末の種類によって表示するスタイルシートを変更すること
    - メディアクエリ(htmlとcss両方に存在する)
    - ビューポート(スマホでも読みやすくする)
10. formを使って入力する部分を作成する
11. javascriptやpythonを使ってさらに高度なwebページへ
    - htmlのformを使って入力欄を作った後は、入力内容をPOSTできるような機能をdjangoなどで記述してあげる
        - https://noumenon-th.net/programming/2019/10/28/django-forms/

# タグ一覧
## id, class
- 要素に名前をつけることができる
- idは一つの要素に対して、classは複数の要素に同じクラス名を付けることで使える
- idにアクセスする方法は「#要素名」
- classにアクセスする方法は「.クラス名」

```html
<タグ id="id名"> </タグ>
<タグ class="同じclass名"></タグ>
<タグ class="同じclass名"></タグ>
```

## table, caption, tr, th, td
- 表を作ることができる
- colspan, rowspan属性を使うと、表を連結することもできる

## div, span
- mainをさらに細かく分類してブロックを作るために使われる
- このタグだけではレイアウトは変わらないが、cssでブロック毎にレイアウトを変更することができるようになる
- idタグやclassタグと一緒に使うことになる
- 使用例
    - https://github.com/kshina76/centos-backup/blob/master/html/04/Sample7.html

## link
- 外部のファイルを使用するときに使われる
- cssなどを使ってレイアウトを変更する際などに使われる

# cssの記法
- cssの記法はタグ名やidやclassを指定して、そのブロックに余白や色などを指定するだけ。簡単。

---

<br></br>

## まとめ
### 聖杯レイアウト
- これは絶対見た方がいい
- https://www.youtube.com/watch?v=XrFD_0Pr6Nc
### rem、em、%、pxの使い分け
#### 単位の説明
- emはフォントサイズを基準にする相対値を指定します。
- remはルートのフォントサイズを基準にする相対値を指定する
- %は、ボックスサイズを基準に相対指定したいところに。
- pxは何にも影響されずにガッチリとサイズを決めたい所に使います。
- https://qiita.com/masarufuruya/items/bb40d7e39f56e6c25f0d
#### 意見1
- font size : remで指定
- 文字の周りのmargin,padding : remで指定
- 画像や領域の幅など : %で指定
- https://teratail.com/questions/158874
#### 意見2
- 文字まわりはremかemを使うといいという意見
- 単位とかについてもわかりやすい記事だった
- https://haniwaman.com/percent-em/
#### 意見3
- ボックスの padding や margin : em/rem
- ボックスのサイズ指定（特に width） : %で指定
- borderの幅、サイトのメインボックスの幅を固定することもある : pxで指定
    - メディアクエリで切り替えをする
    - 親のボックスがパーセントで作られていたら、それに従って子のボックスも変更されるからpxでいいとかかな？
- http://honttoni.blog74.fc2.com/blog-entry-221.html?sp
#### 意見4
- font sizeはremだけにするとremで完結できるからremでいい
- https://www.web-ma.co.jp/column/css/1445.html
#### 意見5
- メディアクエリ → em
- font-size → em / rem
- borderなど常に見た目が変わらない → px
- それ以外 → em / rem
- https://note.com/takamoso/n/nde1275183086#41ojS
#### 闇雲なremはよくない
- font-sizeに関してはpxで指定していいのではないかという意見
- remを使うのにhtmlのfont-sizeを0.625で固定するのはダメ。デフォルトの値を使うこと
- https://to.camp/lesson?v=syr7IVIVoL7ZIoPVuHps
