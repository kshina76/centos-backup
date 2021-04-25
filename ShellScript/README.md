# シェルスクリプトのメモ(zsh)

## それぞれのシェルの違い
### ログインシェル
- 起動方法
  - `/bin/bash`や`/bin/zsh`のオプションに`--login`を指定して起動
  - ログインした際に起動
    - `/etc/passwd`ファイルからログインシェルを取得して`${シェルのパス} --login`みたいなことをしている
  - suコマンドやsshコマンドの第一引数に`-`を指定して起動
- 起動したあとは、自動的にインタラクティブシェルのモードに遷移する
  - つまり、よく使っているターミナルで見えているインタラクティブシェルは、元はログインシェルということがわかる
### インタラクティブシャル
- 起動方法
  - ログインシェルから自動的に起動
  - ターミナルで`bash`や`/bin/bash`や`fish`や`zsh`などを打って起動
### 非インタラクティブ(シェルスクリプト実行)
- 起動方法
  - ターミナルで`zsh test.sh`や`./test.sh`のように、シェルスクリプトを実行

<br></br>

## shとsourceの違い
- [ここを参考](https://www.softel.co.jp/blogs/tech/archives/5971)

- スクリプトを実行するという点では、以下は同じ

  ```sh
  $ ./test.sh （実行権限を付与して）
  $ sh test.sh
  $ bash test.sh
  $ source test.sh
  ```

- 違う点は、上の3つは新たな子プロセスを生成して実行するものであり、soruceの場合は現在のシェルで実行するものである点
  - shコマンドでexportしてしまうと、子プロセスでしかexportされない。実行が終わって親プロセスのシェルに戻ってきたら、exportの効力は無いことになる
  - sourceコマンドでexportすると、現在のシェルで適用されるので、exportの効力が残る
- なので、環境変数を定義する目的で ~/.profile などを書いて、ログイン、ログアウトをし直さずに今のシェルに反映させたいときには、source を使用するとできる

<br></br>

## zshの設定ファイルまとめ
- [ここを参考](https://qiita.com/muran001/items/7b104d33f5ea3f75353f)

### local(~/.xxxx)とglobal(/etc/xxx)
- 特定ユーザー（自分）のみ有効にしたい場合にはlocalで記述
- すべてのユーザーで有効にしたい場合にはglobalで記述
- ただしglobalはlocal設定で上書きされてしまうので、必ず設定されるかは保証されない
### zshenv
- 順序からもわかるようにどんな場合でも必ず最初に読み込まれる。
- ログインシェル、インタラクティブシェル、シェルスクリプトのどの場合でも必要な環境変数などはここに記述するのが良い。
- 影響範囲が広くなることから特に目的がなければここに設定を記述するのは推奨されない。
- 例
  - `$PATH`
  - `$EDITOR`
  - `$PAGER`
  - `$ZDOTDIR`
### zprofile
- ログインシェルの場合に１度だけ読み込まれる。
- インタラクティブシェルやシェルスクリプトでは不要だけどログインシェルの時だけ必要な設定をする場合にはここに記述するのが良い。
### zshrc
- ログインシェルとインタラクティブシェルの場合だけ読み込まれる。
- シェルスクリプトでは不要な場合に記述する。
- 一般的に紹介されている記事ではこの設定ファイルにいろいろ記述することが多い。
- 困ったらここに記述してみて問題が出てきたらちゃんと場所を考えるという運用でも問題ないかもしれない。

<br></br>

## シェルスクリプトの書き方
- コマンドライン引数
  - 使い方
    - `$1`: 1番目の引数
    - `$2`: 2番目の引数
  - コマンドライン引数の場合には、関数を呼び出すときに`hello $1`のように渡さないとだめ
  - 通常のグローバル変数の場合には、渡さなくてもアクセスできる
- 条件式
  - かつ: `-a`または`&&`
  - etc
- 関数
  - `function`は省略可

### 例
- proxy環境と非proxy環境を切り替えるシェルスクリプト

```sh
# # 作りたいもの
# - 方針
#   - nswitchコマンドを作成
#   - コマンドライン引数を使って、環境切り替え
# - 環境
#   - npmのみproxy
#   - gitのみproxy
#   - zshのみproxy
#   - curlのみproxy
#   - 全てのproxy
# - コマンド
#   - nswitch --proxy (npm || git || zsh || all) # proxy環境(-pも登録)
#   - nswitch --home (npm || git || zsh || all) # 非proxy環境(-hの登録)
# # 変数
# - proxy=http://example.com:8080
# # プロキシに通すもの
# - nvm(npm)
#   - proxy環境
#     - npm -g config set proxy $proxy
#     - npm -g config set https-proxy $proxy
#   - 非proxy環境
#     - npm -g config delete proxy
#     - npm -g config delete https-proxy
# - git(sshなので、いらないかも)
#   - proxy環境
#     - git config --global http.proxy $proxy
#     - git config --global https.proxy $proxy
#   - 非proxy環境
#     - git config --global --unset http.proxy
#     - git config --global --unset https.proxy
# - zsh(brewなどが関係)
#   - proxy環境
#     - export HTTP_PROXY=$proxy
#     - export HTTPS_PROXY=$proxy
#   - 非proxy環境
#     - unset HTTP_PROXY
#     - unset HTTPS_PROXY
# - curl
#   - 後で

# proxy
proxy=http://example.com:8080

# npmのproxy設定
function nswitch_npm() {
  if [ $1 = "--proxy" ] || [ $1 = "-p" ]; then
    # proxyを有効化
    echo "proxy_npm"
    npm -g config set proxy $proxy
    npm -g config set https-proxy $proxy
  elif [ $1 = "--home" ] || [ $1 = "-h" ]; then
    # proxyを無効化
    echo "home_npm"
    npm -g config delete proxy
    npm -g config delete https-proxy
  fi
}

# gitのproxy設定
function nswitch_git() {
  if [ $1 = "--proxy" ] || [ $1 = "-p" ]; then
    # proxyの有効化
    echo "proxy_git"
    git config --global http.proxy $proxy
    git config --global https.proxy $proxy
  elif [ $1 = "--home" ] || [ $1 = "-h" ]; then
    # proxyの無効化
    echo "home_git"
    git config --global --unset http.proxy
    git config --global --unset https.proxy
  fi
}

# zshのproxy設定
function nswitch_zsh() {
  if [ $1 = "--proxy" ] || [ $1 = "-p" ]; then
    # proxyの有効化
    echo "proxy_zsh"
    export HTTP_PROXY=$proxy
    export HTTPS_PROXY=$proxy
  elif [ $1 = "--home" ] || [ $1 = "-h" ]; then
    # proxyの無効化
    echo "home_zsh"
    unset HTTP_PROXY
    unset HTTPS_PROXY
  fi
}

# 一括でproxyを設定
function nswitch_all() {
  nswitch_npm $1
  nswitch_git $1
  nswitch_zsh $1
}

if [ $2 = "npm" ]; then
  nswitch_npm $1
elif [ $2 = "git" ]; then
  nswitch_git $1
elif [ $2 = "zsh" ]; then
  nswitch_zsh $1
elif [ $2 = "all" ]; then
  nswitch_all $1
fi

```
