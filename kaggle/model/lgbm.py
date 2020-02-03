import pandas as pd
import numpy as np

import lightgbm as lgb
from sklearn.metrics import log_loss
from sklearn.model_selection import StratifiedKFold

# lightGBMの実装
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
# for文の中でtest結果をappendで保存していって最終的に平均をとればできる気もする。
