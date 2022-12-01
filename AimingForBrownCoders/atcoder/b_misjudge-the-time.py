# B - Misjudge the Time
# https://atcoder.jp/contests/abc278/tasks/abc278_b
# NOTE: 解説見て修正
h, m = map(int, input().split())

def check(h: int, m: int):
  h2 = (h // 10) * 10 + m // 10
  m2 = (h % 10) * 10 + m % 10
  return h2 <= 23 and m2 <= 59

while not check(h, m):
  m += 1
  if m == 60:
    m = 0
    h += 1
  if h == 24: h = 0

print(h, m)
