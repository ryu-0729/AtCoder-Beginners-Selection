# C - HonestOrUnkind2
# https://atcoder.jp/contests/abc147/tasks/abc147_c
# TODO: 処理手順は解説動画を見てなんとなく理解できたが、まだ不十分。復習必要
N = int(input())
g = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
  a = int(input())
  for j in range(a):
    x, y = map(int, input().split())
    x -= 1
    g[i][x] = y

answer = 0
for i in range(1 << N):
  d = [0 for _ in range(N)]
  for j in range(N):
    if ((i >> j) & 1): d[j] = 1

  isOk = True
  for j in range(N):
    if d[j]:
      for k in range(N):
        if g[j][k] == -1: continue
        if g[j][k] != d[k]: isOk = False

  if isOk:
    popcnt = bin(i).count('1')
    answer = max(answer, popcnt)

print(answer)
