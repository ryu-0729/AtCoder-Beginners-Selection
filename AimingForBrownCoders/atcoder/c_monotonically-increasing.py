# C - Monotonically Increasing
# https://atcoder.jp/contests/abc263/tasks/abc263_c
import itertools


n, m = map(int, input().split())

# NOTE: mCn通りの組み合わせを出力
for p in itertools.combinations(range(1, m + 1), n):
  for i in range(len(p)):
    print(p[i], end=' ')
  print()
