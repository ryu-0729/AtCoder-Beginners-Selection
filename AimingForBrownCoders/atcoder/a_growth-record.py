# A - Growth Record
# https://atcoder.jp/contests/abc259/tasks/abc259_a
n, m, x, t, d = map(int, input().split())

if x <= m:
  print(t)
  exit()

print(t - (x - m) * d)
