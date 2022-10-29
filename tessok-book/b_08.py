n = int(input())
xy = [[0 for _ in range(1501)] for _ in range(1501)]
for _ in range(n):
  x, y = map(int, input().split())
  xy[x][y] += 1

A = [[0 for _ in range(1501)] for _ in range(1501)]
for i in range(1, 1501):
  for j in range(1, 1501):
    A[i][j] = A[i][j - 1] + xy[i][j]
for i in range(1, 1501):
  for j in range(1, 1501):
    A[j][i] = A[j - 1][i] + A[j][i]

q = int(input())
for _ in range(q):
  a, b, c, d = map(int, input().split())
  ans = A[c][d] + A[a - 1][b - 1] - A[c][b - 1] - A[a - 1][d]
  print(ans)
