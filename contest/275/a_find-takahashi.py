n = int(input())
h = list(map(int, input().split()))

maxh = max(h)
ans = 0
for i in range(n):
  if h[i] == maxh:
    ans = i + 1

print(ans)
