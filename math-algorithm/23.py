# 062 - Teleporter
import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))
first = [-1 for _ in range(n + 1)]
second = [-1 for _ in range(n + 1)]
cnt = 0
cur = 1

while True:
  if first[cur] == -1:
    first[cur] = cnt
  elif second[cur] == -1:
    second[cur] = cnt

  if cnt == k:
    print(cur)
    sys.exit()
  elif second[cur] != -1 and (k - first[cur]) % (second[cur] - first[cur]) == 0:
    print(cur)
    sys.exit()
  else:
    cur = a[cur - 1]
    cnt += 1
