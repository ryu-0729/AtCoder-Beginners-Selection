# 028 - Frog 1
n = int(input())
h = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
  if i == 0: dp[i] = 0
  if i == 1: dp[i] = abs(h[i - 1] - h[i])
  if i >= 2:
    value1 = dp[i - 2] + abs(h[i - 2] - h[i])
    value2 = dp[i - 1] + abs(h[i - 1] - h[i])
    dp[i] = min(value1, value2)

print(dp[n - 1])
