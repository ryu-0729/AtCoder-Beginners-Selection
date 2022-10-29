# A - Integer Sum
# https://atcoder.jp/contests/abc272/tasks/abc272_a
n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
  ans += a[i]

print(ans)
