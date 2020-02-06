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

