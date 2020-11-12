# figmaの使い方

- レイヤーパネル、ツールバー、プロパティパネル
    - レイヤーパネルは左のやつ
        - 全体の管理
        - グループの概要
    - ツールバーは上のやつ
        - 図形を書くモードやテキストを書くモードを変更する
    - プロパティパネルは右のやつ
        - 色や太さなどといった部品の詳細設定

- コンポーネント、オブジェクトの削除
    - 削除対象を選択してdeleteキー

- グループ化
    - グループ化の方法2つ
        - フレームに配置してグループ化する方法(推奨)
        - 部品を複数してグループ化する方法
    - 左のレイヤーパネル上で所属させたいグループにドラックアンドドロップ

- グループ化は積極的に使う
    - 同じようなページを作成する時に、グループ化した時のコピペが楽

- 一部分を枠線にする
    - 「Border」というプラグインを使うといい
    - 「Border」はrectangleに対しては適用できないので注意。Frameでないとダメ

- テキストの編集
    - テキストボックスをダブルクリックする
    - ツールバーの「T」を選択してから、テキストボックスを選択すると編集できる

- 参考文献
    - https://chot.design/figma-beginner/7532e053b748/

## 開発につなげるテクニック
- frameでグループ化しておくと、HTMLのタグ付けの構成がすぐに浮かぶ
    - frame一つあたり一つのタグを使う
    - 例えば、techblogの例でいうと、「Search」「Categories」「Tags」をそれぞれ別のFrameに入れてグループ化して、それぞれのFrameを「sidebar」というFrameにグループ化している
    - レイヤーパネルの階層ごとにタグを付与していけばいいのではないか！！
        - frameだけでなくてrectangleとかにも全部タグ付したほうがいいかも