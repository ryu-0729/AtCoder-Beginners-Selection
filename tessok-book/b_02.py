a, b = map(int, input().split())

isAns = False
for i in range(a, b + 1):
  if 100 % i == 0:
    isAns = True
    break

if isAns:
  print('Yes')
else:
  print('No')
