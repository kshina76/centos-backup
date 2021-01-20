# fxシステムトレード

## わかったこと
- Log lossとAccuracyの違い
  - Accuracy
    - 予測した値と正解が一致していた数のカウント。正解/不正解しかないのでいつも良い指標とは限らない（惜しかった、などが測れない）
  - Log loss
    - 実際のラベルからどのくらい違っていたのかを考慮できる
    - 分類モデルの性能を測る指標。(このLog lossへの)入力は0~1の確率の値をとる。
    - 正解ラベルが1の時に、0に近づくほど間違えているのでLog lossは大きくなる。1に近づくほど正解しているのでLog lossは小さくなる
  - https://qiita.com/exp/items/1c6c9a3fae2d97bfa0c7
- XGBoostのobjectiveパラメータ(最小化させるべき損失関数を指定)
  - multi:softmax
    - 多項分類でクラスの値を返す
    - 確率が一番高いクラスの値を返す
  - binary:logistic
    - 2項分類で確率を返す
    - 確率そのものが返ってくるので、0.5を境に0,1に振り分け直す処理を書く必要がある
  - reg:logistic
    - binary:logisticと違いはない
    - 違いとしてはデフォルトの評価指標がrmseということ
    - https://github.com/dmlc/xgboost/issues/521
- 回帰と分類の違い
  - 回帰は出力が実数値
  - 分類は出力がカテゴリカル
- 線形回帰と非線形回帰
  - 線形回帰
    - 単回帰: 直線
    - 重回帰: 平面
  - 非線形回帰
    - ロジスティック回帰: 曲線、局面
    - 多項式回帰: 曲線、局面
    - 平滑化回帰: 曲線、局面
  - http://i.cla.kobe-u.ac.jp/murao/class/2014-SeminarB2/9_NonlinearRegression.pdf
- ロジスティック回帰と重回帰の使い分け
  - ロジスティック回帰は0,1の間の値を確率として出力するから分類問題に使える
  - 重回帰は出力が0,1の間ではない実数値になるので、純粋な回帰問題に使える
  - https://jp.quora.com/juu-kaiki-bunseki-to-rojisuteikku-kaiki-bunseki-no-chigai-ha-nande-suka
- ロジスティック回帰は分類か回帰か
  - ロジスティック回帰は確率値(実数)を回帰で求めて、その結果を0.5以上を1として、0.5未満を0にして分類問題に使う
  - 分類問題に使うことがほとんどだからややこしくなる
  - https://scrapbox.io/nishio/ロジスティック回帰は回帰か分類か
- ソフトマックスは回帰が分類か
  - ソフトマックスは確率が高いクラスが出力になるので、出力がカテゴリカルになる。つまり回帰ではなくて分類
- XGBoostのn_estimatorsは学習回数のこと
  - DNNでいうepochのこと
  - n_estimatorsはパラメータサーチをしてはいけない
    - https://amalog.hateblo.jp/entry/hyper-parameter-search
- XGBoostをPythonで実現するには二つの方法がある
  - trainを使った方法
    - データをDMatrixで変換する必要がある
  - XGBRegressorやXGBClassifierを使う方法
    - Scikit-laernのようにかけるからわかりやすい
    - CVが使える
    - DMatrixでデータを変換する必要がない
  - https://note.com/teru3900/n/n9d5e8936704a
- grid searchはscikit learnを使えば簡単にできる
  - https://qiita.com/msrks/items/e3e958c04a5167575c41
  - https://qiita.com/aaatsushi_bb/items/0b605c0f27493f005c88
  - https://qiita.com/shinaK/items/434935d331c0511edef3
- XGBoostでチューニングすべきパラメータ
  - https://qiita.com/aaatsushi_bb/items/0b605c0f27493f005c88
- XGBoostのパラメータ解説
  - https://qiita.com/FJyusk56/items/0649f4362587261bd57a
- talibライブラリの返り値がnanだらけになる理由
  - C言語ベースのライブラリで、そのような仕様だから。`[-1]`として最後の値を取得すればいい
  - https://github.com/mrjbq7/ta-lib/issues/17


<br></br>

## TODO
- mo,poがNaNになってしまうので調査
- macdが0になってしまうので調査
- 時系列データ交差検証
- xgbのパラメータの調査
- xgbのtrainとfitの違い
  - https://teratail.com/questions/198971
- xgbのモデルの保存方法(pickleを使わない方法)
  - https://qiita.com/tmitani/items/48aa45c12af816727f4d
- 推論の部分を実装(やったけど、trainとtestを分けたい)
  - https://blog.amedama.jp/entry/2019/01/29/235642

<br></br>

## 用語
### bid/ask
- bidは売りの時の価格(チャートに表示されている値)
- askは買いの時の価格(売りの時の価格にスプレッドを加算した値)
- つまり、機械学習モデルはbidで組めばいい

<br></br>

## 参考文献
- oandaAPIで5000件以上の値を取得する方法
  - https://www.tcom242242.net/entry/python-basic/oandpy/【onadav20python】oanda-api-v20で5000件以上のデータを取得する/

<br></br>

## アイデア
- ストキャスとかRCIの全組み合わせをパラメータで指定できて、そこから最適化する
- チャートを反転させたときのデータも学習するといい精度になるらしい
- xgbを回帰の2値分類にすることで、1に近づくほど上昇しやすい、0に近づくほど下降しやすいという分類を可能にした
- テクニカルを用いることで、純粋な時系列モデルを組まなくても済んでいる
- オシレーター系を「0」が売られすぎ、「1」買われすぎで分けて特徴量に追加する

<br></br>

## 使用技術
- ライブラリ
  - oandapyV20
  - ta-lib
- GPU関連
  - https://github.com/Kaggle/docker-python
