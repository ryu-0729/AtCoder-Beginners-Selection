n = int(input())
t = [0 for _ in range(n + 1)]
x = [0 for _ in range(n + 1)]
y = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
  T, X, Y = map(int, input().split())
  t[i] = T
  x[i] = X
  y[i] = Y

can = True
for i in range(n):
  dt = t[i + 1] - t[i]
  dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
  if dt < dist: can = False
  if dist % 2 != dt % 2: can = False

if can:
  print('Yes')
else:
  print('No')
