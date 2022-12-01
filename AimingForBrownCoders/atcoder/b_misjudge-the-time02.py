# # B - Misjudge the Time
# https://atcoder.jp/contests/abc278/tasks/abc278_b
# NOTE: シンプルに文字列操作で判定したパターン
h, m = map(int, input().split())

def check(h: int, m: int):
  zh = str(h).zfill(2)
  zm = str(m).zfill(2)
  h2 = zh[0] + zm[0]
  m2 = zh[1] + zm[1]
  return int(h2) <= 23 and int(m2) <= 59

while not check(h, m):
  m += 1
  if m == 60:
    m = 0
    h += 1
  if h == 24: h = 0

print(h, m)
