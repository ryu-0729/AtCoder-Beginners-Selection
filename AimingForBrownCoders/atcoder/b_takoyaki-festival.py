# B - TAKOYAKI FESTIVAL 2019
# https://atcoder.jp/contests/abc143/tasks/abc143_b
n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(n):
  for j in range(i + 1, n):
    ans += d[i] * d[j]

print(ans)
