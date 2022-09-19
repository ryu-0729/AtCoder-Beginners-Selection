# B - 105
N = int(input())

def isFactorCount8(n):
  counter = 0
  for i in range(1, n + 1):
    if n % i == 0:
      counter += 1
  if counter == 8:
    return 1
  else:
    return 0

res = 0
for i in range(1, N + 1):
  if i % 2 != 0:
    res += isFactorCount8(i)

print(res)
