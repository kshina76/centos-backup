# 順列全探索
# https://qiita.com/e869120/items/25cb52ba47be0fd418d6#3-2-順列全探索

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
minimum = 10000000000
count = 0

per = list(itertools.permutations([i for i in range(n)]))
for i in range(math.factorial(n)):
    for j in range(n - 1):
        count += a[per[i][j]][per[i][j + 1]]
    if count < minimum:
        minimum = count
    count = 0
print(minimum)
