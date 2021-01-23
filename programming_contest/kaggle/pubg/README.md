# pubgデータ分析

## 相関性
- 正の相関
  - walkDistance, weaponsAcquired, boosts
- 負の相関
  - killPlace

![image](https://user-images.githubusercontent.com/53253817/105494066-99198580-5cfd-11eb-8338-727f1664d52f.png)

## ビニング
- kills -> 10,20,30,40,50+
- assists -> 
- DBNOs

## メモ
- killPlaceが1位に近づくと、killsは伸びてくる

## わかったこと
### 意外と数値変数からカテゴリ変数に変換することは少ない？？
- カテゴリ変数に変換するのは可視化するために行っている例が多いかも
  - 例えば、年齢層別にデータを見たかったら、0~10歳のようにbinningしてスライシングの材料にするとか
- データに対する深い理解があるならビニングを使ってカテゴリ変数として扱ってもいいれいが多いかもしれない

### 可視化のために数値変数をカテゴリ変数に変換する
- 説明
  - あくまでも可視化をするために行う。本当に外れ値を処理するなら、もっとデータを深掘りする必要がある
  - カテゴリ変数にすることでスライシングの材料などに使えるため、可視化が捗る
  - DataFrameをcopyして作るように(反映されてしまうから)
    - `df_copy = df.copy()`って感じで

1. clippingで水準を減らすことでカテゴリ変数として扱えるようにする方法
  - pandas.quantileを使用
  - 上限や下限を設定することで、水準を一気に減らすことができる

  ```python
  test = pd.DataFrame({"test": [1, 2, 3, 4]})
  test.quantile(0.5) # 2.5
  test.quantile(0.99) # 3.97
  ```

2. binningする方法

### 数値変数ばかりでやれることが少ない場合
- 数値変数をカテゴリ変数に変換して分析を進めてみればいい

### 離散値の場合はカテゴリ変数としても扱っていいかも
- 15未満のデータをカテゴリ変数としていたけど、離散値でカウントすることに意味がありそうならカテゴリ変数として扱ってもいい気がしてきた
- 99パーセントタイルでclippingして水準を少なくしてカテゴリ変数として扱うのもあり

### 外れ値(outlier)を処理するべきか？
- データの性質上ありえないデータなら処理してもいい
- ありえなくない値なら、処理しなくてもいいと思う。GBDTモデルを使うなら線形性とかどうでもいいし。

### pandasのlocが[]でアクセスする理由
- DataFrameをリストのように扱う方法を提供するために`[]`でアクセスする
  - `df.loc[0:20]`のように

### pandasのlocの動作
- `DataFrame.loc[行ラベル, 列ラベル]`
  - 行ラベルと列ラベルを指定してアクセスする
  - ラベルを省略すると、省略した方向が全て選択される

- ラベルにboolean型を渡すと

  ```python
  # boolean型を入れると、Trueのラベルが指定される
  """
              max_speed  shield
  cobra               1       2
  viper               4       5
  sidewinder          7       8
  """
  
  df.loc[True, "max_speed"] # 一行目のcobraが指定されて、max_speed列が指定されるので、「7」が返ってくる
  df.loc[[True, False, True], "shield"] # 一行目のcobraと三行目のsidewinderが指定されるので、「2,8」が返ってくる
  ```

- 指定した列や行を一気に置換する方法
  - `data.loc[data["kills"] > data["kills"].quantile(0.99), "kills"] = "8+"`
    - 第一引数でboolean型のlistが作成されて、Trueだったところを`8+`で置き換えるとしている

- 参考文献
  - https://qiita.com/kazetof/items/992638be821a617b900a

### pandasのgroupbyの使い方(配列をカラムを軸に分割するイメージがわかりやすい)
- groupbyをするとテーブルが複数のテーブルに分割される感じ
  - あえて配列で説明すると`[1,2,3,4,5]` `[[1,2],[3,4,5]]`となるイメージ
  - なので、この状態でカウントを実行すると「2」と「3」が返ってくる

```python
df.groupby(['city', 'food']).mean()

df.groupby("matchId")["matchId"].transform("count")
```

![2021-01-23 4 31のイメージ](https://user-images.githubusercontent.com/53253817/105536649-0516e080-5d34-11eb-9ecf-74849e30ed2e.jpeg)
