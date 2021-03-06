# マンガでわかるマッキンゼー式ロジカルシンキング

# 自分メモ

## 知りたいこと
- 「課題発見」の方法
  - イシューからはじめよう
  - https://note.com/1996_0928/n/n8abfb82f5ed7
- ロジカルに書く方法
- ロジカルに説明する方法
- ロジカルに聞く方法

## 帰納法と演繹法(えんえき)とアブダクション
- 「こうだったらこうだろう」と推論するだけのこと

![2021-01-19 17 56のイメージ](https://user-images.githubusercontent.com/53253817/105011052-cfe26800-5a7f-11eb-8080-aa0ca85eb85e.jpeg)

### 帰納法: 事実の積み重ね
- 複数の事象から結論を導く方法
- 用途
  - 不確定要素の多いビジネスの現場でよく使用される
- 例
  - ソクラテスは死んだ。アリストテレスも死んだ。織田信長も死んだ。だから人間は死ぬ。
    - ソクラテスは死んだ→事象1
    - アリストテレスも死んだ→事象2
    - 織田信長も死んだ→事象3
    - だから人間は死ぬ→結論
1. 事象を集める
  - 結論に導くための材料
  - メリットデメリットどちらの事象も集める
2. 物事の共通事項を見つける
  - 「ソクラテス、アリストテレス、織田信長はみんな人間」という共通項
3. 共通項から結論を導き出す

### 演繹法: 3段階で考える
- 一般的に正しいとされることとある事象(普遍的事象)から、妥当と考えられる結論を導き出す手法
- 用途
  - 普遍的原理に従って論理を展開するため、ある提案に対して反論したい際などにも使用できる
- 例
  - 人間は皆死ぬ。ソクラテスは人間だ。よってソクラテスは死ぬ。
    - 人間は皆死ぬ→大前提(普遍的事象)
    - ソクラテスは人間だ→小前提(理由)
    - よってソクラテスは死ぬ→結論
1. 普遍的事象を考える
2. 小前提を考える
3. 結論づける
- 練習する手順
  1. 結論を考える
    - 何を結論としたいかを明確にしないと、2以降の答えが変わってしまう
  2. 理由を考える
    - なぜその結論を導きたいのか、どこから結論を探し出して来たのか、など結論に至るまでの思考過程や要素を形にしていく作業
  3. 普遍的な事象を考える
    - 一般的に多くの人が当たり前のように知っていることを探す作業

### アブダクション
- 結果から原因を推測し、観測事実に対して説明を見つける手法
- 用途
  - ある事象をもとに複数のアイデアを出してプレゼンなどの資料にまとめる際に有効
- 例
  - 朝起きると庭の芝生が濡れていた。雨が降ると芝生は濡れる。だから昨晩は雨が降ったのだろう。
    - 朝起きると庭の芝生が濡れていた→目の前の現象
    - 雨が降ると芝生は濡れる→普遍的事象
    - だから昨晩は雨が降ったのだろう→仮説

### メモ
- 研究は、帰納法とアブダクションで進めて、演繹法でまとめるのかな？？
- 仮説思考
- どの方法を行うときも「思いつかなかった」が問題点になる。そのような時に「メモ書き」を行うことで容易にできる
- プログラマは演繹？帰納？

### 参考文献
- 帰納、演繹の具体的なポイント
  - https://japan-lifehack.com/logical-thinking-training-induction-deduction/

## ロジックツリー
- ロジックツリーは、1段目にテーマと成る事象を置き、2段目・3段目とそれを要素分解
- ロジックツリーは次のアクションにつなげるためのもの
- ロジックツリーの枝分かれの仕方: ノードごとに以下を行う
  - 要素分解ツリー: 「what(それを構成する要素は何か？)」を繰り返しながら枝分かれさせていく
  - 原因追求ツリー: 「why(なぜその事象が起こるのか？)」を繰り返しながら枝分かれさせていく
  - 問題解決ツリー: 「how(どうすれば解決できるのか？)」を繰り返しながら枝分かれさせていく
### 要素分解ツリー(What)
- その名の通り物事の要素をどんどん分解していって、要素を網羅的に把握するためのロジックツリー
- 右に深掘りされていくにつれて「具体性」が上がっていく

![logic-tree_01](https://user-images.githubusercontent.com/53253817/105039272-b2bf9080-5aa3-11eb-9b47-058173060aeb.jpeg)

### 原因追求ツリー(Why)
- ある問題に対して原因を列挙し、根本原因が何なのかを突き止めるためのロジックツリー
- 右に深掘りされていくにつれて「アクション」が明確になっていく

![20181101005236](https://user-images.githubusercontent.com/53253817/105041926-f667c980-5aa6-11eb-99fe-dd7d4fca4c92.png)

![logic-tree_02](https://user-images.githubusercontent.com/53253817/105039278-b3582700-5aa3-11eb-898d-f5286e24fe07.jpeg)

### 問題解決ツリー(How)、イシューツリー
- 解決したい問題に対して改善策を挙げて、具体的なアクションを明確にする使い方
- 右に深掘りされていくにつれて「アクション」が明確になっていく

![20181202151123](https://user-images.githubusercontent.com/53253817/105041928-f667c980-5aa6-11eb-9a6d-9183c1cf10d6.png)

![logic-tree_03-1024x626](https://user-images.githubusercontent.com/53253817/105039279-b3f0bd80-5aa3-11eb-88c9-11f0b138a9af.jpeg)

## 「課題発見 -> 仮説検証」のサイクルを回す手順
- 「ロジックツリー」を作るとわかりやすい
  - 原因追求ツリーなどのロジックツリーで分解していった時にルートノードが「課題」、子ノードが「仮説」、右に行くほど「検証」が配置されているから
  - 一つ一つの仮説を検証していくことでPDCAサイクルが回って、最終的な課題を解決することができる
### 手順
1. 課題を発見する
2. ロジックツリーの種類を決める
3. 「メモ書き」でロジックツリーの深掘りをする
  - 「原因追求ツリー」なら「なぜ？」をメモ書きで繰り返す
4. ロジックツリーに清書する
5. ロジックツリーに沿って「仮説->検証」を繰り返す
6. 新しい仮説を思いついたら適宜ロジックツリーに付け足していく
7. 繰り返す

### 例
- データ分析
  - 原因追求ツリーで行ってみる

```markdown
- モデルの精度が上がらない
  - 過学習をしているから
    - early stoppingをする
    - leakageしているから
      - 時系列データのデータ分割ミス
      - 未来の情報まで集約してしまっている
  - モデルの表現力がないから
    - 活性化関数を噛ませる
    - 隠れ層を増やす
    - データ量が足りないから
      - データを収集し直す
      - data augumentationをする
```

### わかったこと
- 「メモ書き」はロジックツリーを作っていることに変わりない
  - ロジックツリーをブレインストーミングで書くみたいな感じ
- 「メモ書き」はロジックツリーで重要な事柄である「MECE」を満たすのに最適
  - どんどんアイデアを出すからMECEを満たしやすい


### 参考文献
- https://infinity-agent.co.jp/lab/logic-tree/
- https://www.nsspirt-cashf2.com/entry/2018/12/23/297/

<br></br>

# プロローグ
## ロジカルシンキングの本当の意味
- 相手に「なるほどね」と言ってもらえるようにわかりやすく伝えること
- 「これがこうだったら、こうなるはず」という簡単なこと
  - 空が暗くなってきたから、雨が降りそうだ、だから傘を持って出かける

## ロジカルシンキング
1. 論理的にものごとを考えて整理して、問題点を正確に捉える
  - 現状分析
2. 既成概念にとらわれずもっとも適切な方法を見つける
  - ゼロベースで本質を捉える
3. 具体的に実行する手法・姿勢
  - 本質を考えただけで実行できないものではなくて、実行できるようなことを考える

## ロジカルシンキングの練習
- 好きなことや関心のあるもので論理的思考を使う
- 例1(帰納法): フレームワーク選定
  - (事実1)チームがPythonに精通している人が多いからプログラミング言語はPythonが良い
  - (事実2)パフォーマンスが必要なので、非同期に対応しているフレームワークが良い
  - (事実3)目的はAPIを作ること
  - (結論: 1,2,3より)FastAPIが有効

# 「A4メモ書き」で論理的思考は身に付けられる
- メモに書くことで頭の中が整理されて、解決策が思い浮かぶ
- ポイント
  - 以下のメモ書きを1日に10枚書くのが練習
  - 以下の例だと、10文字程度だけど、慣れてきたら20~30文字で書けるようにする
  - 言葉を選ばず、内容を吟味せず、頭に浮かぶままに書き出していく
- なぜA4の紙なのか
  - 速いから
  - 電子機器だと1枚に1タイトルにならないから
  - 電子機器だとカテゴリ分けしにくいから
  - なので、パワポなどは清書するときに落とし込む先として使用する
- なぜやるのか
  - メモ書きで行っていたことが、書かなくても思い浮かび、瞬時に解決策に導くことができるようになるから
## 方法
1. A4コピー用紙を横置きにして、タイトルを書く、右上に日付を書く
  - 例1:「どうして寝坊をするのか」
  - 例2:「どんな企画が心に残るか」
  - 例3:「どんなフレームワークがパフォーマンスが出るか」
2. 1の具体例を紙1枚に4~6行、各行に20~30文字程度で、1分以内に書く
  - 例1
    - 「お風呂に入るのが遅いから」
    - 「寝る前にスマホを見てしまうから」
    - 「目覚ましが意味をなしていないから」
    - 「みんなと話してしまうから」
    - 「長時間寝ても安眠できないから」
3. 2の項目からタイトルを見つけて、再度2を繰り返す
  - タイトル: 「なぜ安眠できないのか」
    - ベッドが合っていないから
    - 枕が合っていないから
    - 寝る時間がバラバラだから
4. 1〜3を整理してまとめると企画書や提案書になる
5. 寝る前に7個くらいのカテゴリに紙を振り分けていく
  - これによって頭が整理される
## タイトルの付け方
- タイトルは疑問形にする
  - 例1: どういう時に論理的でないと言われるか？
  - 例2: どのようなフレームワークが優れているか？
- タイトルはTODOやHOWTOでもいい
  - 例1: 会議で発言するべきこと
  - 例2: 企画書を速くまとめる方法
- タイトルは抽象的ではなく具体的に(固有名詞も入れる)
  - 例1: なぜ山田さんは私のことをバカにするのか？
- タイトルを多面的に見て、新しいタイトルを生み出す

  ![2021-01-19 18 48のイメージ](https://user-images.githubusercontent.com/53253817/105017236-e50ec500-5a86-11eb-81ad-d39c5ba1bac0.jpeg)

## 習慣
- 電車の中の中吊り広告を見て、何を訴えようとしているのかを考える
- 人と話す時も、本音はどこにあるのかを考える
- 何に対してもメモ書きを実践してみる
  - 例えば、リーダーに任命されたら、「なぜリーダーに任命されたのか」をタイトルとして深堀してみるとか

<br></br>

# マトリックスで脳内を整理する
- あとで読む
## 3つ理由(根拠)をつける
- 何に対しても理由は3つ述べるようにする。述べることができないなら、その方法は間違っているかもしれないので、他の方法を模索する

<br></br>

# 「フレームワーク」で思考を加速する
- 理詰めの発送にフレームワークを使うことで、クリエイティブな発想を可能にする
## 3C分析

![2021-01-19 19 58のイメージ](https://user-images.githubusercontent.com/53253817/105025526-c7465d80-5a90-11eb-907e-b152f66876d2.jpeg)

## メモ書きと3C分析を組み合わせる
- メモ書きを行うことのメリットとして、簡単に深堀りできることがある

![2021-01-19 20 07のイメージ](https://user-images.githubusercontent.com/53253817/105026523-f6a99a00-5a91-11eb-921b-c501c001b872.jpeg)

## 「ロジックツリー」で問題解決を導く
- ロジックツリーには何種類かある
- 「現象・問題」「本質的な原因」「根本的な解決策」「具体的施策」のロジックツリーを紹介する
- もちろんメモ書きで深掘りしてからロジックツリーに清書してみるという方法も使える

![2021-01-19 20 12のイメージ](https://user-images.githubusercontent.com/53253817/105027078-abdc5200-5a92-11eb-9bf4-b229a09e93e7.jpeg)

## マーケティング戦略に使える「4Pロジックツリー」
- Product(製品)、Price(価格)、Place(流通、販路)、Promotion(プロモーション)をルートの隣接ノードとして書いていくロジックツリー

![2021-01-19 20 48のイメージ](https://user-images.githubusercontent.com/53253817/105030855-be0cbf00-5a97-11eb-8d87-29dac6614662.jpeg)
