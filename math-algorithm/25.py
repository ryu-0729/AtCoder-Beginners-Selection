# 065 - Bishop
h, w = map(int, input().split())
cells = h * w

if h == 1 or w == 1:
  print(1)
else:
  print((cells + 1) // 2)
