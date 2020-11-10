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
    1. 継承を使った方法
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

    2. インタフェースを使った方法(推奨)
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


    - 2の方法で行うようにする
        - 継承を使わなくて済むから
            - 継承は慎重に使わないといけないから

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
        - スーパークラスの一部の機能を使って拡張したいときは委譲(コンポジション)を使う
    2. フレームワーク(djangoとか)のような洗練されているものを継承するとき
        - ただし、多段で継承するのはよくない。多重継承はいいのかな？


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

- スレッドとプロセスの違い
    - プロセスの中に複数のスレッドがある

![2020-11-09 21 50のイメージ](https://user-images.githubusercontent.com/53253817/98543325-aa91ea80-22d5-11eb-9fb8-73159c97ee95.jpeg)

- マルチスレッドとは
    - CPUが一度に実行できるスレッドは一つだけど、CPUは一つのスレッドを一気に実行しないで、複数スレッドをそれぞれ少しづつ実行すること
    - これによってあたかもCPUが複数のスレッドを同時に実行しているように見せる
    - マルチスレッドはOSの機能

- プログラムのメモリ領域の種類
    - 静的領域はプログラムの開始に確保されて終了まで配置が固定される
    - プログラムの実行中にアプリケーションから必要なサイズを要求することで割り当てを行い、不要になれば元に戻す
    - スタック領域は一つのサブルーチン呼び出しが一つのスレッド

![2020-11-09 22 05のイメージ](https://user-images.githubusercontent.com/53253817/98544681-ae267100-22d7-11eb-9c61-1cd65a2d8081.jpeg)

- デザインパターンとは
    - 優れた設計のアイデアを後から再利用できるように、名前をつけて文書化したもの

