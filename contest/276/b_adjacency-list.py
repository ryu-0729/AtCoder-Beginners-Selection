# B - Adjacency List
# https://atcoder.jp/contests/abc276/tasks/abc276_b
n, m = map(int, input().split())
t = [[] for _ in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  t[a - 1].append(b)
  t[b - 1].append(a)

for i in range(n):
  print(len(t[i]), end=' ')
  t[i].sort()
  for j in range(len(t[i])):
    print(t[i][j], end=' ')
  print()
