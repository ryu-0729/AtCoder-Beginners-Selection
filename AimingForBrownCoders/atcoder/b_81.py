# B - 81

n = int(input())

isFlag = False
for i in range(1, 10):
  for j in range(i, 10):
    if i * j == n:
      isFlag = True

if isFlag:
  print('Yes')
else:
  print('No')
