# JavaScriptメモ

## JavaScriptを学ぶ順序
1. 生のJavaScriptでDOM操作を学ぶ
  - 文法は開発しながら学んでいけばいい
  - タブUIといった部品を作りながら学ぶ
  - DOMやEventなどを使って動的なwebサイトを作ってみる

2. jQueryを使って動的なwebサイトを作ってみる

3. フレームワークを使って開発をする(自分の好みに合わせて技術選定をする)
  - Angular
    - HTMLとJavaScript（TypeScript）を分割して書く
    - TypeScriptがデフォルト
    - AngularJSとは別物なので注意
  - React
    - JavaScriptの中にHTMLを書く
    - フレームワークではなく、ライブラリの位置付け
    - ルーティングをしたければルータを選んで追加し、HTTP通信をしたければHTTP通信用のライブラリを選定、というようにgolangみたいにマイクロフレームワークな側面がある
  - Vue
    - HTMLにJavaScriptを書く
    - SPA以外を作るならVue一択

---

<br></br>

## AjaxとSPAは何が違うのか
- Ajaxで非同期処理をしてwebページを作ることと、Reactなどを使ってSPAなWebページを作ることの違いがよくわからなかったことからこのような疑問が出てきた

### 従来のアプリケーション(静的コンテンツ)
- 従来のwebアプリケーションは全て同期的に行っていた
  - go言語だけやpythonだけで作ったアプリケーションはこの従来のアプリケーション

  ![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-152901-23c07c5c-6691-df86-b5d1-94e1f9fb0adf](https://user-images.githubusercontent.com/53253817/101347520-91c52680-38cd-11eb-93ab-c30dab3cb1fb.png)

### Ajax
#### Ajaxとは
- JavaScriptとXMLを使って非同期にサーバとの間の通信を行うこと
- Ajaxは一つの機能ではなくて、複数の技術を用いてAjaxという概念を実現しているイメージ
- ブラウザの挙動に頼らない（リンクを押したらリクエストして描画するとか）
  - クリックとかキー入力の挙動をJSで制御する
- 必要なデータはJSで取得しに行く
- 取得したデータをもとに、クライアント側の現在の状態を利用して今表示されている画面を変更する
#### Ajaxを実現するための技術
- XMLHttpRequest
  - ブラウザ上でサーバーとHTTP通信を行うためのAPI
  - URLを指定してバックエンドのサーバと通信する
- JavaScript
  - ブラウザで動く唯一の言語で、XMLHttpRequestが組み込みのオブジェクトとして提供されてる
- DOM
  - HTMLやXMLを「ツリー構造」として展開し、アプリケーション側に文章の情報を伝え、加工や変更をしやすくするもの
  - ツリー構造とは、データ構造の一つで、一つの要素(ノード)が複数の子要素を持ち、一つの子要素が複数の孫要素を持ち、という形で階層が深くなるほど枝分かれしていく構造のこと
- XML(JSON)
  - 文書やデータの意味や構造を記述するためのマークアップ言語の一つ
#### Ajaxの流れのまとめ
- Ajaxをフルスクラッチで実装するのは大変なので、後述するjQueryといったライブラリが誕生した

![2020-12-07 23 23のイメージ](https://user-images.githubusercontent.com/53253817/101362264-3b62e280-38e3-11eb-9868-ee345a7f4b96.jpeg)

### SPA
- webページの画面更新を全て非同期行うように作ったものがSPA
- jQueryだけで構築するのは技術的にはできるけど、大変すぎて現実的ではないからReactなどの仮想DOMという技術が使われる
- https://qiita.com/takanorip/items/82f0c70ebc81e9246c7a

### 参考文献
- https://qiita.com/sho0211/items/28faafcd1840c5948107

## jQueryはなぜ誕生したのか
### jQueryの功績
- 各ブラウザが提供しているDOMなどのAPIを一つのメソッドにまとめ、ブラウザ間の差異をなくした
- Web上でのアニメーションを簡単に記述できるようにした
- 現在のJavaScriptの非同期処理に欠かせないPromiseと似たDeferredという機能を取り入れた
- JavaScriptのfor文などを簡潔に書けるユーティリティの機能も存在
- jQueryの最大の功績はなんと言ってもAjaxを簡潔かつわかりやすく書けること
  - サーバー↔クライアント間の通信がページ転移を伴わないでもできるようになった
  - SPAの元となる
### 参考文献
- https://qiita.com/ygkn/items/eed01ae9c01339d6086a
