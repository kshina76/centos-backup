import pandas as pd
import numpy as np
import warnings

from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings('ignore')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option("display.max_colwidth", 10000)

# メモリ使用量を減らす
# Usage メモリ使用量を減らす
#train = reduce_mem_usage(train)
#test = reduce_mem_usage(test)
def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
    for col in df.columns:
        col_type = df[col].dtype
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return df

# 色々な情報を表示する関数
'''以下の情報を表示する
カラム名 / カラムごとのユニーク値数 / 最も出現頻度の高い値 / 最も出現頻度の高い値の出現回数 /
欠損損値の割合 / 最も多いカテゴリの割合 / dtypes を表示する。
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
    print(stats_df)

# 複数の情報を含んだカラムを分割する
# colは分割したいカラムを一つ選択する。split_symbolは分割する基準の文字を選択する
'''元のコードは以下のように使う
train['OS'] = train['OS_VERSION'].str.split('_', expand=True)[0] 
train['VERSION'] = train['OS_VERSION'].str.split('_', expand=True)[1]
'''
def split_feature(train_x, test_x, col, split_symbol='_'):
    # 初期値はアンダーバーで分割
    return train_x[col].str.split(split_symbol, expand=True)

# 行のNAN数を新しい特徴量に
def count_nans_in_row(train, test):
    train['number_of_NAN_in_row'] = train.isna().sum(axis=1).astype(np.int8)
    test['number_of_NAN_in_row'] = test.isna().sum(axis=1).astype(np.int8)
    return train, test

# trainにあってtestデータにない場合0、ある場合は1
# その逆はtestに加える特徴量
# trainデータにないという特徴量を追加する。決してそのカラムを削除してはダメ。もったいないから
def check_columns_in_another(train, test, col):
    train['col_'+col+'_check_in_test'] = np.where(train[col].isin(test[col]), 1, 0)
    # test の場合は逆
    test['col_'+col+'_check_in_train']  = np.where(test[col].isin(train[col]), 1, 0)
    return train, test

# NANとそれ以外の値の特徴量
# NANの場合は1、それ以外は0
def nan_or_another(train, test, col):
    train['col_'+col+'_nan'] = np.where(train[col].isna(), 1, 0)
    return train

# 数値変数を0以上にシフトする(マイナスが出ないようにしたいときに使う)
# trainとtestのカラムが合っていないとエラーになるので注意。
def shift_higher_than_zero(train, test):
    for col in train.columns:
        if not ((np.str(train[col].dtype)=='category')|(train[col].dtype=='object')):
            min = np.min((train[col].min(), test[col].min()))
            train[col] -= np.float32(min)
            test[col] -= np.float32(min)
    return train, test

# 数値変数の欠損値を-1で埋める
def fill_nan_to_nega(train, test):
    for col in train.columns:
        if not ((np.str(train[col].dtype)=='category')|(train[col].dtype=='object')):
            train[col].fillna(-1, inplace=True)
            test[col].fillna(-1, inplace=True)
    return train, test

# 特徴量同士を結合してLabel Encodingしたものを追加する
# NaNでもできるけどやっていいのかな？それとも処理してからやったほうがいいのかな？
def conb_enc(col1, col2, train, test):
    new_col = col1 + '_' + col2
    train[new_col] = train[col1].astype(str) + '_' + train[col2].astype(str)
    test[new_col] = test[col1].astype(str) + '_' + test[col2].astype(str) 
    le = LabelEncoder()
    le.fit(list(train[new_col].astype(str).values) + list(test[new_col].astype(str).values))
    train[new_col] = le.transform(list(train[new_col].astype(str).values))
    test[new_col] = le.transform(list(test[new_col].astype(str).values)) 
    return train, test

# あるカラム群の欠損の数の合計を特徴量にする
# 例えばAgeとCabinというカラムを選択したときに2つともnanなら2になるし、片方がnanなら1になるし、nanが無ければ0になる
def sum_cols_nan(train, test, col_list):
    train['missing'] = train[col_list].isna().sum(axis=1).astype('int16')
    test['missing'] = test[col_list].isna().sum(axis=1).astype('int16')
    return train, test

train_x = pd.read_csv('./train.csv')
test_x = pd.read_csv('./test.csv')


show_feature_describe(train_x)

#---------------------------------------------後で加工する
# カテゴリ変数のみLabel Encodingする
'''
for col in train.columns:
    if train[col].dtype == 'object':
        le = LabelEncoder()
        le.fit(list(train[col].astype(str).values) + list(test[col].astype(str).values))
        train[col] = le.transform(list(train[col].astype(str).values))
        test[col] = le.transform(list(test[col].astype(str).values))   
'''



