a, b, c, d, e, f = map(int, input().split())
mod = 998244353

x = a * b * c
y = d * e * f

print((x - y) % mod)
