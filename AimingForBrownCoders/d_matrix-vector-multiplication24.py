# Matrix Vector Multiplication
n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
b = [0 for _ in range(m)]

for i in range(n):
  numbersA = list(map(int, input().split()))
  a[i] = numbersA

for i in range(m):
  numbersB = int(input())
  b[i] = numbersB

for i in range(n):
  c = 0
  for j in range(m):
    c += a[i][j] * b[j]

  print(c)
