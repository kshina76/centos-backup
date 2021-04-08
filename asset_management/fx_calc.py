
"""
投資のシミュレーション
"""
# period = 10*12
# interest_rate = 1.010 # 月利
# reserve = 30000 # 毎月の積み立て
# funding = 0
# profit_month = 0
# profit_year = 0
# for i in range(1, period + 1):
#     funding += reserve  # 積み立て
#     profit_month = funding * (interest_rate - 1)  # 月利
#     profit_year += profit_month # 税金処理のための変数
#     funding *= interest_rate # 月利を加えた資金
#     if i % 12 == 0:
#         zeikin = profit_year * 0.20315
#         profit_year = 0
#         funding -= zeikin
#     print(i, funding)


"""
行列の掛け算

example
(1 2) (2 3)
(2 3) (4 5)
(4 5)

input
3
2
1 2
2 3
4 5
2 3
4 5

output
[[10, 13], [16, 21], [28, 37]]
"""
# n = int(input())
# m = int(input())
#
# a = []
# for i in range(n):
#     a.append([i for i in map(int, input().split())])
#
# b = []
# for i in range(m):
#     b.append([i for i in map(int, input().split())])
#
# tmp = []
# result = []
# s = 0
# for i in range(n):
#     for j in range(m):
#         for k in range(m):
#             s += a[i][k] * b[k][j]
#         tmp.append(s)
#         s = 0
#     result.append(tmp)
#     tmp = []
#
# print(result)


"""
数字が大きすぎて誤差が出てしまう場合は、文字列として処理する
"""
# x = input()
# if "." in x:
#     print(x.split(".")[0])
# else:
#     print(x)

a = list(map(int, input().split()))
w = int(input())

def saiki(i, w):
    # ベースケース
    if i == 0:
        if w == 0:
            return True
        else:
            return False

    saiki(i - 1, w - a[i]) # a[i]を選んだ場合
    saiki(i - 1, w)  # a[i]を選ばなかった場合
