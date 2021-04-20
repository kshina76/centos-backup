# GitHub運用まとめ

## vscodeを使ったgitでの開発フロー
- 以下を参考にすれば、全てわかる
  - [VSCodeでのGit基本操作まとめ](https://qiita.com/y-tsutsu/items/2ba96b16b220fb5913be)
  - [gitでのチーム開発マニュアル](https://qiita.com/siida36/items/880d92559af9bd245c34)
  - [git-fetch,git-merge,git-pullの違い](https://qiita.com/wann/items/688bc17460a457104d7d)
  - [git-fetchを細かく解説](https://qiita.com/matsumon-development/items/d3231acccc08c8d74c21)
  - [VSCodeでgitのコンフリクト解消](https://qiita.com/penpenta/items/08b59f4b788ca2ae1c07)

### 手順

![CC105070-59B0-4F35-B0B2-402736DC28BB](https://user-images.githubusercontent.com/53253817/115416769-05d7e980-a233-11eb-8d5e-ede58b6f74c0.jpeg)

- 方針
  - こまめにpull(fetch->merge)をして、`origin/master`,`master`,`origin/develop`,`develop`を最新に保つ
  - コードを書きたくなったら、必ず`master`または`develop`にチェックアウトしてから、ブランチを切る
    - 変なところからブランチを切ってしまうと、コミット履歴などが汚くなってしまうから

- 新しくコードを書きたくなった時
  - ローカルのmasterブランチ(またはdevブランチ)に移動
  - fetchする
  - mergeする
  - featureブランチを切って移動する
  - コードを書く
  - commitする
  - pushする
  - GitHub上でプルリクを送る、masterまたはdevにマージされる
  - リモート追跡の`origin/feature/...`ブランチをVSCodeから削除
    - 何回かプルリクを送って、機能の開発が終わったら削除すれば良い
  - pullをする(fetch->mergeの手順で)
    - リモート追跡の`origin/master`ブランチに、リモートブランチの`master`または`dev`をfetch
      - `cmd+shift+P`で`gitfetch`と検索をしてエンター
      - `git fetch origin develop`としたら、リモートのdevelopブランチを`origin/develop`に取り込むということ
    - ローカルのmasterブランチに移動して、`origin/master`をmergeする
  - ローカルの`feature/...`ブランチを削除する

- コンフリクトの解消
  - Accept Both Changeを選択する

### 用語
- `origin`
  - GitHubのリポジトリのURLを指している
- `origin/master`
  - masterのリモート追跡リポジトリ
  - GitHubのmasterブランチを追跡している(pullなどをしないと最新の状態を保持できない)
  - `pull`や`fetch->merge`をすると保存される場所
- `origin/develop`
  - developのリモート追跡リポジトリ
  - GitHubのdevelopブランチを追跡している(pullなどをしないと最新の状態を保持できない)
  - `pull`や`fetch->merge`をすると保存される場所

![BF70E40B-1FB0-4E21-BD2B-CD6A497A86BC](https://user-images.githubusercontent.com/53253817/115421925-5ea98100-a237-11eb-8ae6-edd5b07b4355.jpeg)


<br></br>

## gitでの開発フローまとめ
- commit前はとりあえず`git status`と`git diff`でステータスと差分を確認する
- commit後はとりあえず`git hist`でコミットログを確認してコミットされているかを確認
- 参考文献
  - https://www.youtube.com/watch?v=1kThUbSdlro
### 事前準備
1. モジュールのインストール
  - commitizenのインストール
    - gitのcommitメッセージを対話形式で簡単に作成することができるツール
  - peco
    - エイリアスの`git df`で必要
    - https://qiita.com/reireias/items/fd96d67ccf1fdffb24ed
  - tig
    - コミットログを綺麗なフォーマットで表示できるツール
    - `git df`や`git hist`のエイリアスが要らなくなるかも
    - https://qiita.com/suino/items/b0dae7e00bd7165f79ea
  - hub
    - `hub browse`でコマンドラインからgithubのサイトを開くことができる
    - https://dev.classmethod.jp/articles/hub/
2. エイリアスの設定
  - `git df`
    - コミットのログを表示してくれて、任意のコミットを選択するとdiffを表示してくれる(どんな変更を加えたかの表示)
    - 17分〜
  - `git hist`
    - コミットのログを表示
  - `git ps`
    - pushのエイリアス
    - pushするときに作業しているブランチをオプションで選択する必要がなくなるので便利
    - `git push origin HEAD`をエイリアスにしている。HEADを指定するとブランチ名を指定しなくてもカレントブランチをリモートにpushできる
  - `git pl`
    - pullのエイリアス
    - 理由はpsと同じ
  - https://github.com/craftzdog/dotfiles-public

### リポジトリの作成〜イニシャルコミット
1. プロジェクトディレクトリの作成
  - DjangoやFlaskなどそれぞれに合わせた方法を調べて作成する
2. リポジトリの作成
  - github上で作成
  - すでに作成してある場合は、`git clone`をすれば`git init`などもされている状態になる
3. プロジェクトディレクトリの初期化
  - `git init`
4. git remote add origin git@github.com/example
  - リモート追跡にリモートリポジトリを登録
5. リモート追跡に登録されたか確認
  - `git remote -v`
6. ステータスを確認
  - `git status`
  - コマンドを打つ度に確認していいと思う
7. ステージングに反映
  - `git add .`
  - 最初のコミットは`git add .`でも問題ないが二回目以降は目的のファイルだけをステージングにあげるようにしたほうがいいと思う
8. ステータスを確認
  - `git status`
9. 差分を確認
  - `git diff`
10. ローカルリポジトリに反映: commitizienを使う
  - `git cz`or`git cz -a`
  - コミットメッセージをインタラクティブに入力する
11. コミットログを確認
  - `git hist`
12. プッシュ
  - `git ps`

### ブランチを切る〜masterにマージ
1. 最新のdevelopからチケット番号でブランチを切る
2. チケット番号ブランチで開発した機能をコミット、プッシュする
3. 終わったらdevelopにプルリクエストを送り、レビューの後マージされる
4. ステージング環境に最新のdevelopを出して確認する
5. 問題なければdevelopをmasterにマージしタグ付け、 本番に最新のタグをデプロイする

### PRからマージ
1. PushしたブランチからGitHub上でPRを作る
2. PR用のテンプレート設定されているなら、それに入力
3. Reviewersからレビューして欲しい人を選択
4. PRのコメントに「close #issue番号(またはissueのURL)」を入力して、PRがマージされた際にissueも同時にcloseするようにする
5. レビューを受けて承認をもらう
6. 自分でマージする(普通は権限を持っている人がマージする)
7. featureブランチを削除する

### リジェクトとコンフリクト
- pushが拒否される二つの理由
  - リジェクト: 異なるファイルに変更を加えた場合
  - コンフリクト: 同一のファイルに変更を加えた場合
- リジェクトの対処法
  - いったん「git pull」（git fetchとgit merge）を実行してから再度「git push」を試みる
  - git fetchでリモートリポジトリの最新の情報をローカルリポジトリに取り込む
  - git mergeで他のブランチやコミットの内容を現在のブランチに取り込む
- コンフリクトの対処法
  - https://www.atmarkit.co.jp/ait/articles/2005/22/news028.html

- https://qiita.com/te2u/items/c23f82ec84cf65564554
- https://www.atmarkit.co.jp/ait/articles/2005/22/news028.html

### 参考文献
- https://note.com/gure_ko/n/n6af09ab69adf
- https://gist.github.com/yousan/b147f14d0c1d697dde6f4d4d6c857fb8
- https://techracho.bpsinc.jp/morimorihoge/2020_09_09/16856
- https://cloudsmith.co.jp/blog/efficient/2020/08/1534208.html


---

- Notification
  - 「@ユーザ名」...ユーザにメンションを送ってメッセージを送信できる
  - 「@組織名」...組織全体にメンションを送信できる
  - 「@組織名/チーム名」...組織に属するチーム全体にメンションを送信できる
  - 「#番号」...そのリポジトリのissue番号にリンクとなる
  - 「ユーザ名/リポジトリ名#番号」...指定したリポジトリへのリンクとなる

---

## それぞれのコマンドの説明

### local
- git init
  - 初期化して.gitを作り、gitの管理対象にするコマンド
  - すでに開発が進んでいるものをcloneした場合は、.gitは最初から作られているのでinitコマンドは使わなくていい
  - .gitが作られていることでgitに管理されることになり、gitのコマンド類が使えるようになる。コマンドの結果は全て.gitに保存されるようになる
  - initをしただけだと、リモートリポジトリの設定がまだだから、git remoteコマンドで設定をしないとダメ

- git addコマンド
  - ステージ領域へファイルを追加

- git commit
  - ローカルリポジトリにリポジトリの歴史を記録
  - この記録を元にワーキングツリーを復元したりする
  - 1行のコミットメッセージならmオプションをつけてコミット
  - 詳細なコミットメッセージならオプションをつけずにコミットすることで、エディタが立ち上がる。フォーマットは以下に準ずる。

    ```
    1行目    コミットする変更内容の要約を1行で記述
    2行目    空行
    3行目以降    変更した理由や詳細を記述
    ```

### log

- git status
  - 前回のコミットと比較した変更内容を表示する
  - gitリポジトリの状態を確認するコマンド
  - 状態は目まぐるしく変わるから、このコマンドで常に確認するようにする

- git log
  - コミットのログを確認

- git diff
  - 「ワークツリー、ステージ領域、最新コミット」間の差分を確認するのに利用するコマンド
  - 「git diff HEAD」コマンドを実行するとワークツリーと最新コミットの差分を確認する。HEADは作業しているブランチの最新のコミットを参照するポインタ。
    - git commitコマンドを実行する前に、このコマンドを実行して前回のコミットとどのような差分があるかを確認する癖をつける



### remote

- git remote -v
  - URLも含めた一覧表示

- git remote add <任意名> <URL>
  - リモートリポジトリを登録
  - 慣習でoriginがよく使われる

- git remote rm <リモートリポジトリの名前>
  - リモートリポジトリの情報を削除

- git fetch
  - リモートリポジトリの最新の状態をローカルリポジトリのリモート追跡ブランチにダウンロードする。
  - ワーキングツリーに影響はない
  - 何も引数に渡さないとgit fetch origin masterが実行される
  - git fetch origin/develop develop とかできるのかな？

- git clone
  - cloneの場合はgit remoteのコマンドはいらない。クローンした時点でoriginにURLが登録される


- git push <リモートリポジトリ> <ローカルブランチ名>
  - git push origin master
      - ローカルブランチのmasterをリモートリポジトリのorigin上の「同名のブランチ」に反映するという意味
  - git push origin master:master
      - 省略せずに書いたパターン
      - ローカルのmasterブランチをリモートのmasterブランチに反映
  - https://www-creators.com/archives/1472


### branch

- git branch --all
  - ブランチを一覧表示
  - allをつけるとリモート追跡ブランチも表示する(ローカルリポジトリにリモートリポジトリの情報を保存しているところ)

- git branch <ブランチ名>
  - ブランチを新規作成

- git branch -m <変更前> <変更後>
  - ブランチ名を変更

- git branch -d <ブランチ名>
  - ブランチを削除
  - Dオプションにすると強制削除

- git checkout <ブランチ名>
  - ブランチを切り替える

- git checkout -b <ブランチ名>
  - ブランチを新規作成して切り替える
    - 作成と切り替えを同時に行う

- git merge
  - ブランチをマージ
  - 統合ブランチにcheckoutしてから、mergeコマンドでトピックブランチを指定することでマージできる
  - トピックブランチは事前にコミットしておくこと
  - 「git merge --no-ff <トピックブランチ>」
    - エディタが立ち上がるが、デフォルトで記述されているから変更しなくていい
  - mergeはあくまでもローカルリポジトリ内の操作なので、リモートリポジトリに反映させたい場合は、mergeの後にmergeしたローカルリポジトリをpushする

## 色々なブランチ
- 安定したブランチ
  - いつでもソフトウェアをリリースできるような安定した状態に保っておくブランチ
  - 通常はmasterブランチなどが安定したブランチ

- トピックブランチ
  - トピックごとのブランチ
  - 例えば、ソフトウェアに機能追加を行いたい場合は、安定ブランチから分岐させて、その分岐させたブランチに機能追加を行っていく
  - また、バクが見つかった場合も新たにトピックブランチを作成して、そのブランチで修正する
  - トピックが達成されたら、トピックブランチを安定ブランチにマージする

- 統合ブランチ
  - 安定ブランチのこと
  - トピックブランチの分岐元のこと
  - masterからdevelopブランチに分岐させて、そのdevelopブランチ上でトピックブランチを分岐させて開発していく場合は、developブランチが統合ブランチになるのかな？

## ブランチモデル
- 開発でどのようにブランチを運用していくかを決めるためのモデル

- git-flowモデル
  - master, develop, feature, release, hotfix, supportブランチを使って運用していく
  - qiitaでわかりやすい図

- GitHub Flowモデル
  - git-flowを簡略化したモデル
  - master, topicブランチを使って運用する

- https://qiita.com/gold-kou/items/7f6a3b46e2781b0dd4a0


## 色々な手順
- mainブランチにdevelopブランチをマージ
  - 本当はdiffやstatusで状態を確認しながらマージしないとダメ

  ```bash
  $ git branch develop      # developブランチを作成
  $ git checkout develop    # developブランチに移行
  $ git add .               # ステージング環境に反映
  $ git commit -m "add"     # ローカルリポジトリに反映
  $ git push origin develop # リモートリポジトリに反映(コミットしたらプッシュはすぐにする癖をつける。コンフリクトしないように)
  $ git checkout main       # マージしたい方に移行する(忘れずに。移行しないとマージできないから)
  $ git merge main develop  # mainブランチにdevelopブランチをマージ(ローカル)
  $ git push origin main    # リモートのmainブランチに反映
  ```

- PullRequestを送る
  - Forkしないパターン(企業内での開発はこっちが一般的かな)
    - https://qiita.com/samurai_runner/items/7442521bce2d6ac9330b
  - Forkするパターン(OSSに参加するならこっちかな)
    - https://qiita.com/aipacommander/items/d61d21988a36a4d0e58b


## わかったこと
- コミットしたらすぐにプッシュすること
  - コンフリクトを避けるために

- 変更を反映したいブランチがある場合は、その変更したいブランチにcheckoutしてから反映作業を行う
  - mergeでもpushでもcommitでもなんでも

- 実際の開発ではPullRequestを投げるので、mergeコマンドを使うことはないかも(mergeは権限がある人だけ)
  - developブランチから派生したfeatureブランチなどにpushして、developにmergeしてもらうためにPullRequestを投げるというかんじ

- ブランチAからブランチBのように異なるブランチ間のプッシュは使わない気がする
  - ブランチBにブランチAをマージして、ブランチBをプッシュすれば、実現できるのでこのように行うといいと思う

- commitとpushの頻度
  - タスク、サブタスク毎に行う
  - commitをしたらすぐにpushする
    - 複数回のコミットをまとめてプッシュしてしまうと、大きいコンフリクトが発生してしまったときに面倒だから
  - https://qiita.com/kozyty@github/items/87fa95a236b6142f7c10

- cloneとforkの違い
  - forkは自分のgithubアカウントに他人のリポジトリをコピーしてくること
  - cloneは自分のローカルマシンにリモートリポジトリをコピーしてくること
  - 開発するときにprを送ったりするのにcloneを使うのが一般的
  - OSSの開発に参加するときはforkするのが一般的。なぜかというと、forkするとオリジナルのリポジトリの管理者にforkしたことが伝わるから。意思表明のようなもの。

## 用語
- ワークツリー、インデックス、リポジトリ
  - ワークツリー
    - gitに管理されているファイルやディレクトリのこと。いつも開発するときに触ってるgoファイルとかhtmlとか。
  - インデックス(ステージ領域)
    - git addコマンドを使用することでワークツリーからステージ領域に反映する。
  - ローカルリポジトリ
    - git commitコマンドを使用することでステージ領域からローカルのリポジトリに反映する
  - リモートリポジトリ
    - git pushコマンドを使用することでローカルリポジトリからリモートリポジトリに反映する
  - https://backlog.com/ja/git-tutorial/intro/04/
  - https://qiita.com/nnahito/items/565f8755e70c51532459


---

# githubを使った開発の進め方
- 参考文献(https://qiita.com/sekiyaeiji/items/d0312c90bff4c37bc5dc)

# githubブランチについてのまとめ  
- 参考文献(https://qiita.com/katsunory/items/252c5fd2f70480af9bbb)
## ブランチの名前付け
### master
- リリース可能な状態だけを管理する
- 特定のブランチからマージすることによってしか更新されない
- 直接コミットしてはならないという制約をもつ
- バージョンごとのtagはここから生まれる
- いつでもリリースできるロボットを表す

### develop/[バージョン番号など]
- 先のリリースに向けた普段の開発で使用する
- 後述のfeatureやreleaseブランチはここから派生
- 開発中のロボット全体を表す

### feature/[派生元バージョン番号など]/[機能名など]
- 機能追加改修などを行う作業ブランチ
- developブランチから、featureブランチを切る
- 完了後はdevelopブランチにマージされて、featureブランチは削除される
- ロボットの一部分を表す。例えば、[feature/foot]というブランチなら、ロボットの足の開発の部分を表す。

### その他
- release/[バージョン番号]
- fix/[バージョン番号]/[バグ識別名]
- support/[バージョン番号]
- hotfix/[バージョン番号]/[バグ識別名] or hotfix/[バグ識別名]
