n = int(input())
a = list(map(int, input().split()))

x = [0 for _ in range(2 * n + 2)]

for i in range(n):
  ai = a[i]
  index = i + 1
  x[2 * index] = x[ai] + 1
  x[2 * index + 1] = x[ai] + 1

for i in range(1, 2 * n + 2):
  print(x[i])
