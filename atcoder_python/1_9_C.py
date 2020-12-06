import sys  # input、exti用
import re  # 正規表現
import collections
import math


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


n = int(input())
a = list(map(int, input().split()))

flag = True
count = 0
while flag:
    for i in range(n):
        if a[i] % 2 != 0:
            flag = False
            break
    if flag:
        flag = True
        for k in range(n):
            a[k] = a[k] / 2
        count += 1
    else:
        break
print(count)
