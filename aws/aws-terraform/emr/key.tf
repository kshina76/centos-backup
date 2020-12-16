
/*
emrのmasterノードに接続できるようにするため、公開鍵をここで登録する。

・参考文献
https://gside.org/blog/2016/11/06/lazyblorg-entry/
*/

resource "aws_key_pair" "pub-key" {
  key_name   = "id-rsa"
  public_key = file("~/.ssh/id_rsa.pub")
}