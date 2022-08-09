# 074 - Sum of difference Easy
n = int(input())
a = list(map(int, input().split()))

answer = 0
for i in range(1, n + 1):
  answer += a[i - 1] * (-n + (2 * i) - 1 )

print(answer)
