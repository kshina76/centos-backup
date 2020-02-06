# optunaを使ったベイズ最適化でのパラメータチューニング  
  
## optunaの変数の使い分け  
・suggest_uniform  
パラメータがfloat型のもの  
  
・suggest_loguniform  
パラメータがfloat型の中でもかなり小さい値を扱うとき。1e-5とか「e」を使って表現するものに対して  
  
・suggest_int  
パラメータがint型のもの  
  
・suggest_categorical  
パラメータが文字のもの  
  
・suggest_discrete_uniform  
パラメータを減らしていきながら最適化するものかな？float型で  


## kaggle本筆者のxgboostの最適化パラメータ  
```python  
# ベースラインのパラメータ  
params = {  
    'booster': 'gbtree',  
    'objective': 'binary:logistic',  
    'eta': 0.1,  
    'gamma': 0.0,  
    'alpha': 0.0,  
    'lambda': 1.0,  
    'min_child_weight': 1,  
    'max_depth': 5,  
    'subsample': 0.8,  
    'colsample_bytree': 0.8,  
    'random_state': 71,  
}  
  
# パラメータの探索範囲  
param_space = {  
    'min_child_weight': trial.suggest_loguniform('min_child_weight', np.log(0.1), np.log(10)),  
    'max_depth': trial.suggest_int('max_depth', 3, 9, 1),  
    'subsample': trial.suggest_uniform('subsample', 0.6, 0.95, 0.05),  
    'colsample_bytree': trial.suggest_uniform('subsample', 0.6, 0.95, 0.05),  
    'gamma': trial.suggest_loguniform('gamma', np.log(1e-8), np.log(1.0)),  
    # 余裕があればalpha, lambdaも調整する  
    # 'alpha' : trial.suggest_loguniform('alpha', np.log(1e-8), np.log(1.0)),  
    # 'lambda' : trial.suggest_loguniform('lambda', np.log(1e-6), np.log(10.0)),  
}  
```
  
## 参考文献  
・有名な人の手動のGBDTチューニング方法  
https://naotaka1128.hatenadiary.jp/entry/kaggle-compe-tips  
https://qiita.com/R1ck29/items/50ba7fa5afa49e334a8f  
  
・optunaの使い方  
https://qiita.com/koshian2/items/1c0f781d244a6046b83e  
https://blog.amedama.jp/entry/2018/12/06/015217  
  
・optunaとクロスバリデーション  
https://www.hirayuki.com/kaggle-zakki/lightgbm-optuna-kfold-introduction  
  
・公式のoptunaのgithub(sampleがいっぱい置いてある)  
https://github.com/optuna/optuna/tree/master/examples  

