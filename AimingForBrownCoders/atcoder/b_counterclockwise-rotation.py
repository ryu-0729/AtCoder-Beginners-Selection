# B - Counterclockwise Rotation
# https://atcoder.jp/contests/abc259/tasks/abc259_b
# NOTE: 座標の回転の公式を利用。https://keisan.casio.jp/exec/system/1496883774
import math


a, b, d = map(int, input().split())
rad = math.radians(d)
x = a * math.cos(rad) - b * math.sin(rad)
y = a * math.sin(rad) + b * math.cos(rad)
print(x, y)
