# Structured Programming
n = int(input())

print(' ', end = '')
for i in range(1, n + 1):
  if i % 3 == 0:
    print(i, end = ' ')
    continue

  x = i
  while x > 0:
    if x % 10 == 3:
      print(i, end = ' ')
      break

    x = x // 10
