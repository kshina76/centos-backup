from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import scipy.sparse
import pandas as pd
import numpy as np
import talib as ta
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    roc_auc_score,
    precision_recall_curve,
    auc,
    roc_curve,
)
from sklearn.model_selection import GridSearchCV

# APIキー、environmentはデモか本番か
oanda_api = API(access_token=access_token, environment="practice")


# oandaAPIを叩いて、いろいろな形のデータを返すクラス
class DataFromOanda:
    def __init__(self, instrument="USD_JPY", params=None):
        self.instrument = instrument
        self.params = params

    # oandaAPIからデータを取得する
    def get_candles(self):
        """
            足データを取得してDataFrameに変換
        """
        instruments_candles = instruments.InstrumentsCandles(
            instrument=self.instrument, params=self.params
        )

        oanda_api.request(instruments_candles)
        response = instruments_candles.response  # json型
        df = pd.DataFrame(response["candles"])  # response["candles"]はlist型

        return df

    # oandaAPIから5000件を超える足データの取得(日付とか色々ついている)
    def get_candles_over5000(self, nb_itr=1):
        candles = None
        for i in range(nb_itr):
            new_candles = self.get_candles()
            params["to"] = new_candles["time"].iloc[0]
            print(params["to"])
            candles = pd.concat([new_candles, candles])
        return candles

    # 終値のリストを返す
    def get_close_price_over5000(self, nb_itr=1):
        candles = self.get_candles_over5000(nb_itr)
        if self.params["price"] == "M":
            bid_ask_mid = "mid"
        elif self.params["price"] == "A":
            bid_ask_mid = "ask"
        elif self.params["price"] == "B":
            bid_ask_mid = "bid"

        candles_price = candles[bid_ask_mid]
        candles_price_list = list(candles_price)

        return [float(dict(i)["c"]) for i in candles_price_list]


# 「cur_pos-period ~ cur_pos+1」の期間でmaを計算する
# 単純20日移動平均（20SMA)であれば、本日を含めた過去20日間の終値を合計し、日数の20で割って平均
# cur_posは本日を表す。
def get_ma(price_arr, cur_pos, period=20):
    if cur_pos <= period:
        # s = 0
        return 0
    else:
        s = cur_pos - period + 1
    tmp_arr = price_arr[s : cur_pos + 1]  # cur_posってなってたけど、+1しないとだめじゃない？？
    # tmp_arr.reverse() これ要らなくね？？
    prices = np.array(tmp_arr, dtype=float)
    return ta.SMA(prices, timeperiod=period)[-1]


def get_rsi(price_arr, cur_pos, period=40):
    if cur_pos <= period:
        # s = 0
        return 0
    else:
        s = cur_pos - period + 1
    tmp_arr = price_arr[s : cur_pos + 1]
    # tmp_arr.reverse()
    prices = np.array(tmp_arr, dtype=float)
    return ta.RSI(prices, timeperiod=period)[-1]


def get_ma_kairi(price_arr, cur_pos, period=None):
    ma = get_ma(price_arr, cur_pos)
    return ((price_arr[cur_pos] - ma) / ma) * 100.0
    return 0


def get_bb_1(price_arr, cur_pos, period=40):
    if cur_pos <= period:
        # s = 0
        return 0
    else:
        s = cur_pos - period + 1
    tmp_arr = price_arr[s : cur_pos + 1]
    # tmp_arr.reverse()
    prices = np.array(tmp_arr, dtype=float)
    return ta.BBANDS(prices, timeperiod=period)[0][-1]


def get_bb_2(price_arr, cur_pos, period=40):
    if cur_pos <= period:
        # s = 0
        return 0
    else:
        s = cur_pos - period + 1
    tmp_arr = price_arr[s : cur_pos + 1]
    # tmp_arr.reverse()
    prices = np.array(tmp_arr, dtype=float)
    return ta.BBANDS(prices, timeperiod=period)[2][-1]


def get_ema(price_arr, cur_pos, period=20):
    if cur_pos <= period:
        # s = 0
        return 0
    else:
        s = cur_pos - period + 1
    tmp_arr = price_arr[s : cur_pos + 1]
    tmp_arr.reverse()
    prices = np.array(tmp_arr, dtype=float)
    return ta.EMA(prices, timeperiod=period)[-1]


def get_ema_rsi(price_arr, cur_pos, period=None):
    return 0


def get_cci(price_arr, cur_pos, period=None):
    return 0


def get_mo(price_arr, cur_pos, period=20):
    if cur_pos <= (period + 1):
        return 0
    else:
        s = cur_pos - period + 1
    tmp_arr = price_arr[s : cur_pos + 1]
    # tmp_arr.reverse()
    prices = np.array(tmp_arr, dtype=float)

    return ta.CMO(prices, timeperiod=period)[-1]


def get_po(price_arr, cur_pos, period=10):
    if cur_pos <= period:
        # s = 0
        return 0
    else:
        s = cur_pos - period + 1
    tmp_arr = price_arr[s : cur_pos + 1]
    # tmp_arr.reverse()
    prices = np.array(tmp_arr, dtype=float)
    return ta.PPO(prices)[-1]


def get_lw(price_arr, cur_pos, period=None):
    return 0


def get_ss(price_arr, cur_pos, period=None):
    return 0


def get_dmi(price_arr, cur_pos, period=None):
    return 0


# def get_vorarity(price_arr, cur_pos, period=None):
#    tmp_arr = []
#    prev = -1
#    for val in price_arr[cur_pos - CHART_TYPE_JDG_LEN : cur_pos]:
#        if prev == -1:
#            tmp_arr.append(0)
#        else:
#            tmp_arr.append(val - prev)
#        prev = val
#    return np.std(tmp_arr)


def get_macd(price_arr, cur_pos, period=100):
    if cur_pos <= period:
        # s = 0
        return 0
    else:
        s = cur_pos - period + 1
    tmp_arr = price_arr[s : cur_pos + 1]
    # tmp_arr.reverse()
    prices = np.array(tmp_arr, dtype=float)

    macd, macdsignal, macdhist = ta.MACD(
        prices, fastperiod=12, slowperiod=26, signalperiod=9
    )
    if macd[-1] > macdsignal[-1]:
        return 1
    else:
        return 0


if __name__ == "__main__":
    # データ取得に使う定数
    COUNT = 5000  # 一度に取得するデータ数(max:5000)
    NB_ITR = 3  # count * NB_ITR 分データを取得
    GRANULARITY = "M15"
    INSTRUMENT = "USD_JPY"
    SKIP = 500  # 学習データの最初を何個読み飛ばすか。テクニカルを計算するときに過去の値を使うから読み飛ばさないと計算できない
    TARGET_OFFSET = 3  # 何個先の足をターゲット変数とするか
    MODE = "train"

    # 足データを取得するためにoandaAPIに渡すパラメータ
    params = {
        "granularity": GRANULARITY,
        "count": COUNT,
        "price": "M",
    }

    xgb_param = {
        "max_depth": 5,
        "eta": 0.2,
        "subsample": 1,
        "objective": "binary:logistic",
        "n_estimators": 2000,
    }

    if MODE == "train":
        # oandaAPIを叩くクラスのインスタンス化
        data_from_oanda = DataFromOanda(instrument=INSTRUMENT, params=params)

        # 終値を取得
        close_price = data_from_oanda.get_close_price_over5000(NB_ITR)

        # 整形データを作成: data_xが説明変数、data_yがターゲット
        data_x = []
        data_y = []
        for i in range(SKIP, len(close_price)):
            # インデックスを超えないように条件分岐
            if i + TARGET_OFFSET < len(close_price):
                data_x.append(
                    [
                        close_price[i],
                        get_ma(close_price, i),
                        get_ma_kairi(close_price, i),
                        # get_bb_1(close_price, i),
                        # get_bb_2(close_price, i),
                        get_ema(close_price, i),
                        # get_mo(close_price, i),
                        # get_po(close_price, i),
                        # get_macd(close_price, i),
                    ]
                )
                # TARGET_OFFSET足後が上昇していたら1、していなかったら0
                high_or_low = (
                    1 if close_price[i + TARGET_OFFSET] - close_price[i] >= 0 else 0
                )
            else:
                break
            data_y.append(high_or_low)

        print(len(data_x), len(data_y))

        # 学習データとテストデータに分割
        X_train, X_test, Y_train, Y_test = train_test_split(
            data_x, data_y, test_size=0.3, shuffle=False
        )
        print(len(X_train), len(Y_train))
        X_train_np = np.array(X_train)
        Y_train_np = np.array(Y_train)

        # XGBoostを使ってグリッドサーチ
        xgb_cv_reg = xgb.XGBRegressor(tree_method="gpu_hist")
        xgb_cv_params = {
            "learning_rate": [0.1, 0.3, 0.5],
            "max_depth": [2, 3, 5, 10],
            "subsample": [0.5, 0.8, 0.9, 1],
            "colsample_bytree": [0.5, 1.0],
        }
        cv = GridSearchCV(
            xgb_cv_reg, xgb_cv_params, cv=10, scoring="roc_auc", n_jobs=-1
        )
        cv.fit(X_train_np, Y_train_np)

        # ベストパラメータで改めて学習
        xgb_reg = xgb.XGBRegressor(
            **cv.best_params_,
            objective="binary:logistic",
            n_estimators=2000,
            tree_method="gpu_hist"
        )
        xgb_reg.fit(X_train_np, Y_train_np)

        # とりあえずテスト段階なのでここでテストする
        X_test_np = np.array(X_test)
        Y_test_np = np.array(Y_test)

        # 検証用データが各クラスに分類される確率を計算する
        y_pred_proba = xgb_reg.predict(X_test_np)

        # しきい値 0.5 で 0, 1 に丸める
        print(y_pred_proba)
        y_pred = np.where(y_pred_proba > 0.5, 1, 0)

        # 精度 (Accuracy) を検証する
        acc = accuracy_score(Y_test_np, y_pred)
        print("Accuracy:", acc)
    elif MODE == "test":
        pass
        # TODO
