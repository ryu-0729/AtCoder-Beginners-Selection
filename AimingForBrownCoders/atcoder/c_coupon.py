# C - Coupon
# https://atcoder.jp/contests/abc246/tasks/abc246_c
# TODO: 解説見て実装
n, k, x = map(int, input().split())
a = list(map(int, input().split()))
d = [0 for _ in range(n)]
c, ans = 0, 0

# NOTE: 何回クーポンが使えるか、クーポンを適用した時の値を保持
for i in range(n):
  d[i] = a[i] % x
  c += a[i] // x
  ans += a[i]

if c >= k:
  ans -= x * k
else: # クーポンの方が多い場合
  ans -= c * x
  k -= c
  k = min(k, n)
  d.sort(reverse=True)
  for i in range(k):
    ans -= d[i]

print(ans)
