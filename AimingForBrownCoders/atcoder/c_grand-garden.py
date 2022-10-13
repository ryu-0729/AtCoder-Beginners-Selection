# C - Grand Garden
# https://atcoder.jp/contests/abc116/tasks/abc116_c
# NOTE: 解説見て実装。理解できているかは微妙
n = int(input())
h = list(map(int, input().split()))
ans = 0
active = 0
for i in range(n):
  if active >= h[i]: # 前の操作で既に事足りているか
    active = h[i]
  else:
    ans += h[i] - active
    active = h[i]

print(ans)
