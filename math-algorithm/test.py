n, k = map(int, input().split())
a, b, c = [0.0] * n, [0.0] * n, [0.0] * n
answer = [0.0] * n

for i in range(n):
  a[i], b[i], c[i] = map(float, input().split())

for i in range(n):
  for j in range(i + 1, n):
    if a[i] * b[j] == a[j] * b[i]: continue
    if a[i] == a[j] and b[i] == b[j] and c[i] == c[j]: continue

    px = (c[i] * b[j] - c[j] * b[i]) / (a[i] * b[j] - a[j] * b[i])
    py = (c[i] * a[j] - c[j] * a[i]) / (b[i] * a[j] - b[j] * a[i])

    result = True
    for k in range(n):
      if a[k] * px + b[k] * py > c[k]:
        result = False

    if result:
      answer[i] = px + py

answer.sort()
print(answer)
