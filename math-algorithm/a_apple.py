# A - Apple 解説
x, y , n = map(int, input().split())

if y < x * 3:
  print(((n // 3) * y + (n % 3) * x))
else:
  print(x * n)
