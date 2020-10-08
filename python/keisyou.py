
class parent():
    class_val = 1

    def get_print(self):
        print('super')
    
    def get_class_val(self):
        print(self.class_val)

class child(parent):
    class_val = 2

    def get_print(self):
        print('child')

    def test_super(self):
        super().get_print()

    def test_self(self):
        self.get_print()

# インスタンス生成
ch = child()



# super()はオーバーライド前のメソッドを呼びたい時に使う。
ch.test_super()

# selfはオーバーライド後または、オーバーライド自体をしていない場合に呼び出したいときに使う。
# つまり、オーバーライドしていない時は、selfでもsuperでもどちらを使っても問題ないことがわかった。
ch.test_self()

# クラス変数は子クラスで値を変更すると、変更される。
ch.get_class_val()

'''
実行結果
super
2
'''