n, x = map(int, input().split())
a = list(map(int, input().split()))

isAns = False
for i in range(n):
  if a[i] == x:
    isAns = True
    break

if isAns:
  print('Yes')
else:
  print('No')
