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
