# B - Alcoholic
# https://atcoder.jp/contests/abc189/tasks/abc189_b
# NOTE: 解説見て修正。floatの誤差に気を付ける
n, x = map(int, input().split())

def addAlco(v: int, p: int):
  return v * p

nowAlco = 0
ans = -1
for i in range(n):
  v, p = map(int, input().split())
  nowAlco += addAlco(v, p)
  if nowAlco > x * 100:
    ans = i + 1
    break

print(ans)
