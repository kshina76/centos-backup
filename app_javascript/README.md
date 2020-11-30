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
