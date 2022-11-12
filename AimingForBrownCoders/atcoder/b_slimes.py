# B - Slimes
# https://atcoder.jp/contests/abc248/tasks/abc248_b
a, b, k = map(int, input().split())
s = 0
while True:
  if a >= b: break
  s += 1
  a *= k

print(s)
