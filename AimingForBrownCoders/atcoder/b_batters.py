# B - Batters
# https://atcoder.jp/contests/abc256/tasks/abc256_b
n = int(input())
a = list(map(int, input().split()))
m = [0 for _ in range(4)]
p = 0

for i in range(n):
  m[0] = 1
  nm = [0 for _ in range(4)]
  for j in range(4):
    if m[j] == 1:
      if j + a[i] >= 4:
        p += 1
      else:
        nm[j + a[i]] = 1
  m = nm

print(p)
