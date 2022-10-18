# A - Adjacent Squares
# https://atcoder.jp/contests/abc250/tasks/abc250_a
h, w = map(int, input().split())
r, c = map(int, input().split())

ans = 0
for i in range(1, h + 1):
  for j in range(1, w + 1):
    x = abs(r - i) + abs(c - j)
    if x == 1: ans += 1

print(ans)
