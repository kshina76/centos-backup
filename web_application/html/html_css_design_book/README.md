# HTML&CSSとWebデザイン　書籍memo

## HTML

- タグと属性
    - タグは、html,head,a,pのようなもの
    - 属性は以下の例のようなもの

```html
//属性は、タグに付加情報を付けたいときにスペース区切りで渡すもの。例えば、のようにaでリンクを張って、どこに飛ばすかをhrefで指定する
<a href="about.html">title</a>
```


<br></br>

- 見出しタグ(h)
    - h1タグはwebページにつき一つ
    - 数字の順番に使うべし
        - 文字の大きさがちょうどいいからといって、h2から使うのはよくない
    - 筆者は、右上の小さいロゴの横の文字にh1で、メインタイトルにh2を振っていた

```html
<h1>rogo</h1>
<h2>title</h2>
```

<br></br>

- 段落タグ(p)
    - pタグで挟んだ文章が段落になる

```html
<p>こんにちは、ここはhtmlのメモとして私が残しているものです</p>
<p>ここに書かれているものは主に、本で勉強した内容を要約しているので、もしよかったら使ってください</p>
```

<br></br>

- 画像表示タグ(img)
    - src属性
        - 画像が置いてあるパスを指定
    - alt属性
        - 画像が読み込めなかった時に表示する文章
    - 終了タグがない(インラインというのかな？)

```html
<img src="about/test.jpg" alt="test">
```

<br></br>

- リンクタグ(a)
    - href属性
        - リンク先のurlを指定。
        - メールアドレスを指定すると、メールを作成する画面に飛ばせる。
    - target属性
        - _blankを指定するとリンクを踏んだときに別タブで開くようになる
    - aタグでimgタグを囲むと画像にリンクを貼ることができる

```html
//画像にリンクを貼る
<a href="about.html"><img src="about.img" alt="about"></a>
```

<br></br>

- 箇条書きリストタグ(ul,ol,li)
    - 箇条書きの項目をそれぞれliタグで囲んで、全体をulタグで囲む
    - 番号付きなら全体をolで囲む

```html
<ul>
    <li>箇条書き1</li>
    <li>箇条書き2</li>
    <li>箇条書き3</li>
</ul>
```

<br></br>

- 表作成タグ(table,tr,th,td)

<br></br>

- フォームの作成(form,input)
    - 名前の入力欄やラジオボタンなどを作成
    - inputタグでラジオボタンやチェックボックスなどを指定して、formタグで囲む
    - radioなどはnameでグルーピングする
    - ボタンの横のテキストは本来labelタグを使うべし
    - 他にも色々あるので要調査

```html
<form action="sample.php" method="post" name="form-sample">
    <input type="text">
    <input type="radio" name="color" value="red"> 赤
    <input type="radio" name="color" value="blue">青
</form>
```

<br></br>

- グループ分けタグ(header,nav,article,section,main,aside,footer,div)
    - header
        - ページタイトルやナビゲーションメニュー
    - nav
        - メインのナビゲーションメニューを囲む。メイン以外のナビゲーションでは使われない。
        - headerタグの中に含まれることが多い。
        - メインタイトルの右上とか下にデザインされることが多いかな。
    - article
        - ブログの記事の部分などに使われる
    - section
        - テーマを持ったグループを作る
    - main
        - ページのメインコンテンツの全体を囲む
    - aside
        - プロフィールとかの補足情報を囲む
    - footer
        - ページ下部のコピーライトとか
    - div
        - cssを使ったデザインのためだけにグルーピングしたい場合に使われる
        - 上に記述したタグでうまくグルーピング出来なかった場合にも使う

<br></br>

## CSS

- 文字のサイズを変更する
    - remや%やpxという単位を使う
    - 適切な文字サイズは14px~18px
        - 文字サイズのバリエーションは2~5種類に収める

```css
h1 {
    font-size: 100%;
}
```

<br></br>
- フォントの種類を変える(font-family)
    - 日本語のフォント名はブラウザによっては認識できないので、カンマ区切りで英語名も書く
    - google fontというウェブで公開されているものもある

- 適切なフォントの種類
    - トリッキーなフォントはメインのタイトルだけ
    - フォントのバリエーションは1~3種類
    - 文字の太さは数値ではなくてnormalやboldで指定する
    - 長文には太文字は使わない
    

```css
h1 {
    font-family: serif;
}
h2 {
    font-family: "ヒラギノ丸ゴ Pro W4", "Hiragino Maru Gothic Pro", sans-serif;
}
```

<br></br>

- 文字のジャンプ率
    - 見出しと本文の文字サイズの差のこと
    - ジャンプ率が高いと楽しい雰囲気、低いと上品で落ち着いた雰囲気になる


<br></br>

- 行間の幅を変更(line-height)
    - 綺麗に見える数値は1.5~1.9の間
    - 詰めすぎると窮屈な印象になってしまう
    - 単位は無しで指定されるのが好まれる

```css
p {
    line-height: 1.7;
}
```

<br></br>

- 文章を揃える(text-align)
    - justifyを指定すると両端が揃えられる
    - centerで中央揃えができるが、2,3行の分には使うのはアリだが、長文には使わない。それかメインタイトルに使う。

```css
p {
    text-align: justify;
}

h1 {
    text-align: center;
}
```

<br></br>

- 色の指定(color,background-color)
- colorプロパティは文字に対して。back ground-colorは背景色
    1. カラーコードで指定
    2. RGBで指定
        - カラーピッカーで調べられる
        - rgb(0,0,0)のように指定
        - rgba(0,0,0,.5)とすると透明度も含める
    3. 色の名前で指定
        - pink,tomato,orange,gold,plum,tanを筆者はよく使うらしい

```css

```

<br></br>

- 配色やデザイン例がP106~121に書かれている

<br></br>

- 背景に画像を指定する(background-image)
    - P122~129
        -背景画像のフリー素材も書かれている

<br></br>

- フォントや背景や画像の大きさをデバイスによって変える
    - widthとheightの単位をvw,vhにする
    - デバイスの大きさによって変わるレスポンシブなサイトを作れる
    - 可変調を相対単位といい、pxで指定するのは絶対単位という

<br></br>

- 余白の調整(margin,padding)
    - marginは要素のまわりに余白を与える
        - margin-top,margin-leftのように四隅を指定できる。時計回りで指定するとmarginだけで四隅を指定できる。paddingも同じ
    - paddingは要素の端とテキストの間に余白を与える

<br></br>

- 要素のまわりに線を引く(border)
    - border-widthで線の太さ
    - border-styleで線の種類
    - border-colorで線の色
    - borderでwidthとstyleとcolorを一気に決めれる
        - border-bottomで下線を引けてwidthとstyleとcolor全ても決めれる。右ならborder-right
            - 白背景にはグレーの下線がいいかも。または、アクセントとしてオレンジを入れるとか。

<br></br>

- リストの装飾(list-style-type,list-style-position など)
    - P144~146

<br></br>

- idとclass指定方法
    - P147~151

<br></br>

- FlexboxとCSSグリッド
    - 要素を横並びにしたり、グリッド配置にするという複雑な形を簡単に実装する方法
    - P152~165
    チートシートがP165にある

<br></br>

- CSSリセット
    - P167~169

<br></br>

## memo
- リンクの下線を消す
    - cssでtext-decorationをnoneに設定

```css
a {
    text-decoration: none;
}
```

<br></br>

- タイトルの背景色の周りの余白を無くす
    - headerとbodyのmarginを0にする必要がある
        - headerだけmarginを0にしてもbodyのmarginが残っているから、完璧には余白を消せない

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

- リストの・を無くす方法

```css
ul {
  list-style: none;
}
```

<br></br>

- cssセレクタで一部分にスタイルを適応できなかったら、「tag1 tag2 *」のように最後にアスタリスクをつけると行けると思う

## その他
- webとインターネットとプロトコルの違い
    - インターネットは世界中のコンピュータが相互に通信できるように構築された道路(ネットワーク)のこと
    - Webとはhttpを使ってテキストや画像を送受信する仕組みのこと。インターネットを使って何かする事のうちの一つ。smtpを使ったメールなどのように、他のものはwebとは言わない。
    - プロトコルはインターネットを使って何かをするときのルール(メールはsmtp、ハイパーテキストはhttp、IPはインターネットそのものを使う時のルール)


## 気づいたこと
- htmlとcssの作成手順
    -以下のようにブロック毎にhtmlとcssを完成させていくイメージ
    1. headerのhtml->css
    2. コンテンツのhtml->css
