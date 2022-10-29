# B - Achieve the Goal
# https://atcoder.jp/contests/abc151/tasks/abc151_b
n, k, m = map(int, input().split())
a = list(map(int, input().split()))
aT = sum(a)

ans = -1
for i in range(k + 1):
  if (aT + i) // n >= m:
    ans = i
    break

print(ans)
