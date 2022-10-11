t = int(input())
n = int(input())
a = [0 for _ in range(t + 1)]
for i in range(n):
  l, r = map(int, input().split())
  a[l] += 1
  a[r] -= 1

b = [0 for _ in range(t + 1)]
for i in range(1, t + 1):
  b[i] = b[i - 1] + a[i - 1]
  print(b[i])
