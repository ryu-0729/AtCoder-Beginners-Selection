# いまいち理解不十分
n = int(input())
A = [[0 for _ in range(1501)] for _ in range(1501)]
for _ in range(n):
  a, b, c, d = map(int, input().split())
  A[a][b] += 1
  A[c][d] += 1
  A[a][d] -= 1
  A[c][b] -= 1

# B = [[0 for _ in range(1501)] for _ in range(1501)]
for i in range(0, 1501):
  for j in range(1, 1501):
    A[i][j] = A[i][j - 1] + A[i][j]
for i in range(1, 1501):
  for j in range(0, 1501):
    A[i][j] = A[i - 1][j] + A[i][j]

ans = 0
for i in range(1501):
  for j in range(1501):
    if A[i][j] >= 1:
      ans += 1

print(ans)
