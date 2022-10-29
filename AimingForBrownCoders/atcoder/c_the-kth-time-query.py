# C - The Kth Time Query
# https://atcoder.jp/contests/abc235/tasks/abc235_c
# NOTE: 解説見て実装
from collections import defaultdict


n, q = map(int, input().split())
a = list(map(int, input().split()))
# TODO: 連想配列の使い方を学習
p = defaultdict(list)

# NOTE: a[i]をキーとして何番目に現れるかを保存
for i in range(n):
  p[a[i]].append(i + 1)

for _ in range(q):
  x, k = map(int, input().split())
  if k <= len(p[x]):
    print(p[x][k - 1])
  else:
    print(-1)
