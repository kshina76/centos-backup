from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction import FeatureHasher

import pandas as pd
import numpy as np

'''
リファレンス
one-hot : one-hot-encoding
label : label encode
hashing : feature hashingのこと。one-hotのカテゴリ数を少なくしたバージョン。n_featuresが変換後のカテゴリ数で、任意の数を指定していい。

to do
・frequency encoding
・target encoding
・embedding
'''

def transform_categorical(train_x, test_x, cat_cols, trans_type, n_features=5):
    
    if trans_type == 'one-hot':
        # trainとtestを結合してonehotにする
        all_x = pd.concat([train_x, test_x])
        all_x = pd.get_dummies(all_x, columns=cat_cols)

        # trainとtestに再分割
        train_x = all_x.iloc[:train_x.shape[0], :].reset_index(drop=True)
        test_x = all_x.iloc[train_x.shape[0]:, :].reset_index(drop=True)
        return train_x, test_x

    elif trans_type == 'label':
        for c in cat_cols:
            le = LabelEncoder()
            le.fit(train_x[c])
            train_x[c] = le.transform(train_x[c])
            test_x[c] = le.transform(test_x[c])
        return train_x, test_x
    
    elif trans_type == 'hashing':
        for c in cat_cols:
            fh = FeatureHasher(n_features=n_features, input_type='string')
            # 数値は文字列に変換する
            hash_train = fh.transform(train_x[[c]].astype(str).values)
            hash_test = fh.transform(test_x[[c]].astype(str).values)
            # データフレームに変換
            hash_train = pd.DataFrame(hash_train.todense(), columns=[f'{c}_{i}' for i in range(n_features)])
            hash_test = pd.DataFrame(hash_test.todense(), columns=[f'{c}_{i}' for i in range(n_features)])
            # 元のデータフレームと結合
            train_x = pd.concat([train_x, hash_train], axis=1)
            test_x = pd.concat([test_x, hash_test], axis=1)
        # もとのカテゴリ変数を削除
        train_x.drop(cat_cols, axis=1, inplace=True)
        test_x.drop(cat_cols, axis=1, inplace=True)
        return train_x, test_x

# read csv
train_df = pd.read_csv('./train.csv')
test_df = pd.read_csv('./test.csv')
print(train_df)

# Usage
#train_df, test_df = transform_categorical(train_df, test_df, ['Pclass', 'Embarked'], 'one-hot')
#print(train_df)
#train_df, test_df = transform_categorical(train_df, test_df, ['Pclass'], 'label')
#print(train_df)
#train_df, test_df = transform_categorical(train_df, test_df, ['Pclass'], 'hashing')
#print(train_df)
