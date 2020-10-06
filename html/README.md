# webページの構成例
- webページはheader, footer, mainのように大きな枠組みに分けて開発していくことになる

![2020-10-06 22 29のイメージ](https://user-images.githubusercontent.com/53253817/95208343-e98ad700-0823-11eb-8e60-447ac2d40a45.jpeg)


- headerにはページのタイトルを配置する。(KOSUKE SHINAGAWA PORTOFOLIO の部分)
- footerにはサイトの情報を配置する。(コピーライトの部分)
- navにはサイト内で見たいページに一気に飛べるボタンの配置？ (works, feature, about, skill, contact の部分)
- mainでページの主要な部分を記述する
- articleで独立した記事を表す。sectionでセクションを表すことができる。

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

