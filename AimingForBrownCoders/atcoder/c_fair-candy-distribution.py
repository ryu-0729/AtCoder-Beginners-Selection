# C - Fair Candy Distribution
# https://atcoder.jp/contests/abc208/tasks/abc208_c
# NOTE: 解説見て修正
n, k = map(int, input().split())
a = list(map(int, input().split()))
p = {}
for i in range(n):
  p[a[i]] = 0
allGive = k // n
b = a.copy()
b.sort()
for i in range(k % n):
  p[b[i]] += 1

for ai in a:
  print(p[ai] + allGive)
