import pandas as pd
import numpy as np

from sklearn.model_selection import KFold

# xgboostによる学習・予測を行うクラス
import xgboost as xgb
from sklearn.metrics import log_loss


class Model:
    def __init__(self, params=None):
        self.model = None
        if params is None:
            self.params = {}
        else:
            self.params = params

    def fit(self, tr_x, tr_y, va_x, va_y):
        params = {'objective': 'binary:logistic', 'silent': 1, 'random_state': 71}
        # インスタンスに渡されたparamsで更新する。空辞書の場合は、何も更新されない。
        params.update(self.params)
        num_round = 10
        dtrain = xgb.DMatrix(tr_x, label=tr_y)
        dvalid = xgb.DMatrix(va_x, label=va_y)
        watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
        self.model = xgb.train(params, dtrain, num_round, evals=watchlist)

    def predict(self, x):
        data = xgb.DMatrix(x)
        pred = self.model.predict(data)
        return pred

# lightGBMの実装
import lightgbm as lgb
from sklearn.metrics import log_loss

class Model:
    def __init__(self, params=None):
        self.model = None
        if params is None:
            self.params = {}
        else:
            self.params = params

    def fit(self, tr_x, tr_y, va_x, va_y):
        # ハイパーパラメータの設定
        params = {'objective': 'binary', 'seed': 71, 'verbose': 0, 'metrics': 'binary_logloss'}
        # インスタンスに渡されたparamsで更新する。空辞書の場合は、何も更新されない。
        params.update(self.params)
        num_round = 10
        lgb_train = lgb.Dataset(tr_x, tr_y)
        lgb_eval = lgb.Dataset(va_x, va_y)
        categorical_features = ['product', 'medical_info_b2', 'medical_info_b3']
        self.model = lgb.train(params, lgb_train, num_boost_round=num_round,
                              categorical_feature=categorical_features,
                              valid_names=['train', 'valid'], valid_sets=[lgb_train, lgb_eval])
    def predict(self, x):
        data = lgb.Dataset(x)
        pred = self.model.predict(data)
        return pred

#---------------------------------------------------------------------------------------------
# データの読み込みと目標変数を分ける
train = pd.read_csv('./train.csv')
train_x = train.drop(['target'], axis=1)
train_y = train['target']
test_x = pd.read_csv('./test.csv')

# -----------------------------------
# hold-out法
# -----------------------------------
# hold-out法でのバリデーションデータの分割

from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split

# train_test_split関数を用いてhold-out法で分割する
tr_x, va_x, tr_y, va_y = train_test_split(train_x, train_y,
                                          test_size=0.25, random_state=71, shuffle=True)

# 学習の実行、バリデーションデータの予測値の出力、スコアの計算を行う
model = Model()
model.fit(tr_x, tr_y, va_x, va_y)
va_pred = model.predict(va_x)
score = log_loss(va_y, va_pred)
print(score)

# 予測
pred = model.predict(test_x)


# -----------------------------------
# kfold法
# -----------------------------------
# KFoldクラスを用いてバリデーションデータを分割

from sklearn.model_selection import KFold
from sklearn.metrics import log_loss

scores = []

# KFoldクラスを用いてクロスバリデーションの分割を行う
kf = KFold(n_splits=4, shuffle=True, random_state=71)
for tr_idx, va_idx in kf.split(train_x):
    tr_x, va_x = train_x.iloc[tr_idx], train_x.iloc[va_idx]
    tr_y, va_y = train_y.iloc[tr_idx], train_y.iloc[va_idx]

    # 学習の実行、バリデーションデータの予測値の出力、スコアの計算を行う
    model = Model()
    model.fit(tr_x, tr_y, va_x, va_y)
    va_pred = model.predict(va_x)
    score = log_loss(va_y, va_pred)
    scores.append(score)

# 各foldのスコアの平均をとる
print(np.mean(scores))


# -----------------------------------
# Stratified K-Fold
# -----------------------------------
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import log_loss

scores = []

# StratifiedKFoldクラスを用いて層化抽出による分割を行う
kf = StratifiedKFold(n_splits=4, shuffle=True, random_state=71)
for tr_idx, va_idx in kf.split(train_x, train_y):
    tr_x, va_x = train_x.iloc[tr_idx], train_x.iloc[va_idx]
    tr_y, va_y = train_y.iloc[tr_idx], train_y.iloc[va_idx]

    # 学習の実行、バリデーションデータの予測値の出力、スコアの計算を行う
    model = Model()
    model.fit(tr_x, tr_y, va_x, va_y)
    va_pred = model.predict(va_x)
    score = log_loss(va_y, va_pred)
    scores.append(score)

# 各foldのスコアの平均をとる
print(np.mean(scores))


# -----------------------------------
# leave-one-out
# -----------------------------------
# データが極めて少ないタスクに対して効果を発揮する
# データが100件しかないものとする
train_x = train_x.iloc[:100, :].copy()
# -----------------------------------
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import log_loss

scores = []

loo = LeaveOneOut()
for tr_idx, va_idx in loo.split(train_x):
    tr_x, va_x = train_x.iloc[tr_idx], train_x.iloc[va_idx]
    tr_y, va_y = train_y.iloc[tr_idx], train_y.iloc[va_idx]

    # 学習の実行、バリデーションデータの予測値の出力、スコアの計算を行う
    model = Model()
    model.fit(tr_x, tr_y, va_x, va_y)
    va_pred = model.predict(va_x)
    score = log_loss(va_y, va_pred)
    scores.append(score)

# 各foldのスコアの平均をとる
print(np.mean(scores))


# -----------------------------------
# GroupKFold
# -----------------------------------
# 4件ずつ同じユーザーがいるデータであったとする
train_x['user_id'] = np.arange(0, len(train_x)) // 4
# -----------------------------------

from sklearn.model_selection import KFold, GroupKFold

# user_id列の顧客IDを単位として分割することにする
user_id = train_x['user_id']
unique_user_ids = user_id.unique()

# KFoldクラスを用いて、顧客ID単位で分割する
scores = []
kf = KFold(n_splits=4, shuffle=True, random_state=71)
for tr_group_idx, va_group_idx in kf.split(unique_user_ids):
    # 顧客IDをtrain/valid（学習に使うデータ、バリデーションデータ）に分割する
    tr_groups, va_groups = unique_user_ids[tr_group_idx], unique_user_ids[va_group_idx]

    # 各レコードの顧客IDがtrain/validのどちらに属しているかによって分割する
    is_tr = user_id.isin(tr_groups)
    is_va = user_id.isin(va_groups)
    tr_x, va_x = train_x[is_tr], train_x[is_va]
    tr_y, va_y = train_y[is_tr], train_y[is_va]

# （参考）GroupKFoldクラスではシャッフルと乱数シードの指定ができないため使いづらい
kf = GroupKFold(n_splits=4)
for tr_idx, va_idx in kf.split(train_x, train_y, user_id):
    tr_x, va_x = train_x.iloc[tr_idx], train_x.iloc[va_idx]
    tr_y, va_y = train_y.iloc[tr_idx], train_y.iloc[va_idx]
