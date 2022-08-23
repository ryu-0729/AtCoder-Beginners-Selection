# B - Explore 解説
import sys

n , m, t = map(int, input().split())
a = [0] + list(map(int, input().split()))
bounus = [0] * (n + 1)
for _ in range(m):
  x, y = map(int, input().split())
  bounus[x] = y

for i in range(1, n):
  if t <= a[i]:
    print('No')
    sys.exit()
  t -= a[i]
  t += bounus[i + 1]

print('Yes')
