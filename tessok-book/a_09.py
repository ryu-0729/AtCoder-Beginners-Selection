h, w, n = map(int, input().split())
A = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
for _ in range(n):
  a, b, c, d = map(int, input().split())
  A[a][b] += 1
  A[c + 1][d + 1] += 1
  A[c + 1][b] -= 1
  A[a][d + 1] -= 1

B = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
for i in range(1, h + 2):
  for j in range(1, w + 2):
    B[i][j] = B[i][j - 1] + A[i][j]
for i in range(1, w + 2):
  for j in range(1, h + 2):
    B[j][i] = B[j - 1][i] + B[j][i]

for i in range(1, h + 1):
  for j in range(1, w + 1):
    print(B[i][j], end=' ')
  print('')
