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



---
## オブジェクト指向の三大要素(クラス、ポリモーフィズム、継承)

- クラスの考え方
    - 似たようなサブルーチンをまとめるもの
        - 動物クラスとか変な比喩を考えないで、プログラミングの機能として割り切った方が理解しやすい
    - さらに頻繁に変更されるであろう箇所をクラスに抽出する
    - 元はグローバル変数を使わないでサブルーチン間で変数の参照や共有をしたいという発想からきた
    - 自己流だけど、openFileとかreadFileとかcloseFileとか、名詞が同じものをクラスでまとめて、open,read,closeというメソッドを作ればうまくまとまりそう。

- カプセル化の考え方
    - クラスの役割は一つに絞る

- 継承の考え方
    - 機能が被ったら。クラス間の共通の機能を親クラスとしてまとめて、子クラスから親クラスを継承する
        - このやり方はだめらしい、、何でもかんでもまとめて神クラスになってしまうから
    - 継承の本質は、交換可能なパーツを作成するために共通点を「規格」としてまとめ上げられるインタフェース。親クラスから機能を受け継ぐためのものではない。
    - インタフェースを継承して実際の中身を書くことが、正しい継承の使い方。機能自体を親クラスから引き継ぐことは継承の本質ではなくてただの便利機能という立ち位置
    - インスタンスの生成(new)はメインクラスかファクトリ機能のクラス以外でnewすることは無い。他のクラスの機能を使いたかったらコンポジションを使うことが推奨される。
        - https://qiita.com/shoheiyokoyama/items/d752834a6a2e208b90ca

- ポリモーフィズムとは？
    - 同じ名前のメソッドを複数のクラスで使用できるようにし、そのメソッドを通して、暗黙的に複数のインスタンスの動作を切り替えることができるようにすること
        - 呼び出したインスタンスがどのクラスかを意識させないこと
            - 継承した親クラスとみなされるから
    - 静的型つけ言語の厳密性を保ったまま、動的型つけ言語の柔軟性を得ることができる
        - 例えば、pythonのlist型のようにリストに異なる型の要素を混ぜるといったことを静的型づけ言語の厳密性を保って実現できるということ
    - それぞれ違うクラスが親クラスと同じとみなすことができる
        - 以下の例だと、SoldierもWizardもHunter同じCharacterBaseクラスとみなされている
    - https://qiita.com/Nossa/items/b6e2f4ed0fa079359fc5#抽象クラスとインターフェースの使い分け

    ```Java
    public abstract class CharacterBase {
        public virtual string Attack() {
        return "";
        }
    }

    // var character = new CharacterBase(); ←これは無理
    ```

    ```Java
    public class Soldier : CharacterBase {
        public override string Attack() {
            return "戦士は斬りかかった！";
        }
    }

    public class Wizard : CharacterBase {
        public override string Attack() {
            return "魔法使いは呪文を唱えた！";
        }
    }

    public class Hunter : CharacterBase {
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



- コンポジションと継承の使い分け

- 有用な参考文献
    - https://qiita.com/tutinoco/items/6952b01e5fc38914ec4e


# 用語やメモ
- 疎結合と密結合なプログラムとは

![2020-11-09 14 16のイメージ](https://user-images.githubusercontent.com/53253817/98502819-57e50e00-2296-11eb-822e-63333d8c07e0.jpeg)
