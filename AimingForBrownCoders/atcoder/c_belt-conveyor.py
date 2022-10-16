# C - Belt Conveyor
# https://atcoder.jp/contests/abc265/tasks/abc265_c
# NOTE: 解説見て微修正
h, w = map(int, input().split())
g = [[''] for _ in range(h)]
for i in range(h):
  g[i] = str(input())

# NOTE: 既に訪れているか判定する配列
v = [[False for _ in range(w)] for _ in range(h)]
v[0][0] = True

isStop = False
i, j = 1, 1
loopFlg = False
while True:
  ni, nj = i, j
  if g[ni - 1][nj - 1] == 'U' and i != 1:
    ni -= 1
  elif g[ni - 1][nj - 1] == 'D' and i != h:
    ni += 1
  elif g[ni - 1][nj - 1] == 'L' and j != 1:
    nj -= 1
  elif g[ni - 1][nj - 1] == 'R' and j != w:
    nj += 1
  else:
    isStop = True

  if isStop: break
  if v[ni - 1][nj - 1]:
    loopFlg = True
    break
  v[ni - 1][nj - 1] = True
  i, j = ni, nj

if loopFlg:
  print('-1')
  exit()

print(i, j)
