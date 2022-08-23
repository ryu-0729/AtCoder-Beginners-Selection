# 066 - Three Cards

n, k = map(int, input().split())
sideEvent = 0

for a in range(1, n + 1):
  for b in range(max(1, a - (k - 1)), min(n, a + (k - 1)) + 1):
    for c in range(max(1, a - (k - 1)), min(n, a + (k - 1)) + 1):
      if abs(b - c) < k: sideEvent += 1

print(n ** 3 - sideEvent)
