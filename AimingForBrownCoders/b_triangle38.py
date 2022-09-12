# Triangle
import math


a, b, c = map(float, input().split())

rad = math.radians(c)
sin = math.sin(rad)
cos = math.cos(rad)
height = b * sin

area = 0.5 * a * height
print(area)
C = math.sqrt((b ** 2) + (a ** 2) - ((2 * b * a) * cos))
length = a + b + C
print(length)
print(height)
