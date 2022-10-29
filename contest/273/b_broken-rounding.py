# B - Broken Rounding
# https://atcoder.jp/contests/abc273/tasks/abc273_b
from decimal import ROUND_HALF_UP, Decimal


x, k = map(int, input().split())

for i in range(k):
  x = int(Decimal(x).quantize(Decimal('1E' + str(i + 1)), rounding=ROUND_HALF_UP))

print(x)
