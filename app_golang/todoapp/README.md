# go言語でソフトウェアアーキテクチャを学ぶ前に理解しておく文法
- interfaceの基本
    - OOP言語でinterfaceを実現した場合
        1. interfaceを定義する
        2. クラスを作成してimplementsでinterfaceを継承
        3. クラス内のメソッドでオーバーライド

        ```java
        interface Calc {
            void calculation();
        }

        class Sum implements Calc {
            //オーバーライド
            public void calculation() {
                //処理
            }
        }
        ```

    - go言語でinterfaceを実現
        1. interfaceを定義する
        2. 構造体を作成
        3. 2で作成した構造体をレシーバとして、interfaceに定義したメソッドと同名のメソッドを定義

        ```go
        type Calc interface {
            calculation()
        }

        type Sum struct {
            X int
            Y int
        }

        func (sum *Sum) calculation() (result int, err error) {
            result = sum.X + sum.Y
            return
        }
        ```

    - 意識すること
        - 常に構造体をクラスと置き換えて考える
        - レシーバを定義していたらすぐに構造体(クラス)と結び付けてメソッドということを意識する

- interfaceの応用
    - https://qiita.com/tenntenn/items/eac962a49c56b2b15ee8
    - https://qiita.com/tenntenn/items/e04441a40aeb9c31dbaf
    - https://qiita.com/tenntenn/items/92928990173514c2adea

- コンストラクタ
    - 構造体をインスタンス化して返す関数
    - 慣例でメソッド名にNewプレフィックスをつける

    ```go
    type Calc interface {
        Caluculation()
    }

    type Sum struct {
        X int
        Y int
    }

    func NewSum() Sum {
        return Sum{
            1,2
        }
    }
    ```

# go言語を使ってクリーンアーキテクチャを実現
- http://inukirom.hatenablog.com/entry/di-in-go
- https://qiita.com/ogady/items/34aae1b2af3080e0fec4
- https://qiita.com/Sekky0905/items/2436d669ff5d4491c527
- https://eng-blog.iij.ad.jp/archives/2442
- https://medium.com/eureka-engineering/pairs-engage-server-side-architecture-c056bd8f598

# 色々なメモ
- sassをまとめてコンパイル
    - https://qiita.com/tonkotsuboy_com/items/67d9fd4d054a45af9f34