# 067 - Cross Sum
h, w = map(int, input().split())
gyou = [[] for _ in range(h)]
retu = [[] for _ in range(w)]
a = [[] for _ in range(h)]
for i in range(h):
  a[i] = list(map(int, input().split()))
answer = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
  gyou[i] = 0
  for j in range(w):
    gyou[i] += a[i][j]

for i in range(w):
  retu[i] = 0
  for j in range(h):
    retu[i] += a[j][i]

for i in range(h):
  for j in range(w):
    answer[i][j] = gyou[i] + retu[j] - a[i][j]

for i in answer:
  print(*i)
