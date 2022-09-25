# C - Skill Up
# https://atcoder.jp/contests/abc167/tasks/abc167_c
# NOTE: 初めて解説等を見ないで解けたbit全探索！
N, M, X = map(int, input().split())
C = [0 for _ in range(N)]
A = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
  std = list(map(int, input().split()))
  C[i] = std[0]
  A[i] = std[1:]

price = -1
for i in range(1 << N):
  d = [0 for _ in range(N)]
  for j in range(N):
    if (i >> j) & 1:
      d[j] = 1

  algo = [0 for _ in range(M)]
  total = 0
  for j in range(N):
    if d[j]:
      total += C[j]
      for k in range(M):
        algo[k] += A[j][k]

  isFlag = True
  for j in range(M):
    if algo[j] < X:
      isFlag = False

  if isFlag:
    if price == -1:
      price = total
    else:
      price = min(price, total)

print(price)
