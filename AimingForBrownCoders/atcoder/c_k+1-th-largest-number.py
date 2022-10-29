# C - (K+1)-th Largest Number
# https://atcoder.jp/contests/abc273/tasks/abc273_c
# NOTE: 解説見て実装
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
p = defaultdict(int)

# TODO: 出現数をカウントするロジックが理解できていない
for i in range(n):
  p[a[i]] += 1

ans = []
for v in p.values():
  ans.append(v)

while True:
  if len(ans) == n: break
  ans.append(0)

for i in range(n):
  print(ans[i])
