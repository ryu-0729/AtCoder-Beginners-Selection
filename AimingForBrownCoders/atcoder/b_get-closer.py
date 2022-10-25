# B - Get Closer
# https://atcoder.jp/contests/abc246/tasks/abc246_b
import math


a, b = map(int, input().split())
d = math.sqrt(a ** 2 + b ** 2)

# TODO: 下記解説にて確認
x = a / d
y = b / d
print(f"{x:.10f} {y:.10f}")
