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


# 整数 N 個 (改行区切り)
# L = [int(input()) for i in range(N)]

# 整数 N 個 (スペース区切り)
# A = list(map(int, input().split()))

N = 4
A = [int(input()) for i in range(N)]

n = A[3] / 50

mul = 1
for j in range(len(A)-1):
    mul = mul * (A[j] + 1)
mul = mul - 1  # 最大のループ回数
