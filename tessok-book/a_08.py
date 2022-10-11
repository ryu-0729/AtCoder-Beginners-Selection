h, w = map(int, input().split())
x = [None] * h
for i in range(h):
  x[i] = list(map(int, input().split()))

A = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(1, h + 1):
  for j in range(1, w + 1):
    A[i][j] = A[i][j - 1] + x[i - 1][j - 1]
for i in range(1, w + 1):
  for j in range(1, h + 1):
    A[j][i] = A[j - 1][i] + A[j][i]

q = int(input())
for i in range(q):
  a, b, c, d = map(int, input().split())
  ans = A[c][d] + A[a - 1][b - 1] - A[a - 1][d] - A[c][b - 1]
  print(ans)
