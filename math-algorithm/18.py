# 009 動的計画法 部分和問題
n, s = map(int, input().split())
list = list(map(int, input().split()))
dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
  for j in range(s + 1):
    if j < list[i - 1]:
      dp[i][j] = dp[i - 1][j]
    if j >= list[i - 1]:
      if dp[i - 1][j] == True or dp[i - 1][j - list[i - 1]] == True:
        dp[i][j] = True
      else:
        dp[i][j] = False

if dp[n][j] == True:
  print('Yes')
else:
  print('No')
