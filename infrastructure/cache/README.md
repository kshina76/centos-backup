# キャッシュについてまとめ
- 基本的に以下の記事を見ればおっけい
  - https://github.com/donnemartin/system-design-primer/blob/master/README-ja.md#キャッシュ
  - https://qiita.com/Shiruba/items/7810a686d8510fd1555a#キャッシュ

## RedisとMemcached
- メモリ(RAM)に保存してキャッシングする
- Redisはデータを永続化することもできるが、パフォーマンスが下がる
- とりあえずRedisを使えばいい

## キャッシュを使って高速化できる部分
- Webサーバ、APサーバ、DBサーバ

![https---qiita-image-store s3 ap-northeast-1 amazonaws com-0-496251-c7e3b451-dca9-e5e7-9896-bd07d72e0372](https://user-images.githubusercontent.com/53253817/103007713-3ce50980-4577-11eb-9c90-c2305749a863.png)

- ローカルキャッシュとリモートキャッシュの二種類があるが、Webサーバとかをロードバランシングするときにはリモートキャッシュかな
