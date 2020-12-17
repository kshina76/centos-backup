# GitHub書籍メモ

## gitでの開発フローまとめ
1. 最新のdevelopからチケット番号でブランチを切る
2. チケット番号ブランチで開発した機能をコミット、プッシュする
3. 終わったらdevelopにプルリクエストを送り、レビューの後マージされる
4. ステージング環境に最新のdevelopを出して確認する
5. 問題なければdevelopをmasterにマージしタグ付け、 本番に最新のタグをデプロイする

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
