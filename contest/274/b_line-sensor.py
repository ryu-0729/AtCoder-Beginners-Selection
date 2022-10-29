h, w = map(int, input().split())
c = []
for i in range(h):
  c.append(str(input()))
cnt = [0 for _ in range(w)]
for i in range(h):
  for j in range(w):
    if c[i][j] == '#':
      cnt[j] += 1

for i in range(w):
  print(cnt[i], end=' ')
