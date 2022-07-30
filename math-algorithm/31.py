# 008 - Brute Force 1

n, s = map(int, input().split())

answer = 0
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i + j <= s: answer += 1

print(answer)
