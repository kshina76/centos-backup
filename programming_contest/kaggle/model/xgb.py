import pandas as pd
import numpy as np

import xgboost as xgb
from sklearn.metrics import log_loss
from sklearn.model_selection import StratifiedKFold


# xgboostによる学習・予測を行うクラス
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

# -----------------------------------
# Stratified K-Fold
# -----------------------------------

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

# 採集結果を出すには、ここでtestデータによる推測をしないとだめ。

