# Distance II
import math


n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

p1, p2, p3, p = 0.0, 0.0, 0.0, 0.0
for i in range(n):
  p1 += abs(x[i] - y[i])
  p2 += abs(x[i] - y[i]) ** 2
  p3 += abs(x[i] - y[i]) ** 3
  p = max(p, abs(x[i] - y[i]))

print(p1)
print(math.sqrt(p2))
print(p3 ** (1 / 3))
print(p)
