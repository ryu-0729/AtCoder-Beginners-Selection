# B - Cakes and Donuts
# https://atcoder.jp/contests/abc105/tasks/abc105_b
N = int(input())
c = 4
d = 7

isFlag = False
for i in range(N):
  for j in range(N):
    if N == (c * i) + (d * j):
      isFlag = True

if isFlag:
  print('Yes')
else:
  print('No')
