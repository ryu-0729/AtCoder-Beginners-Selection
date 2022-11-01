# C - Long Sequence
# https://atcoder.jp/contests/abc220/tasks/abc220_c
# NOTE: 解説見て実装。復習必要
n = int(input())
a = list(map(int, input().split()))
x = int(input())
s = sum(a)
p = x // s

ans = p * n
now = p * s
for i in range(n):
  now += a[i]
  ans += 1
  if now > x: break

print(ans)
