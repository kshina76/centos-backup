# 構成  
webサーバに対してALBで負荷分散を行う。DBは耐障害性を重視して2つ搭載して同期をとっている。  

## 注意点  
・DBサーバは作成に時間がかかるので、13分くらい待つ。  
・セキュリティグループ関連で作成できないことがあるので、depends_onをところどころに記述している  
  
# memoやわかったこと  
・webサーバが立てられるサブネットのルーティングはなぜALBではなくinternet-gatewayがデフォルトゲートウェイなのか  
ALBはあくまでパケットを振り分ける機能のものなので、webサーバからクライアントにレスポンスを返す際は、  
わざわざALBを介さなくても直接internet-gatewayに返したほうがいいから。  
  
・ALB用に別途サブネットを作る必要がある  
  