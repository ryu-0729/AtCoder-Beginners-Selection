# D - Yet Another Recursive Function
# https://atcoder.jp/contests/abc275/tasks/abc275_d
# NOTE: 解説見て、メモ化再帰をしる。。。
import math
from functools import lru_cache


n = int(input())
@lru_cache
def f(n):
  if n == 0: return 1
  return f(math.floor(n // 2)) + f(math.floor(n // 3))

print(f(n))
