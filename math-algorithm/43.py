# 051 - Combination Hard
x, y = map(int, input().split())
mod = 1000000007

def division(a, b, mod):
  return (a * pow(b, mod - 2, mod)) % mod

bunshi, bunbo = 1, 1
for i in range(1, x + y + 1):
  bunshi *= i
  bunshi %= mod
for i in range(1, x + 1):
  bunbo *= i
  bunbo %= mod
for i in range(1, y + 1):
  bunbo *= i
  bunbo %= mod

print(division(bunshi, bunbo, mod))
