# B - Good Distance
# https://atcoder.jp/contests/abc133/tasks/abc133_b
import math


N, D = map(int, input().split())
X = [[0 for _ in range(D)] for _ in range(N)]
for i in range(N):
  X[i] = list(map(int, input().split()))

cnt = 0
for i in range(N):
  for j in range(i + 1, N):
    res = 0
    for k in range(D):
      res += (X[i][k] - X[j][k]) ** 2

    dis = math.sqrt(res)
    if dis.is_integer():
      cnt += 1

print(cnt)
