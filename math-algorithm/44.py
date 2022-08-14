# 051 - Combination Hard part2
x, y = map(int, input().split())
mod = 1000000007
fact = [0] * 200009

def division(a, b, m):
  return (a * pow(b, m - 2, m)) % m

def ncr(n, r, fact, m):
  return division(fact[n], fact[r] * fact[n - r] % m, m)

fact[0] = 1
for i in range(1, 200001):
  fact[i] = i * fact[i - 1] % mod

print(ncr(x + y, y, fact, mod))
