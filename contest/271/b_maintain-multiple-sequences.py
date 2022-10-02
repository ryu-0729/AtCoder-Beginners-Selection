# B - Maintain Multiple Sequences
# https://atcoder.jp/contests/abc271/tasks/abc271_b
n, q = map(int, input().split())
l = []
for i in range(n):
  x = list(map(int, input().split()))
  l.append(x)

for i in range(q):
  s, t = map(int, input().split())
  print(l[s - 1][t])
