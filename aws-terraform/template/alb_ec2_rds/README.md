# 構成  
webサーバに対してALBで負荷分散を行う。DBは耐障害性を重視して2つ搭載して同期をとっている。  
![maltiaz](https://user-images.githubusercontent.com/53253817/73823868-7ec07080-483c-11ea-8857-8447602b7221.jpg)


## 注意点  
・DBサーバは作成に時間がかかるので、13分くらい待つ。  
・セキュリティグループ関連で作成できないことがあるので、depends_onをところどころに記述している  

## 参考文献  
https://qiita.com/sicksixrock66/items/63c6b651e6ccc28b0285  
  
# memoやわかったこと  
・webサーバが立てられるサブネットのルーティングはなぜALBではなくinternet-gatewayがデフォルトゲートウェイなのか  
ALBはあくまでパケットを振り分ける機能のものなので、webサーバからクライアントにレスポンスを返す際は、  
わざわざALBを介さなくても直接internet-gatewayに返したほうがいいから。  
  
・ALB用に別途サブネットを作る必要がある  
  