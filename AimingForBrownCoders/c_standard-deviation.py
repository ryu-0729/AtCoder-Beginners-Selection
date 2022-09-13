# Standard Deviation
import math
from statistics import mean


while True:
  n = int(input())
  if n == 0: break
  s = list(map(float, input().split()))
  m = mean(s)
  res = 0.0
  for i in range(n):
    res += (s[i] - m) ** 2

  print(math.sqrt(res / n))
