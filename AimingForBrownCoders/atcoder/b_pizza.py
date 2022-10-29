# B - Pizza
# https://atcoder.jp/contests/abc238/tasks/abc238_b
# NOTE: 解説見て実装
n = int(input())
a = list(map(int, input().split()))
p = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
  p[i] = (p[i - 1] + a[i - 1]) % 360

p.sort()
p.append(360)
c = [0 for _ in range(n + 1)]
for i in range(n + 1):
  c[i] = abs(p[i] - p[i + 1])

print(max(c))
