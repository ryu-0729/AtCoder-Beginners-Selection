# 049 - Fibonacci Easy (mod 1000000007)
n = int(input())
a = [0] * (n)
mod = 1000000007

a[0] = 1
a[1] = 1
for i in range(2, n):
  a[i] = (a[i - 1] + a[i - 2]) % mod

print(a[n - 1] % mod)
