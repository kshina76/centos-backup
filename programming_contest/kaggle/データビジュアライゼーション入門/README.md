# データビジュアライゼーション
- 後々読んだ方が良さそうな本
  - データ解析の実務プロセス入門

<br></br>

## データの種類

  ![1_aHohRnwe6dmiqzsiRYEpug](https://user-images.githubusercontent.com/53253817/104723274-5d694380-5772-11eb-9f83-69985da009e1.png)

  ![001](https://user-images.githubusercontent.com/53253817/104723525-b3d68200-5772-11eb-9050-2ca3a13cbfd8.png)

<br></br>

## 色々な可視化
- ヒストグラム
  - 量的変数の分布について度数分布を確認
  - ビニングして表示しているイメージ
  - X軸: 量的変数(がく片の長さ、年齢)
  - Y軸: 出現回数
- カウントプロット
  - 質的変数の分布について度数分布を確認
- ボックスプロット
  - 基本統計量を元にデータの分布を視覚的に表現
- 散布図
  - 二つの量的変数間の関係性を把握するのに使われる
  - 二つの量的変数間の関係性を質的変数(または量的変数)によって色分けする使用法もよくある
- バブルチャート
  - 使い所がわからん
- 散布図行列
  - 一度に複数の変数間の散布図を確認できる
- ジョイントプロット
  - 2変数について複数のグラフを組み合わせて表示することができる
  - 例えば、ヒストグラムと散布図とか
- CatPlot
  - 2変数のうち片方が質的変数の場合の散布図
- 縦棒グラフ
  - 棒の長さで大きさの比較をするときに使われる
  - X軸: 質的変数
  - Y軸: 量的変数の平均値など
- 折れ線グラフ
  - 時系列の変化を表現するする際によく使われるもの
- ヒートマップ
  - 相関とか

<br></br>

## データ可視化フロー
- seabornチートシート
- 比較，分布，構成，関係，の4種類
- https://github.com/kshina76/centos-backup/blob/master/programming_contest/kaggle/データビジュアライゼーション入門/seaborn_CheatSheet.md

<img width="965" alt="68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3130383732392f38333332653831372d393261302d373834382d366438332d3339376230346630633735662e706e67" src="https://user-images.githubusercontent.com/53253817/104796927-c944be00-57fd-11eb-86fa-f4ea177e60d0.png">


<br></br>

## 探索的データ解析フロー
- データ解析のアプローチは、大きく分けて仮説をデータで検証する「仮説検証型」とデータから仮説を生み出す「探索型」に分けられる
- 実際にデータ解析を行うときは、仮説検証型と探索型を行き来しつつ知見を見出していく
- データ解析には検証すべき仮説を設定することが必要で、仮説無しに解析をしても得るものはない
- 仮説を得られないときは、まず仮説を作るためにデータを様々な切り口から眺めて傾向を探る必要があり、そこで探索的データ解析を行う
### データの分布をみる
- データの特徴を把握するのに使用
- 知れること
  - データにどの程度バラツキがあるのか
  - どの範囲にデータが集まっているのか
  - ある範囲のデータの個数はどの程度か
#### データが連続値
- 比べる変数が無いor少ない: ヒストグラム
  - ヒストグラムが多峰な場合は、何かしらのカテゴリ変数ごとにヒストグラムを分けて可視化する
    - 多峰とは、ピークがいっぱいあって正規分布とは程遠い場合
- 比べる変数が多い: 箱ひげ図
  - 比較変数が増えると複数のヒストグラムを並べて同時に比較するのが難しくなることから箱ひげ図を使う
#### データが離散値
- 大きさの比をみる: 棒グラフ
- 内訳をみる: 帯グラフ
- 大きさの比とその内訳をみる: 積み上げ棒グラフ
  - 積み上げ棒グラフは棒グラフと帯グラフを合体させたグラフ
### データの関係をみる 　
- データが連続値: 散布図
  - 散布図は二つの量的変数の関係を見るのに使う
  - 正の相関、負の相関があるのかどうかや、その強弱を調べる
- データが離散値: クロス集計/ヒートマップ
  - 一方、あるいは両方に質的変数を含む変数同士の関係を見るときに使う
  - ヒートマップはクロス集計のセルが多いときに威力を発揮
  - ヒートマップは相関を見るようとだけではないっぽい
### データの推移をみる: 主に時系列データに対して、時間的推移を見たいときの可視化手法
- 傾きの増減とその程度をみる: 折れ線グラフ
- 推移の方向と分布をみる: ロウソク足チャート
### 参考文献
- https://qiita.com/hanon/items/33488ed4fc4ece7e1aec
