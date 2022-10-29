# B - Explore
# https://atcoder.jp/contests/abc265/tasks/abc265_b
n, m, t = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
b = [0 for _ in range(n + 1)]
for _ in range(m):
  x, y = map(int, input().split())
  b[x] = y

isFlg = True
isActive = 1
for i in range(1, n):
  t += b[i]
  t -= a[i]
  if t > 0:
    isActive += 1
  else:
    isFlg = False
    break

if isFlg:
  print('Yes')
else:
  print('No')
