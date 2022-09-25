# C - Average Length
# https://atcoder.jp/contests/abc145/tasks/abc145_c
import itertools
import math


N = int(input())
X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]
for i in range(N):
  x, y = map(int, input().split())
  X[i] = x
  Y[i] = y

def distance(x, y, i, j):
  distX = x[i] - x[j]
  distY = y[i] - y[j]
  return math.sqrt((distX ** 2) + (distY ** 2))

dist = 0.0
cnt = 0
# NOTE: 順列全探索
for p in itertools.permutations(range(N)):
  for i in range(N - 1):
    dist += distance(X, Y, p[i], p[i + 1])

  cnt += 1

ans = dist / cnt
print(ans)
