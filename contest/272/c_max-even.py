# C - Max Even
# https://atcoder.jp/contests/abc272/tasks/abc272_c
# NOTE: 解説を見て実装
n = int(input())
a = list(map(int, input().split()))
x = []
y = []
for i in range(n):
  # if a[i] % 2 == 0:
  if a[i] & 1: # NOTE: bit演算で偶数判定
    x.append(a[i])
  else:
    y.append(a[i])

x.sort(reverse=True)
y.sort(reverse=True)
ans = -1
if len(x) >= 2: ans = x[0] + x[1]
if len(y) >= 2: ans = max(ans, y[0] + y[1])

print(ans)
