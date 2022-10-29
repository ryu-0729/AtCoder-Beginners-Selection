# B - Practical Computing
# https://atcoder.jp/contests/abc254/tasks/abc254_b
n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  for j in range(n):
    if j == 0 or j == i:
      a[i][j] = 1
      if a[i][j] != 0:
        print(a[i][j], end=' ')
    else:
      a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
      if a[i][j] != 0:
        print(a[i][j], end=' ')
  print()
