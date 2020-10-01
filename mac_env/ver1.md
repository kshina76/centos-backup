
# 基本的なMac環境構築  

## 1.homebrewをインストールする
https://brew.sh/index_ja

## 2.シェルをzshに変更する
```zsh
$ chsh -s /bin/zsh
```

https://qiita.com/kinchiki/items/57e9391128d07819c321

## 3.terminalのテーマを変更する
- icebergのテーマを適用する
    - https://qiita.com/kinchiki/items/57e9391128d07819c321

## 4.vscodeのインストール
- 公式からmac用をインストールするだけ

- 日本語化ができるけど、エラーでつまづいた時に検索することを考えて英語のままにしておく

- キーバインドは以下で確認(macだとctrl->cmd で考えないとだめ)
    - https://b1tblog.com/2019/10/16/vscode-shortcut/

- codeコマンドを使うことでコマンドからファイルを起動することができる
    - https://qiita.com/1natsu172/items/b951aa33451dad36bd7c

# JavaScript,html,css関連の環境構築
- エディタはvscodeを使うので、とくに困ることはないと思う

## 1.nodebrewのインストールと設定(PATHを通すところまで)
https://code-graffiti.com/how-to-install-node-js-on-mac-with-homebrew/

## 2.express.jsのインストール
- expressをインストール
```zsh
$ mkdir project
$ cd project
$ npm init
$ npm install --save express
```

- express-generatorで雛形を作って、チュートリアルをこなす
    - package.json（requirments.txtと同じ感じ）があると、npm installをするだけで、依存パッケージをインストールしてくれる
    - npm startコマンドは、package.jsonのscriptsのstartに書いてある文字列が実行される。初期だとnode ./bin/wwwが実行される
```zsh
$ npm install -g express-generator 
$ express tutorial
$ cd tutorial
$ npm install
$ npm start
```

## 3.reactのローカルインストール
- 公式に書いてあるnpxを用いたローカルインストールの方法で導入する
    - ネットにはグローバルインストールの方法が多く紹介されているが、環境を汚してしまうので、ローカルで行う
    - npxは、ローカルインストールされたモジュールにPATHを通さなくても実行できるようになるコマンド
    - https://dev.classmethod.jp/articles/node-npm-npx-getting-started/
    - https://www.tmotoki.net/tag/npx/

```zsh
//本来はnpmでローカルインストールしてからnpxをやるみたいだが、npxをいきなりやってもローカルインストールされてから実行されるので問題ない
$ mkdir tutorial
$ cd tutorial
$ npx create-react-app [project名]
```

- npx時にエラーが出た場合は以下を参考にする
    - https://yoshitaku-jp.hatenablog.com/entry/2019/02/12/163000

## 4.html
- htmlをnode.jsを使って表示する
    - https://www.i-ryo.com/entry/2020/03/12/080032

# pythonの開発環境
## pyenvのインストール
## pipenvのインストール
https://qiita.com/Kai-Suzuki/items/80f58267efde8daccfc3
https://qiita.com/TheHiro/items/88d885ef6a4d25ec3020


# あると便利なもの
## treeコマンド
```zsh
$ brew install tree
```

# vscodeでmarkdownを使う方法
- ファイル形式はmdで保存
- cmd-shift-V でmdファイルのプレビューができる
