# A - Median?
# https://atcoder.jp/contests/abc253/tasks/abc253_a
x = list(map(int, input().split()))
b = x[1]
x.sort()

if b == x[1]:
  print('Yes')
else:
  print('No')
