n = int(input())
mod = 1000000007
a = [0 for _ in range(n + 1)]
a[1] = 1
a[2] = 1
for i in range(3, n + 1):
  a[i] = (a[i - 1] + a[i - 2]) % mod

print(a[n])
