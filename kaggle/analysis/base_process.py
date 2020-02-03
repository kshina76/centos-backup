import pandas as pd
import numpy as np

from sklearn.feature_selection import VarianceThreshold

'''
わかったこと
・特徴量選択はobject型を数値に直したり、下準備が終わったらやること。なぜならobject型のままだと処理できないことがあるから。
・object型などは適宜label encodeなどが済んでから。

リファレンス

参考文献
・特徴量選択手法まとめ
https://qiita.com/shimopino/items/5fee7504c7acf044a521
・データ分析まとめ
https://naotaka1128.hatenadiary.jp/entry/kaggle-compe-tips

'''

# nullのカラムを表示して、nullのカラム名を抜き出してくる関数
def is_null(train_x, test_x):
    print(' ')
    print('train_x columns is null')
    print(train_x.isnull().sum())
    print(' ')
    print('test_x columns is null')
    print(test_x.isnull().sum())
    print(' ')
    print('train_x and test_x columns is null')
    print(pd.concat([train_x, test_x]).isnull().sum())
    print(' ')
    null_cols_train = [col for col in train_x.columns if train_x[col].isnull().sum() > 0]
    null_cols_test = [col for col in test_x.columns if test_x[col].isnull().sum() > 0]
    return null_cols_train, null_cols_test

# 完全に重複しているカラムのうち片方のカラムを削除する
def remove_duplicated_columns(train_x, test_x):
    remove = []
    c = train_x.columns
    for i in range(len(c)-1):
        v = train_x[c[i]].values
        for j in range(i+1,len(c)):
            if np.array_equal(v,train_x[c[j]].values):
                remove.append(c[j])
    train_x.drop(remove, axis=1, inplace=True)
    test_x.drop(remove, axis=1, inplace=True)
    return train_x, test_x

# すべてのデータが同じカラムを削除する(すべて0とか)、Object型を判定するとエラーが出るからラベルエンコードしてからやる(多分)
# stdは標準偏差を計算する。標準偏差が0はすべて同じデータであることを表す。
def remove_constant_columns(train_x, test_x):
    remove = []
    for col in train_x.columns:
        if train_x[col].std() == 0:
            remove.append(col)
    train_x.drop(remove, axis=1, inplace=True)
    test_x.drop(remove, axis=1, inplace=True)
    return train_x, test_x

# カラム間で高い相関があるものは削除する(targetと相関があるものは残す)
def remove_high_corr(train_x, test_x):
    threshold = 0.8
    feat_corr = set()
    corr_matrix = train_x.corr()
    print(corr_matrix)
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                feat_name = corr_matrix.columns[i]
                feat_corr.add(feat_name)
    train_x.drop(labels=feat_corr, axis=1, inplace=True)
    test_x.drop(labels=feat_corr, axis=1, inplace=True)
    return train_x, test_x


train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')



# Usage
# is_null(train_df, test_df)

#null_cols_train, null_cols_test = is_null(train_df, test_df)
#print(null_cols_train)

#print(len(train_df.columns))
#train_x, test_x = remove_high_corr(train_df, test_df)
#print(len(train_x.columns))
