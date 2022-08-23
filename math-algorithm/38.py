# 073 - Sum of Maximum
n = int(input())
a = list(map(int, input().split()))

mod = 1000000007
power = [0 for _ in range(n)]
power[0] = 1
for i in range(1, n):
  power[i] = (2 * power[i - 1]) % mod

answer = 0
for i in range(n):
  answer += power[i] * a[i]
  answer %= mod

print(answer)
