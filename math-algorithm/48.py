# 077 - Distance Sum
n = int(input())
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
for i in range(n):
  x[i], y[i] = map(int, input().split())

x.sort()
y.sort()

xTotal = 0
yTotal = 0

for i in range(1, n + 1):
  xTotal += x[i - 1] * (-n + (2 * i) - 1)
  yTotal += y[i - 1] * (-n + (2 * i) - 1)

print(xTotal + yTotal)
