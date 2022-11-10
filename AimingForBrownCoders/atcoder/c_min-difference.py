# C - Min Difference
# https://atcoder.jp/contests/abc212/tasks/abc212_c
# NOTE: 解説見て実装
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ai, bi = 0, 0
ans = 1001001001001001

while ai < n and bi < m:
  ans = min(ans, abs(a[ai] - b[bi]))
  if a[ai] < b[bi]:
    ai += 1
  else:
    bi += 1

print(ans)
