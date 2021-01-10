import sys  # input、exti用
import re  # 正規表現
import collections
import itertools
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


# 10進数 -> n進数変換
def encode(value, base):
    if value > base:
        yield from encode(value // base, base)
    yield value % base


n, x = map(int, input().split())
s = input()
for i in range(n):
    if s[i] == "o":
        x += 1
    elif x != 0 and s[i] == "x":
        x -= 1

print(x)
