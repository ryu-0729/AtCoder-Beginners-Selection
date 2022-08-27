# Circle in a Rectangle
W, H, x, y, r = map(int, input().split())
isTrue = True

if x - r < 0 or x + r > W:
  isTrue = False

if y - r < 0 or y + r > H:
  isTrue = False

if isTrue:
  print('Yes')
else:
  print('No')
