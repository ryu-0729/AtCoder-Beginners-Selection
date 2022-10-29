n = int(input())
a = list(map(int, input().split()))
p = [0 for _ in range(n + 1)]
q = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
  p[i] = max(p[i - 1], a[i - 1])
for i in range(n - 1, 0, -1):
  if i == n - 1:
    q[i + 1] = a[i]
  q[i] = max(q[i + 1], a[i - 1])

d = int(input())
for _ in range(d):
  l, r = map(int, input().split())
  ans = max(p[l - 1], q[r + 1])
  print(ans)
