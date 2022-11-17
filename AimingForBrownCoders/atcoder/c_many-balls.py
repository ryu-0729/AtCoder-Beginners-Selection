# C - Many Balls
# https://atcoder.jp/contests/abc216/tasks/abc216_c
n = int(input())

ans = []
while n > 0:
  if n == 2:
    ans.append('A')
    n -= 1
    continue
  if n & 1:
    ans.append('A')
    n -= 1
  else:
    ans.append('B')
    n //= 2

for a in ans[::-1]:
  print(a, end='')
