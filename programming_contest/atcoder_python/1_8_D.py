import sys  # input、exti用
import re  # 正規表現
import collections
import itertools
import math
import time

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


# 「10進数 -> 2進数変換」を行う。ただしbit全探索用のものなので、左からつめて表示される
# 例えば、10を変換すると、「0101000...」のような二進数に変換される
# value: 変換したい10進数の値, num_array: 2進数の長さ(長さ分0で埋めてくれる)
def bit_array(value, num_array):
    bit = [0] * num_array
    for i in range(num_array):
        div = 1 << i
        bit[i] = int(value / div) % 2
    return bit
