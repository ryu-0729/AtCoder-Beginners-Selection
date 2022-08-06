# B - Ancestor
# NOTE: 解説を参考に実装
n = int(input())
p = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
  dp[i] = dp[p[i - 1] - 1] + 1

print(dp[n - 1])
