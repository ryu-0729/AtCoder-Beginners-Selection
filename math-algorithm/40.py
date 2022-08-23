# 075 - Pyramid
n = int(input())
a = list(map(int, input().split()))
mod = 1000000007
fact = [None] * 200009

def division(a, b, m):
  return (a * pow(b, m - 2, m)) % m

def ncr(n, r, fact, m):
  return division(fact[n], fact[r] * fact[n - r] % m, m)

fact[0] = 1
for i in range(1, 200001):
  fact[i] = i * fact[i - 1] % mod

answer = 0
for i in range(n):
  answer += a[i] * ncr(n - 1, i, fact, mod)
  answer %= mod

print(answer)
