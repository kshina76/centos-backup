# vscodeの設定まとめ

## vscodeでまず設定すること
- 最低限の初期設定
    - https://yumegori.com/vscode-initial-setting20191022
- おすすめプラグインとtips
    - https://qiita.com/sensuikan1973/items/74cf5383c02dbcd82234
- フォルダーなどのアイコンを変更(setiが個人的に見やすい)
    - https://marketplace.visualstudio.com/items?itemName=qinjia.seti-icons
- go言語のフォーマッターやタブの設定(基本2tabにして、goの時に4tabにする設定)
    - https://casualdevelopers.com/tech-tips/how-to-setup-vscode-with-golang/
- ファイルツリーを見やすくする
    - https://qiita.com/toriiico/items/3070bac14946168be1ce

## VSCodeでmarkdownを書くときにやること
- [ここを参考](https://qiita.com/tomokin966/items/7731a6337670f5de2342)

## setting.json
- ツリーのインデントを深くする
    - `"workbench.tree.indent": 20`

## 入れるプラグイン(ローカル)
- Japanese Language Pack
    - 日本語化
- seti-icons
    - アイコンのテーマ
- drawio integration
    - drawioをvscodeで書ける
- plant uml
    - umlをvscodeで書ける
- Remote Containers
    - dockerの環境をvscodeで使えるようにするもの
    - これがないとdockerで構築した環境で自動補完などを使えない
    - コンテナの中でのvscodeのプラグインはローカルとは別なので注意
        - devcontainer.jsonのextensionsでプラグインのidを入力すると、コンテナ作成時にインストールしてくれる
        - 新しいプラグインをインストールしたら左下のアイコンからrebuildをする
    - setting.jsonはlocalのもコンテナの中で使えているっぽい？
    - 以下を参考にしたら構築できた
        - https://www.keisuke69.net/entry/2020/06/04/145719
        - https://qiita.com/d0ne1s/items/d2649801c6f804019db7

## 入れるプラグイン(コンテナ)
- それぞれのプロジェクトの中の.devcontainerに記述している

# トラブルシューティング
## ms-python.pythonという拡張機能をインストールしたら自動補完が効かなくなった
- 左のメニューバーからextensionを開いて、ms-python.pythonをdisabledにした。workspaceだけではなくて、全体に適用した。

## ショートカットキー
- 画面分割
    - https://mittaniblog.com/vscode-editor-split/
- 基本的に以下のキーを覚えるのがいい
    - https://skillhub.jp/blogs/234
- 定義に飛ぶ
    - `fn+F12`
- 定義を表示
    - `Option+fn+F12`
- 定義を横に表示
    - `cmd+K`からの`fn+F12`
- 一気に行の後ろまで飛んだり、一行を全削除したり

- 置換
    - `Option+cmd+F`
- 正規表現
    - `Option+cmd+R`
