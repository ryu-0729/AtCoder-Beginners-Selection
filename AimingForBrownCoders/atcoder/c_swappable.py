# C - Swappable
# https://atcoder.jp/contests/abc206/tasks/abc206_c
# NOTE: 解説見て実装
n = int(input())
a = list(map(int, input().split()))
x = {}
ans = 0

for j in range(n):
  y = 0
  if a[j] in x:
    y = x[a[j]]
  else:
    x[a[j]] = 0
  # NOTE: a[j]を見た時にそれよりも前の値で条件を満たす個数をカウント。値が同じ場合はマイナスする
  ans += j - y
  x[a[j]] += 1

print(ans)
