# NOTE: 素数判定
import math


def isPrime(n):
  x = math.sqrt(n)
  # NOTE: √nまでで割り切れるかを判定。割り切れない場合は素数
  for i in range(2, int(x) + 1):
    if n % i == 0: return False

  return True
