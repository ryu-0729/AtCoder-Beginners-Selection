# C - Cheese
# https://atcoder.jp/contests/abc229/tasks/abc229_c
# NOTE: 解説見て実装。

n, w = map(int, input().split())
c = []
for _ in range(n):
  a, b = map(int, input().split())
  c.append((a, b))

c.sort(reverse=True)
ans = 0
for i in range(n):
  x = min(w, c[i][1])
  ans += x * c[i][0]
  w -= x

print(ans)
