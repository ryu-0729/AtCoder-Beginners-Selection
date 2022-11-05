# C - Ringo's Favorite Numbers 2
# https://atcoder.jp/contests/abc200/tasks/abc200_c
# NOTE: 解説を参考に実装
n = int(input())
a = list(map(int, input().split()))
x = {}
for i in range(n):
  if a[i] % 200 in x:
    x[a[i] % 200] += 1
  else:
    x[a[i] % 200] = 1

ans = 0
for val in x.values():
  ans += val * (val - 1) // 2

print(ans)
