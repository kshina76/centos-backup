# データ分析の流れ
- データ分析の手順
  - https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
  - https://towardsdatascience.com/exploratory-data-analysis-eda-techniques-for-kaggle-competition-beginners-be4237c3c3a9
  - https://qiita.com/hkthirano/items/12e046b3e02961d8460d
  - https://data-bunseki.com/2019/08/19/kaggle%EF%BC%9Ahouse-price-%E3%83%81%E3%83%A5%E3%83%BC%E3%83%88%E3%83%AA%E3%82%A2%E3%83%ABeda%E6%8E%A2%E7%B4%A2%E7%9A%84%E3%83%87%E3%83%BC%E3%82%BF%E8%A7%A3%E6%9E%90/#i-10

## 大まかな解析手法
- 単変量解析
  - 1つの変数だけを取り上げて解析すること
  - 平均や中央値といった数字で分析を行うことも可能だが、数字だけを見ていてもわかりにくいので、通常はヒストグラムや箱ひげ図で視覚化して分析する
- 二変量解析
  - 二変数間を解析すること
  - 二変量解析では、通常、相関係数を求めて分析を行うが、視覚化としては散布図、そしてクロス集計表もよく用いられる
- 多変量解析
  - 重回帰分析やクラスタリングといった、3つ以上の変数が絡む解析

![2021-01-20 22 39のイメージ](https://user-images.githubusercontent.com/53253817/105182455-63936180-5b70-11eb-88c1-69d5cd5995b1.jpeg)

![2021-01-20 22 40のイメージ](https://user-images.githubusercontent.com/53253817/105182597-90477900-5b70-11eb-9f73-2ecdb6581977.jpeg)


## TOOD
- 単変量、二変量、多変量の解説と種類など色々まとまっている
  - https://www.intage.co.jp/glossary/056/
- アンサンブル、スタッキング
  - https://qiita.com/hkthirano/items/2c35a81fbc95f0e4b7c1
- 対数変換、Box-Cox変換、Yeo-Johnson変換
  - 正規分布にしたがっていない場合の変換方法

## 0. まずやること
### 0-1. 方針
- 基本的に単変量解析と二変量解析を行ってから、多変量解析をするという手順になる
  - これは一般的なデータ分析の流れ

### 0-2. データ収集
- スクレイピングでもいいし、何かしらの方法で

### 0-3. モデルの評価指標の決定
- 評価指標が目的関数にそのまま使えるものなら、そのまま使うのがいい
- 評価指標が微分不可能なもので、別の目的関数を用意する必要があるなら、kaggle本を参照する

### 0-4. ベースのスコアを出す
1. データセットからユーザidを落とす(これはすぐやる)
2. データセットからtargetを分離する(学習する直前に落とした方がいい多分。)
3. label encodingしてGBDT(lgbm,xgb,cb)でモデル作成
4. submit(これを基準のスコアとする)

<br></br>

## 1. データ理解
### 1-1. スプレッドシートを作成して埋める
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
### 1-2. 自分の経験から仮説を立てる
- 考える点
  - ターゲット変数に対してこの特徴量を考慮すると効きそうか？
  - もし考慮するなら、その程度は？
  - 似たような特徴量はなかったか？
- 方法
  - 「メモ書き」でブレインストーミングのようにアイデアを出すといいかも
### 1-3. 影響度の高そうな変数とそうでない変数に分ける
- 期待が高い変数は後述する「3」で可視化する
- 期待が低い変数は後述する「4」で可視化する
- 期待が低いと思っていたけど、「4」で高いに変更されたものを深掘りする

<br></br>

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

2. 1で調べた情報からデータタイプを推測して以下のデータタイプに振り分ける(とりあえずNumericとCategoricalでいいかも)
  - Numeric
  - Categorical/Ordinal
  - Datetime
  - Coordinates
  - 質的変数か量的変数かの判断は「質問の仕方による」
    - http://www.rikkyo.ne.jp/web/ymatsumoto/socdata09/socdata0901.pdf
3. データタイプごとにカラム名をリストにまとめておく
  - あとで使うと思う
  - 一気にプロットしたいときなどに便利
    - ユニークな値が多すぎるとプロットできないので、1で調べた変数からあたりをつけておく

<br></br>

## 3. 可視化: 期待が高い変数
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
- pairplotやboxplotで相関や規則性や傾向を見る

```python
#box plot overallqual/saleprice
var = 'OverallQual'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000)
```

![f3cd6ec84b47032c400f563e80cdca34](https://user-images.githubusercontent.com/53253817/105173918-1231a500-5b65-11eb-8643-08005449ac81.png)

```python
var = 'YearBuilt'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000)
plt.xticks(rotation=90)
```

![3ce436f04ca45fafceefeb757daa9c7b](https://user-images.githubusercontent.com/53253817/105173922-12ca3b80-5b65-11eb-88b1-d15f1b8795bb.png)

### 3-4. その他
- カテゴリをcountplotで出現回数を可視化  
- 数値をdistplotで出現回数を可視化  
- カテゴリ(x軸)×数値(y軸)で可視化していく。pairplotやboxplotで相関や規則性を見る。  
- 数値×数値で可視化していく。pairplotなど。  
### 参考文献  
- 可視化での詳しいメモは後述する「可視化でわかったこと」を参照  
- 可視化は以下の方法から必要なものを選んでいけばいいと思う。  
  - https://www.kaggle.com/kralmachine/seaborn-tutorial-for-beginners  
  - https://www.kaggle.com/kanncaa1/seaborn-tutorial-for-beginners  
  - https://qiita.com/TomoyukiAota/items/fd75c28b802bad9e6632  

<br></br>

## 4. 可視化: 期待が低い変数
- 大まかな手順
  - 相関行列により全体の相関性を把握
  - ターゲット変数と相関の強い特徴量に絞る
  - 散布図で関係を確認
### 4-1. 全体の相関性の可視化
1. 明らかにターゲット変数と相関が高い(白色で表示されている)変数は何か？
2. 期待が低いと思っていたのに、ターゲット変数との相関が高い変数は何か？
3. なぜその結果になるのかを現実世界の観点から仮説を立てる
  - 説明を求められた時や、新しい特徴量を作成するときに役立つ

```python
corrmat = df_train.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
```

### 4-2. ターゲット変数相関が強い特徴量の可視化
1. ターゲット変数との相関が高いものtop10を以下で抜き出す
  - 下記のコードで表示できる
2. 多重共線性(マルチコ)が発生していないか？
  - 説明変数同士の相関が高い場合に多重共線性が発生していると判断する
3. なぜその結果になるのかを現実世界の観点から仮説を立てる
  - 説明を求められた時や、新しい特徴量を作成するときに役立つ

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
- 多重共線性があるとなぜダメなのか
  - https://yolo-kiyoshi.com/2019/05/27/post-1160/
### 4-3. 散布図で関係を確認
1. ドットが連なって境界線(上限、下限)を描いていないか？
2. 線形的に増減しているのか？
3. 指数的に増減しているのか？

- 4-2で調べたターゲット変数と相関が高いものtop10から多重共線性が発生しているものを除いた変数間で散布図をプロットする

```python
#scatterplot
sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(df_train[cols], size = 2.5)
plt.show()
```

<br></br>

## 5. 可視化: 期待が低いから高いに変更された変数
- あとでまとめる

<br></br>

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
1. 単変量解析
  - ターゲット変数のみについての外れ値を見る
2. 二変量解析
  - 散布図を使って、ターゲット変数と特徴量の間の関係をプロットする(前述でやってきた作業の図を使う)
  - 外れ値を目視して削除する
  - 外れ値の定義は感覚

<br></br>

## 7. 多変量解析できるかどうかの確認
- ここからはターゲット変数に対して多変量解析を適用することができるかを確認していく
  - 多変量解析とは、要はモデルを学習して予測させるということ
### 7-1. 検証するべき4つの仮定
- 正規性
  - データが正規分布にしたがっているように見えるかどうか
  - したがっていなかったら対数変換をするとか
    - 正の歪度がある場合は対数変換が有効
- 等分散性
  - 全変数において分散が同じレベルであることが望まれる
  - プロットの広がりがどの場所も等しくなることが、等分散性であるということ

  ![https---qiita-image-store s3 amazonaws com-0-247972-9ff48625-5962-c18a-2656-af21493d9b53](https://user-images.githubusercontent.com/53253817/105184231-73ac4080-5b72-11eb-82b4-a73c8d846d9d.jpeg)

- 線形性
  - 散布図を調べて線形パターンになっていることが望まれる
  - パターンが線形でない場合は、データ変換を探索する価値がある
- 相関誤差の欠如
  - 時系列データの場合に注意すべきらしい
  - よくわからん

```python
#transformed histogram and normal probability plot
sns.distplot(df_train['SalePrice'], fit=norm)
fig = plt.figure()
res = stats.probplot(df_train['SalePrice'], plot=plt)
```

<br></br>

## 8. 学習
### 8-1. モデルの選択
- 基本的にGBDTを使用することになる
  - XGBとかLGBMとか
### 8-2. 交差検証のデータを作成
- K-foldとかtime-splitとか

<br></br>

## 9. 特徴量エンジニアリング
- 8までですある程度のを出すことができた後に、さらにスコアをあげる時に行う
- とりあえずkaggle本の第3章を見ながら進めればいいと思う
- 以下のデータごとの処理方法がまとまっている
  - Numeric
  - Categorical/Ordinal
  - Datetime
  - Coordinates
  - https://ishitonton.hatenablog.com/entry/2019/02/24/184253
### 9-1. 数値変数の変換
#### 9-1-1. 線形変換: 分布の伸縮
- 標準化
  - 使用する場面
    - 線形回帰やロジスティック回帰などの線形モデルの場合
    - ニューラルネットの場合
    - 二値変数以外
- Min-Maxスケーリング
  - 用途としては標準化と同じだが、外れ値の影響を受けやすいため標準化の方が使用される
#### 9-1-2. 非線形変換: 分布の形状変換
- logx変換
  - 0が含まれていると使用できない
- log(x+1)変換
  - 変数に0が含まれている場合に使用できる
- Box-Cox変換
- Yeo-Johnson変換
- generalized-log-transformation
  - あまり使われていない
- その他
  - 絶対値、平方根、二乗、n乗、
  - 正の値かどうか、ゼロかどうかなどの二値変数
  - 数値の端数を取る
  - 四捨五入、切り上げ、切り捨て
#### 9-1-3. clipping
- 上限下限を設定して、外れ値を上限か下限に丸める
#### 9-1-4. binning
- 数値変数を区間で分割してカテゴリ変数として扱う方法
#### 9-1-5. 順位への変換
- 数値変数から大小関係飲みに注力して抽出する方法
#### 9-1-6. Rank-Gauss
- 数値を順位に変換した後に、順位を保ったまま正規分布に近づける手法
### 9-2. カテゴリ変数の変換
- 変数が文字列でなくても、値の大きさや順序に意味がない場合はカテゴリ変数として扱う
#### 9-2-1. one-hot encoding
- n個の水準を持つカテゴリ変数をn個の二値変数に変換する方法
- カテゴリ変数の水準が多すぎる場合は以下の方法を検討
  - 別のencoding
  - カテゴリ変数をグルーピングして水準を減らしてからone-hot encoding
  - 頻度の少ないカテゴリを「その他のカテゴリ」にまとめる
#### 9-2-2. label encoding
- 水準を整数に置き換えるだけ
- GBDTを使う場合は、この方法が一般的
#### 9-2-3. feature hashing
- あまり使われない
#### 9-2-4. frequency encoding
- 出現回数、出現頻度でカテゴリ変数を置き換える方法
- 出現回数とターゲット変数の間に関係がある場合は有効
#### 9-2-5. target encoding
- リークする可能性があるから十分に注意して使う
#### 9-2-6. embedding
#### 9-2-7. 順序変数の扱い
- 順序を保ちながら整数に変換すればいいだけ
#### 9-2-8. カテゴリ変数の分割
- 型番などの「ABC-10002」などは「ABC」と「10002」に分割する
  - そのままencodingしてしまうと型番の情報が減ってしまうから
### 9-3. 日付・時刻を表す変数の変換
#### 9-3-1. 年・月・日
- 年
- 月
  - 季節性を取り入れることができる
- 日
#### 9-3-2. 年月・月日
- 年月
- 月日
#### 9-3-3. 曜日・祝日
- 曜日
- 祝日
#### 9-3-4. 特別な日
- クリスマスなど
#### 9-3-5. 時・分・秒
- 時
- 分
- 秒
#### 9-3-6. 時間差
- 家が建てられてからどれだけ経ったかなど
### 9-4. 変数の組み合わせ
- データの知識を使って、どの組み合わせが効果がありそうかという仮説を立てながら行う
#### 9-4-1. 数値変数 × カテゴリ変数
- カテゴリ変数の水準ごとに、数値変数の平均や分散といった統計量をとる
- カテゴリ変数の水準ごとに、数値変数の値を絞る
#### 9-4-2. 数値変数 × 数値変数
- 数値変数同士を加減乗除したり、あまりを出したり、二つの値が同じかどうかを特徴量にしたり
- 例えば、物件の面積と部屋数で割るとか
- GBDTは加減より乗除をモデルに反映しづらいから、乗除を特徴量に加えると良かったりする
#### 9-4-3. カテゴリ変数 × カテゴリ変数
- 水準がかなり増えることに注意して使う
#### 9-4-4. 行の統計量をとる
- 欠損値、ゼロ、負の値をカウント
- 平均、分散、最大、最小
### 9-5. 他のテーブルの結合
- kaggleなどで複数のcsvファイルに分割されていたりするから、それを結合する
### 9-6. 集約して統計量をとる
- 1対多のデータの時に使用する
- 例えば、ユーザIDと購入商品は1対多の関係なので、ユーザIDごとにgroupbyして平均やカウントなどの統計量をとる
- ユーザIDだけでなくて、カテゴリ変数を基準にgroupbyするならなんでも良い
- 詳しくはkaggle本P166〜
### 9-7. 時系列データの扱い
- 多いのであとで
### 9-8. 次元削減・教師なし学習を使った特徴量
#### 9-8-1. PCA
- 次元削減
#### 9-8-2. NMF
#### 9-8-3. LDA
#### 9-8-4. t-SNE
- 次元削減
#### 9-8-5. UMAP
- 次元削減
#### 9-8-6. オートエンコーダー
- ニューラルネットを使った次元圧縮
#### 9-8- クラスタリング
- クラスタリングして出てきた結果をカテゴリ変数として使う
- または、クラスタ中心からの距離を特徴量に使うこともできる
### 9-10. その他のテクニック


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
