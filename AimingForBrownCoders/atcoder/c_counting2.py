# C - Counting 2
# https://atcoder.jp/contests/abc231/tasks/abc231_c
# NOTE: 解説見て実装。2分探索。
from bisect import bisect_left


n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for _ in range(q):
  x = int(input())
  index = bisect_left(a, x)
  print(n - index)
