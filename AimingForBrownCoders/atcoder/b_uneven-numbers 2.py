# B - Uneven Numbers
N = int(input())

res = 0
for i in range(1, N + 1):
  if len(str(i)) % 2 != 0:
    res += 1

print(res)
