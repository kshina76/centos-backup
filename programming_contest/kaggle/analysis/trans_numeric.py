from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PowerTransformer

import pandas as pd
import numpy as np

'''
リファレンス
standarization : 標準化
min_max : min-maxスケーリング（正規化）
box-cox : 正規分布に近づける（線形回帰やkNNで効くよ。元の分布が正規分布を横にずらしたようなものでないとダメ。マイナスダメ。）
abs, sqrt, power, nega-posi : 基本的な数値変換
clipping : 外れ値に対して有効
binning : 数値変数をカテゴリカル変数に変換する手法
Rank : 大小関係に基づいた順位に変換する手法
RankGauss : Rankに変換したものを正規分布に近づける手法

to do
・ゼロかどうかの二値変数
・数値の端数をとる(価格の100円未満の部分や小数点以下をとる)
・四捨五入、切り上げ、切り捨てを行う
・binning
・Rank
・RankGauss

'''
# 数値に用いる変換(カテゴリカル変数には使わない)
# train_x, test_xはdataframe型。num_colsは数値のカラム名のリスト、trans_typeは変換アルゴリズム名
def transform_numeric(train_x, test_x, num_cols, trans_type):
    if trans_type == "standarization":
        scaler = StandardScaler()
        scaler.fit(train_x[num_cols])
        train_x[num_cols] = scaler.transform(train_x[num_cols])
        test_x[num_cols] = scaler.transform(test_x[num_cols])
        return train_x, test_x

    elif trans_type == "min_max":
        scaler = MinMaxScaler()
        scaler.fit(train_x[num_cols])
        train_x[num_cols] = scaler.transform(train_x[num_cols])
        test_x[num_cols] = scaler.transform(test_x[num_cols])
        return train_x, test_x

    elif trans_type == "box_cox":
        # box-coxはマイナスを想定していないため、プラスのモノだけに対して行う。
        pos_cols = [c for c in num_cols if (train_x[c] > 0.0).all() and (test_x[c] > 0.0).all()]
        pt = PowerTransformer(method='box-cox')
        pt.fit(train_x[pos_cols])
        train_x[pos_cols] = pt.transform(train_x[pos_cols])
        test_x[pos_cols] = pt.transform(test_x[pos_cols])
        return train_x, test_x

    elif trans_type == 'abs':
        train_x[num_cols] = train_x[num_cols].abs()
        test_x[num_cols] = test_x[num_cols].abs()
        return train_x, test_x

    elif trans_type == 'sqrt':
        pos_cols = [c for c in num_cols if (train_x[c] >= 0.0).all() and (test_x[c] >= 0.0).all()]
        train_x[pos_cols] = train_x[pos_cols].apply(np.sqrt)
        test_x[pos_cols] = test_x[pos_cols].apply(np.sqrt)
        return train_x, test_x

    elif trans_type == 'power':
        train_x[num_cols] = train_x[num_cols]**2
        test_x[num_cols] = test_x[num_cols]**2
        return train_x, test_x

    elif trans_type == 'nega-posi':
        # 正の場合は1、負の場合は-1、0は0(0と1の2値にしたほうがいい)
        train_x[num_cols] = train_x[num_cols].apply(np.sign).astype(int)
        test_x[num_cols] = test_x[num_cols].apply(np.sign).astype(int)
        return train_x, test_x

    elif trans_type == 'clipping':
        # 1％点と99％点を計算する
        p01 = train_x[num_cols].quantile(0.01)
        p99 = train_x[num_cols].quantile(0.99)
        # 1％点以下の値は1％点に、99％点以上の値は99％点にclipping
        train_x[num_cols] = train_x[num_cols].clip(p01, p99, axis=1)
        test_x[num_cols] = test_x[num_cols].clip(p01, p99, axis=1)
        return train_x, test_x

# read csv
train_df = pd.read_csv('./train.csv')
test_df = pd.read_csv('./test.csv')
print(train_df)


# Usage
#train_df, test_df = transform_numeric(train_df, test_df, ['PassengerId', 'Pclass'], 'box_cox')
#print(train_df)
#train_df, test_df = transform_numeric(train_df, test_df, ['PassengerId', 'Pclass'], 'abs')
#print(train_df)
#train_df, test_df = transform_numeric(train_df, test_df, ['PassengerId', 'Pclass'], 'sqrt')
#print(train_df)
#train_df, test_df = transform_numeric(train_df, test_df, ['PassengerId', 'Pclass'], 'power')
#print(train_df)
#train_df, test_df = transform_numeric(train_df, test_df, ['PassengerId', 'Pclass'], 'clipping')
#print(train_df)



