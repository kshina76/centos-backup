## 歴史やオブジェクト指向の基礎
- プログラミングの歴史
    - 機械語
    - アセンブリ言語
        - 機械語に分かりやすい命令名を与えたもの
        - 人間にわかりやすくなったものの、少し間違えただけでプログラムが暴走したりした
    - 初期の高級言語
        - FORTRANやcobolなどの誕生
    - 構造化プログラミング
        - 「順次進行」「条件分岐」「繰り返し処理」の基本三構造のシンプルな構成
        - goto文の廃止
            - スパゲッティコードをうむから
    - サブルーチンの誕生
        - 同じコードを繰り返さないように
    - ローカル変数と引数の値渡し
        - グローバル変数を少なくするために出てきた考え方
    - サブルーチン間で変数の変更や参照
        - クラスが備えている機能

- 構造体にサブルーチンを加えたものがクラスだと思う
    - だからgo言語だと構造体にメソッドを定義できる(構造体に対してでなくても定義できるが)

- OOPが生まれた理由
    1. グローバル変数を使わずにサブルーチン間で変数の呼び出しや参照を行いたい

- interfaceとabstractの違い
    - https://qiita.com/NaokiIwamoto/items/8722354a3a4076c2b39f


---
## オブジェクト指向の三大要素(クラス、ポリモーフィズム、継承)

- クラスの機能
    1. 関連性のあるサブルーチンと変数(グローバル変数とか)を一つにまとめる
        - メソッド名が動詞だけになっていることにも注目
    
    ```Java
    int fileNo;

    void openFile(String pathName){}
    void closeFile(){}
    void readFile(){}
    ```

    ```Java
    public class TextFileReader {
        int fileNo;

    void open(String pathName){}
    void close(){}
    void read(){}        
    }
    ```
    
    2. クラスの内部だけで使う変数やサブルーチンを隠す
        - javaだとprivateをつけて隠すということ
        - 前述した例だとfileNoにprivate修飾子をつける
        - スパゲッティコードの元凶となるグローバル変数をなくすことができる

    3. 1つのクラスからインスタンスをたくさん作る

- クラスの考え方
    - 似たようなサブルーチンをまとめるもの
        - 動物クラスとか変な比喩を考えないで、プログラミングの機能として割り切った方が理解しやすい
    - さらに頻繁に変更されるであろう箇所をクラスに抽出する
    - 元はグローバル変数を使わないでサブルーチン間で変数の参照や共有をしたいという発想からきた
    - 自己流だけど、openFileとかreadFileとかcloseFileとか、名詞が同じものをクラスでまとめて、open,read,closeというメソッドを作ればうまくまとまりそう。

- カプセル化の考え方
    - クラスの役割は一つに絞る

- 完璧なカプセル化
    1. setter,getterを使わない
        - クラスがどのように情報を管理しているのかを外に漏らさないのが正しいカプセル化だから
        - 外からクラス内の値を取得しようという時点でオブジェクト指向として間違っているから、他の方法を考え直す
        - フィールドはとにかくprivateにしておく
        - 例えば性別のフィールドを参照したくなったら、isMaleというメソッドを作ってtrueかfalseを返すようにする 

<br></br>

- ポリモーフィズムとは？
    - 同じ名前のメソッドを複数のクラスで使用できるようにし、そのメソッドを通して、暗黙的に複数のインスタンスの動作を切り替えることができるようにすること
        - 呼び出したインスタンスがどのクラスかを意識させないこと
            - 継承した親クラスとみなされるから
        - 要は以下のようなこと
        ```Java
        //普通のインスタンス化
        Soldier s = new Soldier();

        //ポリモーフィズム
        CharacterBase cb = new Soldier();
        ```

    - それぞれ違うクラスが親クラスと同じとみなすことができる
        - 次項の例だと、SoldierもWizardもHunter同じCharacterBaseクラスとみなされている
    - https://qiita.com/Nossa/items/b6e2f4ed0fa079359fc5#抽象クラスとインターフェースの使い分け

- ポリモーフィズムを使うメリット
    - 静的型つけ言語の厳密性を保ったまま、動的型つけ言語の柔軟性を得ることができる
        - 例えば、pythonのlist型のようにリストに異なる型の要素を混ぜるといったことを静的型づけ言語の厳密性を保って実現できるということ(次項の例)
    

- ポリモーフィズムの2種類の実現方法
    1. 抽象クラスを使った方法(Abstract Classパターンと言われている)
        ```Java
        public abstract class CharacterBase {
            public virtual string Attack() {
            return "";
            }
        }

        // var character = new CharacterBase(); ←これは無理
        ```

        ```Java
        public class Soldier extends CharacterBase {
            public override string Attack() {
                return "戦士は斬りかかった！";
            }
        }

        public class Wizard extends CharacterBase {
            public override string Attack() {
                return "魔法使いは呪文を唱えた！";
            }
        }

        public class Hunter extends CharacterBase {
            public override string Attack() {
                return "狩人は矢を放った！";
            }
        }
        ```

        ```Java
        using System;
        using System.Collections.Generic;

        public class Program {
            static void Main() {
                var party = new List<CharacterBase>() {  //違うクラス型なのにポリモーフィズムを使っていることにより同じクラスとしてみなされる
                    new Soldier(),
                    new Wizard(),
                    new Hunter(),
                };
                foreach (CharacterBase character in party) {
                    Console.WriteLine(character.Attack());
                }
            }
        }
        ```

    2. インタフェースを使った方法
        ```Java
        interface CharacterBase {
            string Attack();
        }

        // var character = new CharacterBase(); ←これは無理
        ```

        ```Java
        public class Soldier implements CharacterBase {
            public override string Attack() {
                return "戦士は斬りかかった！";
            }
        }

        public class Wizard implements CharacterBase {
            public override string Attack() {
                return "魔法使いは呪文を唱えた！";
            }
        }

        public class Hunter implements CharacterBase {
            public override string Attack() {
                return "狩人は矢を放った！";
            }
        }
        ```

        ```Java
        using System;
        using System.Collections.Generic;

        public class Program {
            static void Main() {
                var party = new List<CharacterBase>() {  //違うクラス型なのにポリモーフィズムを使っていることにより同じクラスとしてみなされる
                    new Soldier(),
                    new Wizard(),
                    new Hunter(),
                };
                foreach (CharacterBase character in party) {
                    Console.WriteLine(character.Attack());
                }
            }
        }
        ```


    - 実現方法の使い分け
        - 方法1
            - Template Methodパターンを実現したい場合に自然と使うことになる
                - 抽象クラスを使うから
                    - 「実装されたメソッド」と「抽象メソッド」を混在させて実現するのがTemplate Methodだから
        - 方法2
            - Template Methodパターンではない場合
                - できるだけ継承を使いたくないから、特に必要がないならinterfaceで行うのがいい
                    - 継承は慎重に行うものだから

    - 参考文献
        - https://www.hyuki.com/dp/dpinfo.html#AbstractClass

<br></br>

- 継承の問題点
    1. カプセル化を弱めてしまう
        - スーパークラスの実装を見ないといけないから、プログラマが大変
    2. スーパクラスに変更が発生した場合の対応が大変
        - 全てのサブクラスに反映させなければいけないから

- 継承の二つの用途
    1. 再利用のための継承
        - すでに存在するクラスを継承し、拡張する
        - これを目的にした継承はしないほうがいい。あくまでも副産物
            - ユーティリティクラスを作成したほうが便利なことが多いから
    2. 汎化のための継承
        - 類似クラスの共通なフィールドや処理をくくりだす
            - 複数のクラスに渡って共通して繰り返される処理を継承するスーパークラスの中に移動させる
            - これによってスーパークラスに一般的な処理を行わせて、サブクラスには固有な処理を行わせることができる
                - 一般的な処理は、ファイルから読み出す処理など、一般的な処理のことを指す
        - しかし、これを使って無闇に共通のクラスを作りすぎるのもよくない。神クラスができてしまう

- 二つの継承の違い
    - 再利用のための継承
        - ただの機能拡張に使う継承
    - 汎化のための継承
        - サブクラスが複数存在していて、サブクラス同士に何らかの関係性を持っていることから発生する継承

- 継承を使っていい場面
    1. is-aの関係が完璧に満たされている時
        - 子に親と同じ役割が期待される場合、親と同様に振る舞えるようになる継承を使うのが良い
            - これをリスコフの置換原則という
        - スーパークラスの一部の機能を使って拡張したいときは委譲(コンポジション)を使う

    2. フレームワーク(djangoとか)のような洗練されているものを継承するとき
        - ただし、多段で継承するのはよくない。多重継承はいいのかな？
        - オーバーライドをして良いことがドキュメントに記されているならオーバーライドする


- インスタンスの生成(new)はメインクラスかファクトリ機能のクラス以外でnewすることは無い。他のクラスの機能を使いたかったらコンポジションを使うことが推奨される。
    
    ![2020-11-09 15 48のイメージ](https://user-images.githubusercontent.com/53253817/98508618-1eff6600-22a3-11eb-95c0-81fb5e8ec6d1.jpeg)

- 継承は扱いが難しいことからGoやRustでは採用されていない

- インタフェースの重要性
    - https://ikenox.info/blog/inheritance-and-delegation-and-interface/

- 参考文献
    - https://qiita.com/shoheiyokoyama/items/d752834a6a2e208b90ca
    - https://www.furomuda.com/entry/20081026/p1
    - https://qiita.com/mikamikuh@github/items/1cdcd8b25a2e23f10525
    - https://mizchi.hatenablog.com/entry/2018/07/31/124354
    - https://www.furomuda.com/entry/20081026/p1

<br></br>

- 抽象クラスとinterfaceの違い
    - 抽象クラス
        - 「実装されたメソッドの定義」と「抽象メソッドの定義」の両方を行える
        - 共通の処理をまとめたりする中で使う人のため。だからprotectedかpublicを選べる
    - interface
        - 「抽象メソッドの定義」のみ、多重継承も許されている
        - 詳細は見せず出来ることを定義し、外から使う人のため。だからpublic
    
    - 参考文献
        - https://qiita.com/yoshinori_hisakawa/items/cc094bef1caa011cb739

    ![2020-11-12 17 06のイメージ](https://user-images.githubusercontent.com/53253817/98912432-76067480-2509-11eb-9dc0-cdc8a1be0e7e.jpeg)

- 抽象クラスとinterfaceの使い分け
    - https://qiita.com/igayamaguchi/items/e1d35db0a14a84bda452

- ポリモーフィズムの色々なパターン

- Abstract Classパターンとは？
    - Template Methodパターンを実装しようとすると自然に使っていると思う
    - https://www.hyuki.com/dp/dpinfo.html#AbstractClass

- Template Methodパターンとは？
    - スーパークラスで「処理の流れの定義」と「流れの中で使うメソッドを抽象メソッドとして定義」を行うこと
        - https://thinkit.co.jp/article/13182
    
    - 以下の例はTemplate Methodではなくてポリモーフィズムだと思う。実装メソッドが無いスーパークラスを使ってポリモーフィズムを行うなら抽象クラスではなくてinterfaceを使えばいいのでは？
        - https://qiita.com/aiko_han/items/e8ddce85188970fd77da


<br></br>

- 継承を使うべきかを判定する手順
    1. Template Methodまたはインタフェースでの継承か？
        - この場合は継承をしていい。
        - それ以外の場合は2に進む

    2. 継承でなくて委譲では実現できないか？
        - サブクラスからスーパークラスの機能を少し使いたい程度であれば委譲を選択するべき
        - コードの共通化を目的としているなら、継承は使ってはいけない。委譲を使うべき
            - https://www.ikemo3.com/dic/commonize/
        - 機能追加、機能変更の継承はダメ。委譲を使う
            - https://qiita.com/tonluqclml/items/c0110098722763caa556
        - 委譲はサブクラスのメンバ(フィールドに)にスーパークラスのオブジェクトを持たせることでできる
    
    3. リスコフの置換原則を満たしているか？
        - サブクラスをスーパークラスに置き換えたときに、問題なく振舞うか？
        - 「問題なく振舞うか」というのは想定していない振る舞いをしないかということ
            - 以下にpythonを使った例がわかりやすい
                - https://gside.org/blog/2019/11/17/
        - 特にオーバーライドをした時に想定していない振る舞いが起きたりするので、そこをしっかり確認する
            - 抽象メソッドをオーバーライドするのは問題ない。実装されているメソッドをオーバーライドするときに気を付ける
            - 確かに、djangoのget_context_dataはオーバーライドしてもスーパーとサブで同じ振る舞いをする

- 継承の使い所
    - ElectoricCarはスーパークラスのCarの機能を全て満たす
        - is-aの関係が完璧に成り立っている

```Java
class Car {
    void SpeedUp(){
        // ...
    }

    void OpenWindow(){
        // ...
    }

    // ...
}

```

```Java
class ElectoricCar extends Car {
    // 電気自動車特有のロジック
    void Charge() {
        // ...
    }
}
```

- 委譲の使い所
    - UserRepositoryがスーパークラスであるDatabaseのdoSQLという機能だけを使いたい場合
    - もしこの場面で継承を使ってしまうと、余計な機能が継承されて、単一責務の法則に反することになる

```Java
class Database {
    void connectToDatabase(String dbHost, String dbName, ...){
        // DBへの接続ロジック
    }

    Result doSQL(String sql){
        // 接続しているDBにクエリを投げ、その結果を返すロジック
    }

    // そのほかデータベースの接続状態の管理など
}
```

```Java
class UserRepository {

    Database database;

    UserRepository(Database database){
        // UserRepositoryのインスタンス生成時にDatabaseのインスタンスをセット
        this.database = database;
    }

    User getUser(int userId) {
        String sql = String.format("SELECT * FROM users WHERE user_id=%d", userId);
        Result result = this.database.doSQL(sql)
        // クエリの実行結果をもとにユーザーオブジェクトを作って返す
    }
}
```

- 継承と委譲の使い分けまとめ
    - 継承はis-aの関係が完璧に満たされた時に使うといい
        - しかし将来的に満たさなそうなら使わないほうがいい
    - 委譲はサブクラスが、スーパークラスを単なるツールとして使うときに使うといい
        - スーパークラスの一部分のメソッドだけ使いたい場合など

- 参考文献
    - https://ikenox.info/blog/inheritance-and-delegation-and-interface/

<br></br>

- 実装ではなく、インタフェースに対してプログラムをする
    - インタフェースが提供されているなら、実装クラスを呼び出すのではなく、インタフェースに対してメソッドを呼び出すようにプログラムをするという意味
    - 後々の変更に柔軟に対応できるから
    - 以下のようにプログラミングをしろということ
    ```Java
    //こっちじゃない
    Soldier s = new Soldier();

    //こっち
    CharacterBase cb = new Soldier();
    ```

<br></br>

- まとめ

    ![2020-11-09 15 51のイメージ](https://user-images.githubusercontent.com/53253817/98508783-6dad0000-22a3-11eb-9f85-17e97c4d9230.jpeg)


---

## オブジェクト指向のさらに進んだ仕組み3選(パッケージ、例外、ガベージコレクション)

- パッケージ
    - クラスをさらにまとめる仕組み
        - クラスだけでなくて、パッケージにパッケージをまとめることもできる
    - 全世界でクラスの名前の重複を避ける役割がある
        - jp.co.nikkeibp のように

<br></br>

- 例外
    - エラーコードを使った従来の例外処理
        - 1が以上終了、0が正常終了のようにエラー処理をすること
        - エラーコードの問題点
            1. エラーコードの判定を書き忘れたり、値を間違えたりすると原因究明が難しくなる
            2. エラーコードの判定がサブルーチン間で連鎖してしまう
                - 例えばサブルーチンAからBを呼んでいて、BからCを呼んでいる際に、Cでエラーが発生したらBにリターンして、BがAにリターンをするという連鎖状態
                - プログラムのロジックが冗長になってしまう
    - 例外を使った新しい方法
        - 特別な名前のついたエラーを返す方法。NullExceptionとか
        - 例外のメリット
            1. エラーの判定を書き忘れることが無くなる
                - 例外を宣言しているメソッドを呼び出す側では、例外を処理するロジックを正しく書いていないとエラーになる
                - try-catchで例外処理
            2. さらに上位のメソッドに例外を伝える場合は、例外を投げるだけでいい
                - 例外をthrowするだけでいいということだと思う
                - 末端のメソッドでエラー判定を書けばいい
                    - 途中のメソッドでエラー判定を書かないことで、エラー判定を一つのメソッドにためることができる

<br></br>

- ガベージコレクション
    - OOPでたくさん作ったインスタンスを安全に削除する仕組み
        - ガベージコレクタというプログラムのおかげで、インスタンスを作成するとメモリが確保されるが、これを安全に開放することができる
    - C言語などでは、freeとかを使ってメモリを直接操作していたから危険だった

- ガベージコレクションの対象となるもの

![2020-11-09 21 34のイメージ](https://user-images.githubusercontent.com/53253817/98541828-600f6e80-22d3-11eb-85cf-d9dd3cfc69e7.jpeg)

<br></br>

- まとめ

![2020-11-09 16 57のイメージ](https://user-images.githubusercontent.com/53253817/98514403-bc12cc80-22ac-11eb-9f31-34d070e1aee1.jpeg)

---

# OOPによるソフトウェアとデザインの再利用

- クラスライブラリ
    - 汎用的な機能を持つクラスをたくさん集めたもの
    - ライブラリを継承することで、バラエティに富んだ実装を行うことができる

    ![2020-11-09 22 48のイメージ (1)](https://user-images.githubusercontent.com/53253817/98549106-b4b7e700-22dd-11eb-8667-06e59841f2a2.jpeg)

- 関数ライブラリ
    - 汎用的な機能を持つサブルーチンをたくさん集めたもの
    - サブルーチンを呼び出すだけ
    - 継承やポリモーフィズムを使えないので、カスタマイズ性がない

    ![2020-11-09 22 48のイメージ](https://user-images.githubusercontent.com/53253817/98549100-b1bcf680-22dd-11eb-8656-b08bd89eae32.jpeg)

- フレームワーク
    - アプリケーションの半完成品

- デザインパターン
    - 機能拡張や再利用がしやすいソフトウェアを作るためのノウハウ集
    - デザインパターンを使うことでライブラリを利用する注意点や設計意図を伝えることが容易
    - クラスライブラリの開発者がデザインパターンに沿って設計することが多々ある(JavaのライブラリはGoFに沿っているものが多かった)

- GoFのデザインパターン

![2020-11-09 23 00のイメージ](https://user-images.githubusercontent.com/53253817/98550452-77ecef80-22df-11eb-9b24-cebec5269740.jpeg)

- 様々な領域の「パターン」

![2020-11-09 23 06のイメージ](https://user-images.githubusercontent.com/53253817/98551066-39a40000-22e0-11eb-8675-4184612979f0.jpeg)


---






- 有用な参考文献
    - https://qiita.com/tutinoco/items/6952b01e5fc38914ec4e


# 用語やメモ
- 疎結合と密結合なプログラムとは

![2020-11-09 14 16のイメージ](https://user-images.githubusercontent.com/53253817/98502819-57e50e00-2296-11eb-822e-63333d8c07e0.jpeg)

<br></br>

- コンパイラ方式とインタプリタ方式と中間コード方式の違い
    - コンパイラ方式
        - メリデメ
            - 実行速度が速い
            - 実行するのに手間がかかる
            - プラットフォームが異なると実行できない(機械語がマシンによって異なるから)
        - 用途
            - 政府や銀行のシステム
            - 企業の基幹システム
    - インタプリタ方式
        - メリデメ
            - 異なるプラットフォーム(異なるOSなど)でもファイルを配布すればすぐに実行できる
            - 実行速度が遅い
        - 用途
            - インターネットを通じて、様々な種類のマシンにダウンロードされて動くソフトウェア
    - 中間コード方式
        - メリデメ
            - コンパイラ方式とインタプリタ方式のいいとこ取り

![2020-11-09 21 39のイメージ](https://user-images.githubusercontent.com/53253817/98542332-14a99000-22d4-11eb-9db5-e90fc39815cf.jpeg)

![2020-11-09 21 41のイメージ](https://user-images.githubusercontent.com/53253817/98542519-681bde00-22d4-11eb-9d9c-1ae898bad5fe.jpeg)


<br></br>

- プログラムのメモリ領域の種類
    - 静的領域はプログラムの開始に確保されて終了まで配置が固定される
    - プログラムの実行中にアプリケーションから必要なサイズを要求することで割り当てを行い、不要になれば元に戻す
    - スタック領域は一つのサブルーチン呼び出しが一つのスレッド

![2020-11-09 22 05のイメージ](https://user-images.githubusercontent.com/53253817/98544681-ae267100-22d7-11eb-9c61-1cd65a2d8081.jpeg)

- デザインパターンとは
    - 優れた設計のアイデアを後から再利用できるように、名前をつけて文書化したもの

<br></br>

- スレッドとプロセスの違い
    - プロセスの中に複数のスレッドがある

![2020-11-09 21 50のイメージ](https://user-images.githubusercontent.com/53253817/98543325-aa91ea80-22d5-11eb-9fb8-73159c97ee95.jpeg)

- マルチスレッドとは
    - マルチスレッドはOSの機能で複数のスレッド同時に(のように)処理すること
    - マルチスレッドを用いた並行処理
        - CPUが一度に実行できるスレッドは一つだけど、CPUは一つのスレッドを一気に実行しないで、複数スレッドをそれぞれ少しづつ実行すること
        - これによってあたかもCPUが複数のスレッドを同時に実行しているように見せる
    - マルチスレッドを用いた並列処理
        - ある1つの時点で、実際に、物理的に、複数の仕事をしていること
        - これは、速くすることが目的
        - CPUのcore数が2つ以上の場合に可能


- 並行処理と並列処理の違い
    - 並行処理
        - ある1つの時点では、1つの仕事しかしていないが、複数の仕事間を切り替えることによって、同時にやっているように見えること。
        - これは、速くするとかいうより、単純に同時にやることあるいは他を待たせないことが目的
    - 並列処理
        - ある1つの時点で、実際に、物理的に、複数の仕事をしていること
        - A、B、Cの処理をよーいどん、で3つ同時にスタートする
        - これは、速くすることが目的
        - CPUのcore数が2つ以上の場合に可能
        - 複数のプロセス上で、複数のスレッドが立ち上がる
    
    ![https---qiita-image-store s3 amazonaws com-0-106693-ee7e9cb3-53b9-9b88-d335-1a71be17f0ee](https://user-images.githubusercontent.com/53253817/98650360-1f1f6480-237c-11eb-917d-d8aa37bdf778.png)

- 並行/並列処理のパターン

    ![2020-11-10 18 04のイメージ](https://user-images.githubusercontent.com/53253817/98653013-ceaa0600-237f-11eb-83ad-2c0ddebea529.jpeg)


- 同期処理とは
    - 書いた順番に実行されていく
    - 重たい処理が間にあると、そこで大きな待ち時間が生まれる

- 非同期処理とは
    - 並行処理のこと
    - 時間がかかる処理の完了を待たずに次の処理を進め、同時に複数の処理を進めることを非同期処理という
    - 例えば、外部のサーバと通信する関数を呼んだあと、レスポンスが返るまでに一旦関数から抜けて別の処理を進めて レスポンスを受け取り次第、呼び出し元に値を返す処理など
    - プログラムは基本的には逐次実行といって、一つの処理が終わったら次の処理を行うようにしているが、それだと非効率な場合があるから非同期処理という仕組みがある
    - コールバック関数
        - Aという関数が完了次第、実行したい関数(function)を引数として渡して実行させるもの
        - JavaScriptでは、上述のコールバック関数で処理順をコントロールできるが、ネストが深くなる

- プログラミングにおける並列/並行処理
    - core数が一つの時は並行処理になって、core数が複数の時は並列処理になる
        - 設定で扱うcore数の上限をあげると並列処理になる
    - go言語に関してはruntime パッケージの関数 GOMAXPROCS で指定するか、環境変数 GOMAXPROCS で指定するとgoroutineが並列で動く

- JavaScriptでの非同期処理
    - https://qiita.com/kiyodori/items/da434d169755cbb20447

- goが他の非同期プログラミングよりも優れている理由
    - https://qiita.com/methane/items/5ad7c092c0d426db4ab5

- 参考文献
    - https://qiita.com/Takagi_/items/84b4a2184f42ee77867c
    - https://qiita.com/Kohei909Otsuka/items/26be74de803d195b37bd
    - https://ascii.jp/elem/000/001/475/1475360/
    - http://www.nct9.ne.jp/m_hiroi/golang/abcgo14.html

<br></br>