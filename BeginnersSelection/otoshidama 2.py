n, Y = map(int, input().split())

x, y, z = -1, -1, -1
for i in range(n + 1):
  for j in range(n + 1):
    k = n - i - j
    if k < 0: continue
    total = 10000 * i + 5000 * j + 1000 * k
    if Y == total and i + j + k == n:
      x, y, z = i, j, k

print(x, y, z)
