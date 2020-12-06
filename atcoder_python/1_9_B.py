import sys  # input、exti用
import re  # 正規表現
import collections


# 入力の高速化
def input():
    return sys.stdin.readline()[:-1]


# 正規表現をコンパイル
def re_compile(pattern):
    repattern = re.compile(pattern)
    # result = repattern.sub()
    return repattern


# 文字の出現回数を辞書型で返却
# textにappleという文字列が入ってきたら、a,p,l,eそれぞれのカウントができる
def str_count(text):
    dic = {}
    for i in text:
        dic[i] = text.count(i)
    return sorted(dic.items())  # keyでソートして返す. valueでソートしたい場合はlambdaで.


result = []
while True:
    s = input()
    if s[0] == '-':
        break
    m = int(input())
    h = [int(input()) for i in range(m)]

    for i in h:
        s = s[i:] + s[0:i]
    result.append(s)

for i in result:
    print(i)
