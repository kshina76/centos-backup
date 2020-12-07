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

## Ajax、XMLHttpRequest、jQuery、FetchAPI、SPAまとめ

### 従来のアプリケーション(静的コンテンツ)
- 従来のwebアプリケーションは全て同期的に行っていた
  - go言語だけやpythonだけで作ったアプリケーションはこの従来のアプリケーション

  ![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-152901-23c07c5c-6691-df86-b5d1-94e1f9fb0adf](https://user-images.githubusercontent.com/53253817/101347520-91c52680-38cd-11eb-93ab-c30dab3cb1fb.png)

<br></br>

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

#### 参考文献
- https://qiita.com/hisamura333/items/e3ea6ae549eb09b7efb9

<br></br>

### jQuery
- VueやAngularやReactを使うとDOMの直接操作は推奨されないので、jQueryはAjaxのためだけに使うことが多くなる
#### jQueryがなぜ誕生したのか 
- 一番はAjaxのAPIを提供して、Ajaxを簡潔かつわかりやすく書けるようにしたこと
#### jQueryの功績
- 各ブラウザが提供しているDOMなどのAPIを一つのメソッドにまとめ、ブラウザ間の差異をなくした
- Web上でのアニメーションを簡単に記述できるようにした
- 現在のJavaScriptの非同期処理に欠かせないPromiseと似たDeferredという機能を取り入れた
- JavaScriptのfor文などを簡潔に書けるユーティリティの機能も存在
- jQueryの最大の功績はなんと言ってもAjaxを簡潔かつわかりやすく書けること
  - サーバー↔クライアント間の通信がページ転移を伴わないでもできるようになった
  - SPAの元となる
#### 参考文献
- https://qiita.com/ygkn/items/eed01ae9c01339d6086a


<br></br>

### FetchAPI
#### FetchAPIとは
- JavaScript標準でjQueryのAjaxAPIのようにわかりやすいコードで直感的に非同期通信を利用できるように策定されたのがFetchAPI
- 要はライブラリに頼らないで、標準でAjaxをわかりやすく実現しようということ
#### 参考文献
- https://launchcart.jp/blog/xmlhttprequestajaxとfetch-apiの使い方を比較してみる/
<br></br>

### XMLHttpRequestとFetchAPIのコード比較
- 上がXMLHttpRequestで、下がFetchAPI
- FetchAPIの方がまとまっていてわかりやすいかも

```javascript
// APIの呼び出し
var xhr = new XMLHttpRequest();

// 通信が成功したとき
xhr.addEventListener('load', function () {
  var data = JSON.parse(xhr.response);
  console.log(data);
});

// 通信が失敗したとき
xhr.addEventListener('error', function () {
  console.error(xhr.response);
});

// 通信の設定
xhr.open('POST', 'api.json'); // リクエストの初期化
xhr.setRequestHeader('Content-Type', 'application/json charset=utf-8'); // 通信オプション（例としてheaderのContent-Type）の設定

// 通信の開始
xhr.send(JSON.stringify({"hoge": "fuga"}));
```

```javascript
// Fetch APIの実行
fetch('api.json', {
  headers: {
    'Content-Type': 'pplication/json; charset=utf-8'
  },
  body: JSON.stringify({"hoge": "fuga"})
})

  // 通信が成功したとき
  .then(function(response) {
    return response.json();
  })
  .then(function(json) {
    console.log(json);
  })

  // 通信が失敗したとき
  .catch(function(error) {
    console.error('Error:', error);
  });
```

<br></br>

### 脱jQuery
- AngularJSやVue.jsでは、DOMの直接操作は推奨されないからjQueryはAjaxでしか使わなくなるので、AjaxはAjax専用のライブラリにまかせてしまって、jQuery依存を外したくなる
- HTTP通信のためだけにjQueryは嫌だ
#### Ajax専用ライブラリ
- axios
  - 一番簡潔に記述できるライブラリ
- SuperAgent
  - axiosより機能が多い
- FetchAPI
  - IE11には対応していないが、今後はこれが良さそう
  - JavaScript標準なので外部ライブラリではないのかな？
#### 参考文献
- https://qiita.com/katsuyuki/items/e2979de137255a573979
- https://qiita.com/hashrock/items/3113690bb3de5bba639b
<br></br>

### SPA
- webページの画面更新を全て非同期行うように作ったものがSPA
- jQueryだけで構築するのは技術的にはできるけど、大変すぎて現実的ではないからReactなどの仮想DOMという技術が使われる
- https://qiita.com/takanorip/items/82f0c70ebc81e9246c7a

#### 参考文献
- https://qiita.com/sho0211/items/28faafcd1840c5948107


---

<br></br>

## JavaScriptの同期・非同期まとめ
### どれが同期処理でどれが非同期処理なのか
- JavaScriptは提供されているオブジェクトによって同期だったり非同期だったりする
  - goとかだとgo routineで明示的に行うけど、JavaScriptだと暗黙的なんだな
- 基本的に時間がかかる処理や、外部と連携する処理は非同期で実装されている
#### 非同期処理のカテゴリ
- HTTPリクエスト系 (XHR, fetch, ajax)
- アニメーション系
- イベント系 (DOM Events)
- タイマー系 (setTimeout, setInterval)
#### 参考文献
- https://teratail.com/questions/175371

<br></br>

### JavaScriptには3+1つの非同期処理がある
#### コールバック
- 処理が終わったら指定した関数が呼ばれる、原始的な方法
- 複数のコールバック関数の処理が走ったら、先に終わったほうが実行される
- コールバックの問題点
  - 複数の非同期処理を順に実行する場合、ネストされまくってコールバック地獄に陥る
  - 複数の非同期処理を並列に実行して完了を待ち合わせるのは難しい
  - コールバック関数は呼び出し元の関数が終了してから実行されるため、コールバック内から例外を投げても呼び出し元の関数では捕捉できない
#### Promise
- コールバックの3つの問題点を解決するためにできた仕様
- Promise.all()
  - promiseにまとめた非同期処理全てが完了された段階でコールバックされる仕組み
  - 非同期処理を並列で実行させたいときに使う
- sequenceTasksメソッド
  - 非同期処理を逐次処理(直列処理)で実行するもの
    - 逐次処理はAという処理がどんなに遅くてもA,Bの順番で処理が行われるということ
  - 引数にpromiseオブジェクトを渡す
- Generator
  - これも非同期処理の逐次処理(直列処理)を実現するもの
  - 任意の時点で処理を止めてそこから再開することができるため、非同期の処理をいったん止めて、コールバックが終了したら再開するという処理をすることで、直列処理を実現できる
- ES6とES5
  - ES6に対応している環境ではデフォルトで使うことができる
  - ES5までしか対応していない環境で使う場合はbluebirdなどのライブラリが必要
- promiseを使うときのパターン
  - 基本は全てPromiseでくるむ。
  - 並列処理はPromise.allでまとめて処理できる。
  - 直列処理はPromiseをさらにGeneratorとcoで包むと、すっきり書ける。
#### async/await
- Promiseをさらに簡単に書けるようにしたシンタックスシュガー
  - シンタックスシュガーとは、長かったり複雑だったりする構文をわかりやすい構文に置き換えること
- https://qiita.com/SotaSuzuki/items/f23199e864cba47455ce
#### deferred(番外編)
- jQueryを使ってPromiseのような動作をさせるものがdeferred
#### 参考文献
- https://knowledge.sakura.ad.jp/24888/
- https://qiita.com/YoshikiNakamura/items/732ded26c85a7f771a27
- https://qiita.com/kiyodori/items/da434d169755cbb20447
- https://qiita.com/toshihirock/items/e49b66f8685a8510bd76
- http://beck23.hatenablog.com/entry/2014/11/08/022842
