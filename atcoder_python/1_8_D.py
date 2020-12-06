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


s = str(input())
p = str(input())

for i in range(len(s)):
    flag = True
    s = s[1:len(s)]+s[0]  # 先頭の一文字を末尾に配置
    for j in range(len(p)):
        if s[j] != p[j] and flag:
            flag = False
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")
