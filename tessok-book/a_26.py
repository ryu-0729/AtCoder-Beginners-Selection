import math


q = int(input())

def isPrime(n):
  x = math.sqrt(n)
  for i in range(2, int(x) + 1):
    if n % i == 0: return False

  return True

for i in range(q):
  xi = int(input())
  print('Yes') if isPrime(xi) else print('No')
