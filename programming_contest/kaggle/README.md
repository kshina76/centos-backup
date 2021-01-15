# データ分析の流れ
- データ分析の手順
  - https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
  - https://towardsdatascience.com/exploratory-data-analysis-eda-techniques-for-kaggle-competition-beginners-be4237c3c3a9
## 0. まずやること
### 0-1. データ収集
- スクレイピングでもいいし、何かしらの方法で
### 0-2. ベースのスコアを出す
1. データセットからユーザidを落とす(これはすぐやる)
2. データセットからtargetを分離する(学習する直前に落とした方がいい多分。)
3. label encodingしてGBDT(lgbm,xgb,cb)でモデル作成
4. submit(これを基準のスコアとする)

## 1. データを理解するためのスプレッドシートを作成と埋める
- スプレッドシートの項目
  - 変数名
  - 変数のタイプ: CategoricalまたはNumeric
  - セグメント: 変数の種類をカテゴリに分ける
    - 「築年数の変数」と「家全体のクオリティ」 -> 家セグメント
  - 期待: 変数の影響の期待値
    - 「高、中、低」の3段階
  - 結論: 変数の影響の結論
    - 「高、中、低」の3段階
  - コメント: 変数に対するコメント、なんでも
- 「期待」の欄の埋め方
  - 自分自身の実世界の経験に基づいて埋める
  - 例えば、木造建築と鉄筋コンクリートのどちらを好むか？とか、築年数はどれくらい気にするか？とか
- 「結論」の欄の埋め方
  - 「それぞれの変数」と「ターゲット変数」の間で散布図を描いて、結論を埋める
  - 後述する3で説明している
- このスプレッドシートを埋めることで、変数への深い理解や、いらない変数の削除に踏み切ることができる

## 2. データ確認
1. データの型を調べる(floatとかintとかobjectとか)
  
  ```python
  '''以下の情報を表示する
  カラム名 / カラムごとのユニーク値数 / 最も出現頻度の高い値 / 最も出現頻度の高い値の出現回数 /
  欠損損値の割合 / 最も多いカテゴリの割合 / dtypes
  '''
  def show_feature_describe(train):
    stats = []
    for col in train.columns:
        stats.append((col,
                    train[col].nunique(),
                    train[col].value_counts().index[0],
                    train[col].value_counts().values[0],
                    train[col].isnull().sum() * 100 / train.shape[0],
                    train[col].value_counts(normalize=True, dropna=False).values[0] * 100,
                    train[col].dtype))
    stats_df = pd.DataFrame(stats, columns=['Feature', 'Unique values', 'Most frequent item', 'Freuquence of most frequent item', 'Percentage of missing values', 'Percentage of values in the biggest category', 'Type'])
    stats_df.sort_values('Percentage of missing values', ascending=False)
    return stats_df
  ```

2. 1で調べた情報からデータタイプを推測して以下のデータタイプに振り分ける
  - Numeric
  - Categorical/Ordinal
  - Datetime
  - Coordinates
3. データタイプごとにカラム名をリストにまとめておく
  - あとで使うと思う

## 3. 可視化
### 3-1. ターゲット変数についての可視化
1. describeでありえない数字が入っていないかを最小値などを見て調べる
  - `df_train["target"].describe()`
2. ヒストグラム
  - `sns.distplot(df_train["target"])`
  - `print("Skewness: %f" % df_train["target"].skew())`
  - `print("Kurtosis: %f" % df_train["target"].kurt())`
  - 正規分布からずれていないか？
  - 正の歪度か？、負の歪度か？
    - 正の歪度はヒストグラムが左にずれている。負は右
  - 尖度(ピーク)はどのくらいか？
  - https://bellcurve.jp/statistics/course/17950.html
### 3-2. ターゲット変数と数値変数の関係
- `data = pd.concat([df_train["target"], df_train["relation"]], axis=1)`
- `data.plot.scatter(x="relation", y="target", ylim=(0,800000))`
- どのような相関があるか？
- 線形的か？指数的か？
### 3-3. ターゲット変数とカテゴリカル変数の関係
- pairplotやboxplotで相関や規則性を見る
### 3-4. その他
- カテゴリをcountplotで出現回数を可視化  
- 数値をdistplotwで出現回数を可視化  
- カテゴリ(x軸)×数値(y軸)で可視化していく。pairplotやboxplotで相関や規則性を見る。  
- 数値×数値で可視化していく。pairplotなど。  
### 参考文献  
・可視化での詳しいメモは後述する「可視化でわかったこと」を参照  
・可視化は以下の方法から必要なものを選んでいけばいいと思う。  
https://www.kaggle.com/kralmachine/seaborn-tutorial-for-beginners  
https://www.kaggle.com/kanncaa1/seaborn-tutorial-for-beginners  
https://qiita.com/TomoyukiAota/items/fd75c28b802bad9e6632  

## 4. 可視化: 相関
### 4-1. 全変数のヒートマップ

```python
corrmat = df_train.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
```

- 明らかに相関が高い(白色で表示されている)変数は何か？
  - 多重共線性(マルチコ)が発生していることを観測できるので便利
- 多重共線性があるとなぜダメなのか
  - https://yolo-kiyoshi.com/2019/05/27/post-1160/
### 4-2. ターゲット変数とのヒートマップ
- ターゲット変数との相関が高いものtop10を抜き出す

```python
#saleprice correlation matrix
k = 10 #number of variables for heatmap
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()
```

- 相関が高いことから重要な変数がわかる

## 5. 可視化: 散布図
- 4で調べたターゲット変数と相関が高いものtop10の間で散布図をプロットする

```python
#scatterplot
sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(df_train[cols], size = 2.5)
plt.show()
```

- ドットが連なって境界線(上限、下限)を描いていないか？

## 6. データクリーニング
### 6-1. 欠損データの処理
```python
#missing data
total = df_train.isnull().sum().sort_values(ascending=False)
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)
```

- 欠損データを考えるときに重要な項目
  - 欠損データはどの程度あるのか？
  - 欠損データはランダムなのか？、パターンがあるのか？
- この段階で1~5でいらないと判断された変数もまとめて削除する
- 欠損データがあって削除するもの
  - 相関が高かった同士の変数の中で欠損値が少ないものだけを残して、それ以外は削除する
- 欠損データがあっても削除しないもの
  - 「ほんの少ししか欠損データがない」かつ「他の変数と相関がないことから、あったほうがモデルの表現力が上がる可能性があるもの」
    - この場合は欠損しているところの「行」だけを削除するといった方針を取る

### 6-2. 外れ値の処理
- ターゲット変数と説明変数の間で散布図を書いて、外れ値を目視して削除する

## 7. データの深堀
- ここまでで、データのクリーニングとデータの理解が終わっていて、ここからはさらにデータを深堀していく
- 検証するべき4つの仮定
  - 正規性
    - データが正規分布にしたがっているように見えるかどうか
    - したがっていなかったらlogをとるとか
  - 同種混合性
    - 従属変数（複数可）が予測変数（複数可）の範囲にわたって等しいレベルの分散を示すという仮定
  - 線形性
    - 散布図を調べて線形パターンを探す
    - パターンが線形でない場合は、データ変換を探索する価値がある
  - 相関誤差の不在
    - わからん

```python
#transformed histogram and normal probability plot
sns.distplot(df_train['SalePrice'], fit=norm)
fig = plt.figure()
res = stats.probplot(df_train['SalePrice'], plot=plt)
```

## 3.特徴量エンジニアリング  
- 以下のデータごとの処理方法がまとまっている
  - Numeric
  - Categorical/Ordinal
  - Datetime
  - Coordinates
  - https://ishitonton.hatenablog.com/entry/2019/02/24/184253



---

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
- ieee-cis fraud detection(カーネル1位)
  - https://www.kaggle.com/artgor/eda-and-models
- データ分析の色々な手法  
  - https://qiita.com/TaigoKuriyama/items/8f9286b5c882819adebb#%E5%85%A8%E3%82%AB%E3%83%A9%E3%83%A0%E3%81%AE%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0%E8%A1%A8%E7%A4%BA  
- コンペに役立つtips
  - https://naotaka1128.hatenadiary.jp/entry/kaggle-compe-tips
- 特徴選択の色々な手法
  - https://qiita.com/shimopino/items/5fee7504c7acf044a521
