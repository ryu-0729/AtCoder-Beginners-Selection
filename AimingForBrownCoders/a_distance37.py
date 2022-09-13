# Distance
import math

x1, y1, x2, y2 = map(float, input().split())
x = abs(x2 - x1) ** 2
y = abs(y2 - y1) ** 2
print(math.sqrt(x + y))
