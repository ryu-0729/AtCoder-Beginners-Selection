# C - Friends and Travel costs
# https://atcoder.jp/contests/abc203/tasks/abc203_c
# NOTE: 解説見て実装
n, k = map(int, input().split())
friend = []
for i in range(n):
  a, b = map(int, input().split())
  friend.append((a, b))

friend.sort()
p = 0
ans = k

while p < n and friend[p][0] <= ans:
  ans += friend[p][1]
  p += 1

print(ans)
