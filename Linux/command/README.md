# 駆け出しエンジニアの頃に知ってたら超捗ってたlinux系コマンド・テクニックまとめ

# はじめに
僕が初めて現場に入ったときは、ターミナルの真っ黒い画面に面食らっていましたが、今では最も眺めている時間の長いものになりました。

プログラミングを始めてから1年半がたった今でも、ほぼ毎日のように使っているLinux系のコマンド・テクニックをまとめました！

これさえ抑えておけば、駆け出しエンジニアの方はとりあえず現場に放り込まれてもサバイブできるはずです！


# コマンドまとめ
## ls
`list`の略。
コマンドを打ったディレクトリ以下のファイル・フォルダを表示してくれます。
### lsの使用例

```bash
> ls
```

## pwd
`print working directory`の略。
現在のディレクトリの位置を表示してくれます。
### pwdの使用例
```
> pwd

→ /Users/hoge/path
```

## cd
`change directory`の略。
ディレクトリ移動ができます。何もつけず`cd`だけ打つとホームディレクトリに、`cd -`と打つと、直前にいたディレクトリに移動できます。

### cdの使用例

```bash
> cd path/to/hoge
→ hogeディレクトリに移動
```

## mv
`move`の略。
ファイル・ディレクトリの移動ができます。ファイルのリネームをしたいときもコイツを使います。
### mvの使用例
```bash
ファイルの移動。hoge.txtをsome_directoryに移動させる
> mv hoge.txt some_directory

ファイルのリネーム。hoge.txtをfuga.txtにリネームする
> mv hoge.txt fuga.txt
```

## cp
`copy`の略。
`cp 第1引数 第2引数`で、`第1引数`のファイルを`第2引数`にコピーします。
### cpの使用例

```bash
hoge.txtをsome_directoryの中にfuga.txtという名前でコピー
> cp hoge.txt some_directory/fuga.txt
```

## find
名前の通り、ファイルやディレクトリを探しだすコマンドです。ちょっと複雑で難しいのですが、なれるとむっちゃ便利です。

### findの使用例
```bash
拡張子が`md`のファイルを現在いるディレクトリ以下から探し出します
（ルートディレクトリで実行すると全ディレクトリに対して検索するので検索結果がエグいことになります）

> find . -name "*.md"

```

## grep
`Global regular expression print`の略。
コマンドを打ったディレクトリ以下からファイルを読み込み、テキストを検索してくれるコマンドです。

### grepの使用例

```bash
> grep hoge

→
hoge.md
17:hogehoge/fugafuga

fuga.md
25:→ /Users/hoge/path
33:> cd path/to/hoge
34:→ hogeディレクトリに移動

hogefuga.md
27:/Users/hoge
```

ちなみに、ripgrepというgrepの進化版（亜種？）がありまして、ripgrepのほうが圧倒的に早いので、こちらをおすすめしておきます。

[ripgrep](https://github.com/BurntSushi/ripgrep)


## cat
`concatenate（鎖状につなぐ）`の略。猫ちゃんではありません。
指定したファイルの中身が閲覧できます。

### catの使用例

```bash
> cat hoge.txt

→
hogehogehogeho
hogehogehogeho
hogehogehogeho
```


## more
指定したファイルの中身が閲覧できます。`cat`とは違い、ファイルの中身がちょっとずつ表示されるので、ファイルの行数が多いときに使うと便利です。moreを打った後は、`q`を押すと、もとの画面に戻ります。

### moreの使用例

```bash
> more hoge.txt
```

## less
`more`の進化版みたいなコマンドです。今回は`more`と`less`の両方を紹介しましたが、基本的にはどちらか一つだけ使えるようになっておけばOKです！

moreと同じくコマンドを叩くと、閲覧モードに移行し、`q`を押すともとの画面に戻ります。

↓の記事も参考になるのでぜひ。

[エンジニアなら知っておきたい lessコマンドtips 11選
](https://qiita.com/ine1127/items/64b5b6cf52471c3fe59c)

### lessの使用例
```bash
> less hoge.txt
```

## head
指定したファイルを上から○行だけ表示してくれます。`head -10`と数字を指定すると、ファイルの上から**10行**だけ、みたいなことが可能になります。

### headの使用例
```bash
head -10 hoge.txt

→
(hoge.txtの上から10行分が表示される)
```
## tail
`head`とは逆で、指定したファイルを下から○行だけ表示します。`head`と同じく、`tail -10`と数字を指定すると、ファイルの下から**10行**だけ表示、みたいなことが可能になります。

### tailの使用例
```bash
tail -10 fuga.txt

→
(fuga.txtの下から10行分が表示される)
```

## echo
引数をあてると、その引数の内容を出力します。環境構築などでよく見るコマンドですね。

### echoの使用例
```bash
> echo $PATH

→
/Users/sukebeeeeei/.tfenv/bin:/Users/sukebeeeeei/node_modules:/Users/sukebeeeeei/.nodenv/bin:/Users/sukebeeeeei/.nodenv/shims:/usr/local/opt/mysql@5.7/bin:/Users/sukebeeeeei/go/bin:/Users/sukebeeeeei/.goenv/shims:/Users/sukebeeeeei/.goenv/bin:/Users/sukebeeeeei/.pyenv/shims:/Users/sukebeeeeei/.pyenv/bin:/Users/sukebeeeeei/.rbenv/shims:/Users/sukebeeeeei/.rbenv/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/Library/TeX/texbin:/usr/local/go/bin:/opt/X11/bin:/usr/local/texlive/2018/bin/x86_64-darwin/:/Users/sukebeeeeei/dotfiles

（PATHが表示されてます）
```
## touch
ファイルのタイムスタンプを現在時刻に更新します。
ファイルが存在しない場合は、空ファイルを作成します。なんで`touch`という名前なのでしょうか。誰か教えてください。

### touchの使用例
```bash
# hoge.txtがある場合
> touch hoge.txt

→
(ファイルのタイムスタンプが更新されます)

# hoge.txtが無い場合
> touch hoge.txt

→
（中身が空のhoge.txtが作成されます）
```

## vi・vim
`vi・vim`が開けます。わざわざ**vscodeやatom**などのエディターを開くのが面倒なときなどに使いますね。

後は、`vim hoge.txt`とすると、`hoge.txt`が存在しなかった場合に、ファイルを生成してくれるので、

- あるファイルを作成し
- そのファイルにちょろっと書き込みをする

というときには頻出のコマンドです。vi・vimに関しては、基本的なコマンドはすべてのエンジニアが習得しておくべきなので、使ったことがないよーという方は、この際にぜひ練習してみてください。

[知識0から始めるVim講座
](https://qiita.com/JpnLavender/items/fabcc79b4ab0d52e1f6d)

### vi・vimの使用例
```bash
> vim hoge.txt
```

## mkdir
**make directory**の略です。その名の通り、ディレクトリを作成するコマンドです。

### mkdirの使用例
```bash
> mkdir hoge

→
(hogeディレクトリが作成されます)
```

## rm
`remove`の略。ファイルを削除するときに使うコマンドです。
使い方をミスると**破滅**するので、ご利用は計画的にどうぞ

[rm～ディレクトリやファイルを削除する
](http://www.obenri.com/_command/rm01.html)
### rmの使用例
```bash
> rm hoge.txt

→
hoge.txtが削除されます
```

## rmdir
`remove directory`の略。ディレクトリを削除するときに使うコマンドです。中身が空っぽのディレクトリしか消せません。ですので、ほぼほぼ使うことはないですw（この記事で紹介しておきながら）

ファイルが中にあるディレクトリを消したい場合は、`> rm -rf hoge_directory`とすることがほとんどです。

### rmdirの使用例
```bash
> rmdir hoge_empty_directory

→
（hoge_empty_directoryを削除）
```

## ln
`link`の略です。シンボリックリンクを作ることができます。シンボリックリンクとはなんぞや？、という方は下記記事をご参照ください。

[シンボリックリンク設定方法
](https://qiita.com/0084ken/items/6f39498c86fb592b2baf)

### lnの使用例
```bash
> ln -s ~/dotfiles/vimrc/_vimrc ~/.vimrc
```

## man
`manual`の略。
コマンドの説明を表示するコマンド（ややこしい）です。**「あーーーこのコマンドどうやって使うんだっけ？」**とか、**「このコマンドのオプションって何があるんだっけ？」**というときに使います。

### manの使用例
```bash
> man ls

→
（lsコマンドの説明書がでてくる）
```

## sudo
`superuser do`の略です。**すぅーどぅー**とか、**須藤さん**と読むことが多いです。

管理者権限でコマンドを実行したいときに使います。`sudo`をつけると、コマンドを叩いた後にパスワードを聞かれるので、それを入力してコマンドを実行します。

### sudoの使用例
```bash
> sudo vim hoge.txt

→Password:
(パスワードを入力してEnterを押すとコマンドが実行できる)
```

## history
その名の通り、今までに打ってきたコマンドの履歴が表示されます。
### historyの使用例
```bash
> history

→
...
11879 less must_cover_linux_commands.md
11880 tail must_cover_linux_commands.md
11881 more must_cover_linux_commands.md
11882 head must_cover_linux_commands.md
11883 more must_cover_linux_commands.md -n 100
11884 more must_cover_linux_commands.md -n 3
...
```

# 便利テクニック集
コマンドラインを扱う上で、知っていると**とても捗る**テクニックを紹介します。知っている人からしたら当たり前のことなんですが、それを誰もが知っているとは限りませんからね。僕も初めて現場に入って数ヶ月ぐらいして初めて知りましたし、知った当時はいたく感動したものです。

## “< > >>”
解説するより実例を出したほうが理解は早いと思うので、参考例をば。

```bash
> ruby calculate.rb < input_data.txt
（calculate.rbを実行し、そのデータとしてinput_data.txtを指定します）

> ruby calculate.rb > output_data.txt
（calculate.rbを実行し、その出力結果をoutput_data.txtに出力します。output_data.txtが存在していなかった場合はファイルの作成も勝手に行われます。output_data.txtが存在していた場合は、ファイルの中身が出力結果で上書きされます）

> ruby calculate.rb >> output_data.txt
（cdalculate.rbを実行し、その出力結果をoutput_data.txtの末尾に追加します。> output_data.txtとは違い、ファイルの中身が上書きされないのがポイント）

> ruby calculate.rb < input_data.txt > output_data.txt
（<と>、および>>は組み合わせることができます。↑では、calculate.rbを実行し、実行に用いるデータはinput_data.txtの中身を、そして実行結果をoutput_data.txtに出力します）
```

## pipe (|)
コマンドとコマンドをつなげることができます。**むっっっっちゃ使います。**

```bash
> cat hoge.txt | grep fuga
(hoge.txtのなかでfugaという文字列が含まれている場所を探す)
```

## $(), ``
`$()`のカッコの内部でコマンドを実行し、その結果を返してくれます。といっても、これだけでは全然意味がわからないと思うので、実例を出します。

```bash
> cat $(ls)

（先に$(ls)が実行され、その結果がcatの引数となります。その結果、↑のコマンドを実行したディレクトリ配下のファイルの中身がすべて表示されます。）
```

## 正規表現
例えば`grep`コマンドでは、`*`や`+`、`.`などの正規表現を使うことができます。というより、grepはもともと`Global regular expression print`の略なので、正規表現が使えるのは当たり前なんですけどねw

`*`と`+`は同じ文字の繰り返し（*は空文字を含むのに対し+は1文字以上）。`.`は任意の1文字ですね。

```bash
> grep .*hoge

（hogeを含む文章を検索）
```

# コマンドとテクニックを組み合わせてみる
では、今までに紹介したコマンドとテクニックを組み合わせてみます！

## うわーあのコマンドなんだっけーってとき
ctrl + rで過去のコマンドが検索できますが、↓のコマンドでも同じことができます。

```bash
> history | grep command_name
```

## （macの場合） Downloadに入っているファイルのうち最新○件の名前を知りたい

```bash
> ls -lat ~/Downloads | head -10
total 3408200
drwxr-xr-x+ 112 keisuke  staff       3584  1 18 21:49 ..
drwx------@ 569 keisuke  staff      18208  1 18 18:54 .
-rw-r--r--@   1 keisuke  staff      65540  1 18 18:54 .DS_Store
-rw-r--r--@   1 keisuke  staff     254894  1 18 18:54 finished.zip
-rw-r--r--@   1 keisuke  staff       1692  1 17 22:53 dupSSHkey.pem
-rw-r--r--@   1 keisuke  staff     128909  1 13 10:19 assignment-2-problem.zip
-rw-r--r--@   1 keisuke  staff     129247  1 12 11:43 01-start.zip
-rw-r--r--@   1 keisuke  staff      26651  1 12 11:43 learning-card.pdf
-rw-r--r--@   1 keisuke  staff     236506  1 12 11:25 forms-03-finished.zip
```

## ログを見たいとき
```bash
tail -f log/development.log
```
ログを見たいときはこのコマンドですね。Railsを書いているときは、だいたいこのコマンドを叩いて、ログ確認用にターミナルを1パネル分割り当ててます。

## ログの中から特定の文字列だけを検出したいとき
```bash
tail -f log/development.log | grep "検索したい文字列"

もしくは

cat log/development.log | grep "検索したい文字列"
```

プリントデバッグとかしたいときはこのコマンドを使ったりしますね。

## .zshrc（もしくは.bashrc）に文字列を挿入したい
環境構築するときによく見るコマンドですね。''の中身をechoで出力し、その出力結果を~/.zshrcに挿入する、というコマンドです。

```bash
echo 'export PATH=">HOME/.nodenv/bin:>PATH"' >> ~/.zshrc
```

## 特定のプロセスIDを調べたい
grepというプロセスが動いているか調べるコマンドです。

```bash
> ps aux | grep grep
sukebeeeeei          80328   0.0  0.0  4268280    656 s012  S+    9:52PM   0:00.00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn grep
```

## 2個下のディレクトリにあるファイルを一覧でみたいとき

```bash
↓のような構造のディレクトリがあるとします（僕のQiitaに上げる記事を保存してあるディレクトリですw）
>  qiita-outputs git:(master) ✗ tree
.
├── README.md
├── alfred_techniques.md
├── articles
│   └── nukistagram_release.md
├── english_acronym.md
├── env_and_env_fetch
│   └── sample.rb
├── favorite_english_site.md
├── must_cover_linux_commands.md
├── must_gem_list.md
├── path_understanding.md
├── peco_intro.md
├── really_good_software.md
└── software_engineer_general_knowlegde.md

2 directories, 12 files

（正規表現を用いてやってみる。ディレクトリの構造が複数層見られる）
>  qiita-outputs git:(master) ✗ ls *
README.md                              must_gem_list.md
alfred_techniques.md                   path_understanding.md
english_acronym.md                     peco_intro.md
favorite_english_site.md               really_good_software.md
must_cover_linux_commands.md           software_engineer_general_knowlegde.md

articles:
nukistagram_release.md

env_and_env_fetch:
sample.rb

（2個下のディレクトリのファイルを調べる）
>  qiita-outputs git:(master) ✗ ls */*
articles/nukistagram_release.md env_and_env_fetch/sample.rb
```

## 出力結果のうち、先頭10行だけを見たい
```bash
> ls */* | head -10
```

## 出力結果が長くなるので、一部をちょい出しにしてチェックしていきたい
```bash
> ls */* | less
```

## dockerのイメージをまとめて消したいとき
```bash
> docker rmi $(docker images -q)

もしくは

> docker rmi `docker images -q`
```

`docker images`でdockerのイメージ一覧が見られます。オプションで`-q`をつけることによって、イメージIDだけが表示されるように。

それを先に`$(docker images -q)`で処理して、その返り値に対して`docker rmi`を実行します。（rmi: remove image）

参考までに。`docker images`のうち、先頭5つだけを見たい場合。

```bash
> ~ docker images | head -5
REPOSITORY                                      TAG                          IMAGE ID            CREATED             SIZE
<none>                                          <none>                       8769696a985d        4 days ago          910MB
<none>                                          <none>                       694f9395f0e7        4 days ago          1.04GB
<none>                                          <none>                       8ff2255c3c50        4 days ago          995MB
<none>                                          <none>                       a1457d2c753d        2 weeks ago         995MB
<none>                                          <none>                       788141cacfc5        2 weeks ago         998MB
```

`docker images`のうち、先頭5つのイメージIDだけをみたいとき

```bash
>  ~ docker images -q | head -5
8769696a985d
694f9395f0e7
8ff2255c3c50
a1457d2c753d
788141cacfc5
```

## grepの検索結果をファイルに出力する
```bash
> grep hoge > hoge_search_result.txt
```



## 出力したテキストを置換して表示したい
`sed（stream editorの略）`というコマンドを使うと、テキストの置換ができたり、色々テクニカルで面白いことができるようになります。

```bash
> echo abcabc | sed s/ca/12/g

→ ab12bc
```

## grepで一致したうち、その前後の行の内容も知りたいとき
```bash
grep -C nで一致したところの前後n行も表示できる

> grep -C 3 "search_word" search_file
```

## あるコマンドのオプションの内容をパッと知りたいとき
例えば、findコマンドで、正規表現はどのように扱うのか、オプションをつければいいのか、とかを知りたいとする。そういうときはこれ。

```bash
findコマンドについてマニュアルを表示し、そのマニュアルのなかで"regular expression"に一致する箇所を、その前後3行も含めて表示する

> man find | grep -C 3 "regular expression"

     The options are as follows:

     -E      Interpret regular expressions followed by -regex and -iregex pri-
             maries as extended (modern) regular expressions rather than basic
             regular expressions (BRE's).  The re_format(7) manual page fully
             describes both formats.

     -H      Cause the file information and file type (see stat(2)) returned
--
--
     -regex pattern
             True if the whole path of the file matches pattern using regular
             expression.  To match a file named ``./foo/xyzzy'', you can use
             the regular expression ``.*/[xyz]*'' or ``.*/foo/.*'', but not
             ``xyzzy'' or ``/foo/''.

     -samefile name
```

# 最後に
上記で紹介したコマンドやテクニックも、**シェルスクリプトとかエイリアスと組み合わせるともっともっと強力になるのですが、本記事から逸脱した内容となるためなくなく断念しました**。この記事がバズったら、そのあたりを解説した記事も執筆したいなぁと考えていたり。

「ワイはこんなコマンド使ってるで！」、みたいな便利tipsがあったらぜひコメントを！
間違いや誤字脱字の報告もぜひぜひお願いします！

## 宣伝
バズったので唐突に宣伝を入れておきますw
結構気合い入れて書いた記事です〜。自信作なのでぜひ読んでってくださいw!

[【英語学習】海外の面白い・勉強になるプログラミング系Youtuberを5人&その他英語圏のおすすめ動画を一気紹介！
](https://qiita.com/sukebeeeeei/items/f8ed3e4a32232be977ff)


[【作業効率化】優秀すぎて課金してでも個人的に使ってるMacOSソフトウェアまとめ【5選】
](https://qiita.com/sukebeeeeei/items/b14ee87d7bd29511e580)

[pecoを使ったらターミナルの操作が劇的に効率化できた話](https://qiita.com/sukebeeeeei/items/9b815e56a173a281f42f)

## 参考文献

[Linuxコマンドは単語の意味を理解するとグッと身近なものになる
](https://qiita.com/tetsuya/items/46888bb4dfc8a6bfef02)

[新しいLinuxの教科書](https://www.amazon.co.jp/gp/product/4797380942/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=affiliate3203-22&creative=1211&linkCode=as2&creativeASIN=4797380942&linkId=29b5e7860f9583ad8edb0e5de56f7152)

[［試して理解］Linuxのしくみ ～実験と図解で学ぶOSとハードウェアの基礎知識](https://www.amazon.co.jp/gp/product/477419607X/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=affiliate3203-22&creative=1211&linkCode=as2&creativeASIN=477419607X&linkId=cd8945dcad25f265404e69f7ef8f0efb)

[UNIXという考え方―その設計思想と哲学](https://www.amazon.co.jp/gp/product/4274064069/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=affiliate3203-22&creative=1211&linkCode=as2&creativeASIN=4274064069&linkId=d5bcc2cec50e233629282f5545bfe35f)

## おまけ

Gatsby.jsで自作のブログを作ってみました。色々記事をアップしていきます！
[http://keisukee.com/](http://keisukee.com/)
