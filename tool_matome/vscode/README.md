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
