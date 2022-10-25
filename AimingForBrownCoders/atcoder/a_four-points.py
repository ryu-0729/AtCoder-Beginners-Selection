# A - Four Points
# https://atcoder.jp/contests/abc246/tasks/abc246_a
# NOTE: 解説見て実装
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ansX = 0
if x1 == x2:
  ansX = x3
if x1 == x3:
  ansX = x2
if x2 == x3:
  ansX = x1

ansY = 0
if y1 == y2:
  ansY = y3
if y1 == y3:
  ansY = y2
if y2 == y3:
  ansY = y1

print(ansX, ansY)
