# データ分析の流れ  
## 1.とりあえずスコアを出す  
ベースラインとなるスコアを出しておく  
以下行う作業  
・データセットからユーザidを落とす(これはすぐやる)  
・データセットからtargetを分離する(学習する直前に落とした方がいい多分。)  
・label encodingしてGBDTでモデル作成  
・submit(これを基準のスコアとする)  
  
## 2.データ確認  
データの中身を調べていく作業  
  
### 2-1.手動で推測  
・カラムの名前からどのような特徴量かを推測(この時点で完全にわかる必要はない)  
・自作のdescribe featureでデータの内訳を確認  
・カテゴリ変数と数値変数を分けてカラムのリストを作成(手作業で)  
  
### 2-2.可視化  
・カテゴリをcountplotで出現回数を可視化  
・数値をdistplotwで出現回数を可視化  
・カテゴリ(x軸)×数値(y軸)で可視化していく。pairplotやboxplotで相関や規則性を見る。  
・数値×数値で可視化していく。pairplotなど。  

### 2-3.参考文献  
・可視化での詳しいメモは後述する「可視化でわかったこと」を参照  
・可視化は以下の方法から必要なものを選んでいけばいいと思う。  
https://www.kaggle.com/kralmachine/seaborn-tutorial-for-beginners  
https://www.kaggle.com/kanncaa1/seaborn-tutorial-for-beginners  
https://qiita.com/TomoyukiAota/items/fd75c28b802bad9e6632  
  
## 3.特徴量エンジニアリング  
ここでは「1」の結果からカラムを一つ一つを深掘りしていき、データから特徴量を作る段階  
臆することなく間違っていても効くことがあるからいっぱい特徴量を作る  
  
### 3-1.groupby系  
・カテゴリ変数でgroupbyをしてから数値変数でmeanやstdを取って、その値で何かの数値変数を割る(もしかしたら四則演算もするのかな？？)  
・groupbyでなんらかの処理をする  
・カテゴリ内の平均  
・
  
### 3-2.その他  
・count,sum,max,min,rollingとかの特徴量作成  
・is_null,is_zero,is_not_zero,over_0.5とかの特徴量作成  
・PolynomialFeaturesでクロスフィーチャーを作る  
・行ごとの統計情報をまとめる(NaNの数,0の数,負の数)  
・「.」や「_」で区切って特徴量にする  
・行ごとにNaNのカウント  
・とりあえず四則演算  
・ビニングでカテゴリカルに  
・trainとtestそれぞれにない値のフラグ  
・NaNとそれ以外の値の特徴量  
・特徴量組み合わせ  
  
### 3-3.外れ値の対処  
・数値変数に対してlog変換やbox-cox変換を使うことで外れ値をならす  
https://www.ten-kara-data.com/how-to-outlier/  
・clipping  
0以下の数値がある時はlog変換できないからこっちを使うといいかも。  
  
### 3-4.参考文献  
・クロスフィーチャー  
http://www.mirandora.com/?p=2505  
  
## 4.特徴量削除(次元削除を含む)  
### 4-1.自動で次元削除  
・heat_mapで相関が高い変数を抜き出してくる、その変数たちをPCAにかける。  
上の動作を分けた変数ごとに何度も繰り返していく。  
・木モデルはNMFという手法のほうが効く可能性はある。  
  
### 4-2.手動で不要な特徴を削除する段階  
・自作のsum_cols_nanで「ほぼ同じ値(9割)」「ほぼnull(9割)」「値が一つしか無い」カラムを削除する  
・相関係数が1(または0.9以上)のうちどちらかのカラムを削除(PCAをした後にやるべき)  
  
## 5.学習できる形と学習しやすい形に変換  
### 5-1.学習できる形  
・カテゴリ変数を手動で全部リスト化してfor文で全部label encoding(trainとtest合わせて)  
・infと-infをNaNに変換  
  
### 5-2.学習しやすい形  
・目的変数をlog変換やbox-cox変換で正規分布に近づける。ただし、平均値が左側にずれていて、右側に裾が長い分布に対してだけ有効。  
・変換前より変換後の方が正規分布に近付いたかを判断するには「QQプロット」を使った後に「シャピロウィルク検定」を使うことで正確に判断できる。  
  
※説明変数にlog変換を使う場合は外れ値をならすために使ってる。決して正規分布に近づけるわけではない。目的変数に使うと正規分布に近づけるために使っている。  
https://qiita.com/flystaslingan40/items/7fe67fb47d88e4811301  
https://www.ten-kara-data.com/how-to-outlier/  
  
## 6.特徴選択  
・再帰的特徴選択(RFE)で特徴量を減らしていく  
・feature_importanceも活用  
  
## 7.validationの選択  
タスクによって方法が異なるので注意。例えば時系列データにはtimesplitで、k-foldしないといけないとか。  
  
## 8.モデル構築、学習、評価、チューニング  
主にGBDTを使うことになると思う  
チューニングはベイズ最適化を行うといいと思う。  
http://www.mirandora.com/?p=2505  
  
## 9.アンサンブル  
スタッキングやブレンディングなど。  
・単純にK-foldしたそれぞれの結果をaveraging  
・多様性を求めるために色々なモデルでアンサンブル  
・後々に色々な特徴量のパターンで作成したそれぞれのモデルをアンサンブル  
  

## 参考文献  
・ieee-cis fraud detection(カーネル1位)  
https://www.kaggle.com/artgor/eda-and-models  
  
・データ分析の色々な手法  
https://qiita.com/TaigoKuriyama/items/8f9286b5c882819adebb#%E5%85%A8%E3%82%AB%E3%83%A9%E3%83%A0%E3%81%AE%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0%E8%A1%A8%E7%A4%BA  
  
・コンペに役立つtips  
https://naotaka1128.hatenadiary.jp/entry/kaggle-compe-tips  
  
・特徴選択の色々な手法  
https://qiita.com/shimopino/items/5fee7504c7acf044a521  