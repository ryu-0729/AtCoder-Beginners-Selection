# B - Enlarged Checker Board
# https://atcoder.jp/contests/abc250/tasks/abc250_b
# TODO: 理解不十分
n, a, b = map(int, input().split())
x = [['.' for _ in range(b * n)] for _ in range(a * n)]

for i in range(a * n):
  for j in range(b * n):
    r = i // a
    c = j // b
    if not (r + c) & 1: x[i][j] = '#'

for i in range(a * n):
  for j in range(b * n):
    print(x[i][j], end='')
  print()
