# JavaScript メモ

## プログラムを書く手順
1. 作りたいものを考える
2. 機能を考える
3. 機能をさらに分割して、簡単に書ける粒度まで分割する
4. まずは簡単な処理を書いてみる
  - 例1: for文を回す前に、一つのデータだけに対して適用してみる
  - 例2: 関数化する前に処理を書いてみる
5. とにかく機能を満たすような動きをするコードを書く
  - ここでは綺麗かどうか、クラスをガチガチに定義するなどはしなくて良い
6. リファクタリング
  - 共通化をする
  - 関数化する
  - クラス化する
  - 関数を分解する(1処理1関数)
  - コメントを追加する

<br></br>

## オブジェクト指向で作成する方法
- 色々な「世界を定義」していって、「世界を組み合わせて」開発していく方法
- 例(twitter)
  - クラス
    - Userクラス
    - Tweetクラス
    - Profileクラス
    - Actionクラス
    - etc
  - 組み合わせ方
    - UserクラスがTweetクラスとActionクラスとProfileクラスを持っている
    - etc
- 組み合わせるだけなら関数でも実現できるが、「変数と関数」のかたまりである「クラス」を組み合わせることで、よりわかりやすいプログラムを作ることができる
- 組み合わせ方としては、プロパティに他のクラスのインスタンスを渡すといった方法などを取る

<br></br>

## ドキュメントの読み方
- 引数と返り値を見る

<br></br>

## JavaScript を使ったフロントエンド開発とは

- JavaScript を使用しない Web 開発
  - 新しいコンテンツをクリックする度にページ遷移
  - レスポンスが HTML
  - ページ全体がレンダリング
- JavaScript を使用する Web 開発
  - バックエンドの API サーバから json が返ってきたものを成形して表示するのがフロントエンドの役割
  - レスポンスが json
  - 必要なところだけを DOM 操作をして、レンダリングする

### フロントエンドにおけるJavaScriptの役割

- データのやり取り(json)
  - `window.fetch()`など
- DOM 操作
  - `document.getElementByID("foo")`など

### DOM 操作

- json にアクセスして、HTML に反映していくイメージ

```html
<li>
  <div>
    <img src="data[0].src" />
    <h1>data[0].name</h1>
    <p>data[0].body</p>
  </div>
</li>
```

```json
{
  "data": [
    {
      "name": "web開発",
      "body": "JSを学びました",
      "src": "https://example.com"
    }
  ]
}
```

### オブジェクトの作り方

- オブジェクト
  - データと機能をまとめたもの
- プロパティ
  - オブジェクト内のデータに相当
- メソッド
  - オブジェクト内の機能に相当

```js
let shimabu = {
  name: "しまぶー", //プロパティ
  techProgramming: function () {}, //メソッド
};
```

```js
//ドットを用いたアクセス(こっちがよく使われる)
console.log(shimabu.name);
console.log(shimabu.techProgramming());

//角括弧を用いたアクセス
console.log(shimabu["name"]);
console.log(shimabu["techProgramming"]());
```

### Window, Document

- JavaScript はブラウザで動く言語で、ブラウザ自体もオブジェクトで定義されていることから、ブラウザのオブジェクトのプロパティやメソッドに定義することができる
  - 例えば Window オブジェクトや Document オブジェクトなどに JavaScript からアクセスをして、色々な操作を実現する
  - `window.console.log()`や`window.documents.getElementByID()`など全てwindowオブジェクトに定義されている(これに関しては感動した)

- Windowオブジェクト
  - Windowは省略可能
  - Windowオブジェクトの中に`console.log()`や`document.getElementByID()`や`button.addEventListener`などがプロパティとして定義されている
    - つまりブラウザのwebサイトに表示される「部品」を表している
    - windowオブジェクトに対して`addEventListener`を適応するとウィンドウ自体を再読み込みしたりできる
  - Windowオブジェクトを使うと、ブラウザをリロードさせたり、ブラウザの大きさを取得したり、ブラウザに関することもなんでもできる

  ![2021-04-12 19 24のイメージ](https://user-images.githubusercontent.com/53253817/114380626-3da4b880-9bc5-11eb-892b-e3d2cb97e2d7.jpg)

- DOM操作
  - DOM要素(=HTML)の`id='foo'`の要素を取得する

  ```js
  document.getElementByID('foo');
  ```

### ブラウザ上のJavaScriptからAPIを叩く方法
- `window.fetch()`を使う

```js
//async awaitを使った書き方
async function callApi() {
  const res = await fetch("https://example.com");  //awaitをつけないとpromiseオブジェクトが返ってくる
  const users = await res.json();
  console.log(users);
}

callApi();
```

```js
//async thenを使った書き方
function callApi() {
  fetch("https://exmaple.com")
    .then(function (res) {
      return res.json()
    })
    .then(function (users) {
      console.log(users)
    })
}

callApi();
```

```js
//XMLHttpRequestを使った書き方
function callApi(){
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "https://example.com");
  xhr.responseType = "json";
  xhr.send();
  xhr.onload = function () {
    console.log(xhr.response);
  };
}

callApi();
```

### 色々やってみる

- ボタンクリック、APIアクセス、DOM操作

  ```js
  const button = document.getElementByID("addBtn");
  const lists = document.getElementByID("lists");

  //ボタンクリックイベントを取得
  button.addEventListener("click", async () => {
    //データのやりとり
    const res = await fetch("https://example.com");
    const users = await res.json();

    //DOM操作
    const list = document.createElement("li");  //リスト要素「<li></li>」を作成
    list.innerText = "foo";  //「<li>foo</li>」を作成
    lists.appendChild(list);
  })
  ```

<br></br>

## 高階関数
- 関数を返す関数を定義すること

```js
//高階関数
const f = (x) => {
  (y) => x * y;
}
console.log(f(3)(2))  //6

//省略記法
const f = x => y => x * y
console.log(f(3)(2)) //6
```

<br></br>

## 非同期処理
- 非同期処理の手順
  - fetch-APIで、APIコール
    - その返答を待ってしまうと時間がかかってしまうから、Promiseオブジェクトを渡して、その間に違う処理を走らせる
  - APIコールの処理はサーバ側で処理をして、その間ブラウザ側は先の処理を進める
  - APIコールの処理が終わって値が確定したら、fetch-APIのところに戻る
- 非同期処理を考える時のポイントは、依存関係を明確にすること
  - 例: 処理Aは、処理Bと処理Cが終わっていないといけないから、処理Bと処理CをPromiseをして、thenに処理Aを記述しよう！
    - Promise.allを使う
- よくライブラリの関数で、引数に関数を渡しているものがあるが、それは非同期処理をしているということ。そして引数に渡される関数がコールバック関数という。

### コールバック関数とは
- [ここを参考にする](https://www.youtube.com/watch?v=HhoUmOEAqTI)
- `addEventListner("click", function())`のように、「クリックを待っててね！ クリックされたら`function`を実行するね！ クリックされるまで他の処理しているね！」というように、「〜したら...してね。それまで~~してるね！」というようなものをコールバック関数という
  - プログラム上でaddEventListnerを定義しても、クリックされるまでfunctionは実行されずに、その先の処理をしている。いわゆる非同期処理

### クロージャと用途
- [ここを参考に](https://www.youtube.com/watch?v=1akMrht6I7A&t=7s)
- クロージャとは、関数の中に変数と関数が定義されている空間のこと

  ```js
  function func(引数1) {
    const val = 引数1;
    return function func2() {
      if(val < 0) {
        return -1 * val
      }
    }
  }
  ```

- クロージャを使うことで、コールバック関数を渡さないといけないライブラリをカスタマイズすることができる
  - addEventListnerなどのように、決まった形の引数と返り値を持った、コールバック関数を引数に渡さなければいけないものでも、`val1`のように色々な引数を追加して渡せることで、柔軟性のあるコールバック関数を作成することができる

  ```js
  function func(val1) {
    return function func2(val2) {
      if(val1 < val2) {
        return -1 * val1
      }else{
        return val2
      }
    }
  }
  addEventListner(~,~)
  ```

### Promiseとは
- 未来のまだ確定していない値の状態を表すオブジェクト
  - 本当はめちゃくちゃ時間がかかる処理でも、呼び出すとすぐにPromiseのオブジェクトを返す
  - 引換券みたいなもの
- Promiseオブジェクトの値は、いつ確定するかわからない
- Promiseオブジェクトには値が確定したときに行って欲しい処理(関数)を登録できる
  - この関数は、コールバック関数という
  - 値が確定したら、コールバック関数が呼び出される
- Promiseを返す関数は、非同期用の関数ということ
  - APIコールするfetch関数とか
  - 「ファイルを参照したり」、「ストレージに保存したり」といった関数とか

- thenは「これが終わったら、こうする」というもの
  - 以下の例だと、「fetch関数の処理が終わったら、thenの中身のコールバック関数を呼び出す」というもの
  - Promiseオブジェクトの値が確定したら、コールバック関数に引数を渡して呼び出される

  ```js
  const result = fetch("https://example.com");
  //ここのアロー関数がコールバック関数
  result.then(res => {
    console.log(res);
  });
  ```

- thenチェイン
  - then自体もPromiseオブジェクトを返す
  - 上から順番に待たないで非同期で実行されるが、表示される順番は守られる
  - `catch`はthenのどこかでエラーが起きたときに、他のthenをすっ飛ばして、catch内の処理に遷移してくれる

  ```js
  sleep(1000)
  .then(() => console.log('1'))
  .then(() => sleep(1000))
  .then(() => console.log('2'))
  .then(() => sleep(1000))
  .then(() => console.log('3'))
  .then(() => sleep(1000))
  .catch((e) => {
    console.log(e)
  })
  ```

- プロミス化
  - Promise型を返してくれないような古いライブラリに対して、Promiseを返すようにすること
  - 引数にコールバック関数を渡すような関数があったら、練習でプロミス化しても良いかも

  ```js
  //プロミス化
  function takeLongTimeFunction() {
    return new Promise((resolve, reject) => {  //rejectは、非同期処理が失敗したときにエラーを投げてくれる
      //ここに非同期処理したいものを書く(時間のかかる処理)
      setTimeout(function() {
        resolve('成功')  //resolveの引数(成功)が、thenのコールバック関数の引数(res)になる
        //reject(new Error('失敗'))
      }, 1000);
    });
  };

  //プロミス化されていることを確認
  takeLongTimeFunction()
  .then((res) => console.log(res));
  ```

- Promise.all
  - 複数のPromiseを扱いたいときに使用する
    - 「処理Aは、処理Bと処理Cが終わっていないといけないから、処理Bと処理CをPromiseをして、thenに処理Aを記述しよう！」のような時
  - 同時並行で進められる処理は、Promise.allで並行につなぐ
  - 依存関係があって、順番に進めるべき処理はthenで直列につなぐ

  ```js
  const fetchUsers = fetch("https://example.users.com");
  const fetchBooks = fetch("https://example.books.com");
  Promise.all([fetchUsers, fetchBooks])
  .then(([res1, res2]) => {
    console.log(res1);
    console.log(res2);
  })
  ```

### async/await
- asyncとは
  - async functionは呼び出されるとPromiseを返す。
  - async functionが値をreturnした場合、Promiseは戻り値をresolveする。
  - async functionが例外や何らかの値をthrowした場合はその値をrejectする。
- awaitとは
  - awaitを指定した関数のPromiseの結果が返されるまで、async function内の処理を一時停止する。
  - 結果が返されたらasync function内の処理を再開する。
  - awaitをつけることで、Promiseが確定することを保証するといったイメージ。
- 使い方
  - 非同期処理を伴う関数定義にasyncをつける
  - 非同期処理を伴う関数実行時にawaitをつける
  - awaitはasync付き関数内でしか使えない
- [ここを参考にした](https://qiita.com/soarflat/items/1a9613e023200bbebcb3)

```js
const getUserName = async () => {
  //awaitはfetchだけではなくて、「fetch().then().catch()」全体にかかっている
  const result = await fetch('https://example.com')
    .then(res => {
      console.log('非同期処理が成功した');
      return res.json
    })
    .catch(e => {
      console.log('非同期処理が失敗した');
      return null
    });
  
  //awaitの関数が終わるまで、ここは処理されない
  console.log('awaitが終わった後だよ');
}
```

```js
//以下のように書くこともできる
const getUserName = async () => {
  const result = await fetch('https://example.com');
  const res = await result.json();
}
```

<br></br>

## export関連
- [CommonJSのexportsの種類](https://qiita.com/senou/items/a2f7a0f717d8aadabbf7)
- [Node.jsのexportsの種類](https://www.webdesignleaves.com/pr/jquery/node-js-module-exports.html)

### 「named exports」と「exports」
- `named exports`はCommonJS、`exports`はNode.jsでの書き方で、処理は同じ
- どちらも、外部のファイルから参照できるようにする

```js
// named exports

// user.js
export const getName = () => {
  return 'Foo';
};

// main.js
import {getName} from 'user';  // pathを指定
console.log(getName());
```

```js
// exports

// user.js
const getName = () => {
  return 'Foo';
};
exports.getName = getName;  // 外部参照できるように設定している

// main.js
import {getName} from 'user';
console.log(getName())
```

### 「default exports」と「module.exports」
- ファイルに一つの関数やクラスしか定義されていない場合、ファイルごとimportするような使い方をするexport
- あまり使わない方が良さそう
