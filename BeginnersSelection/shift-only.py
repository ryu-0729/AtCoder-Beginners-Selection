n = int(input())
a = list(map(int, input().split()))

counter = 0
isTrue = True
while True:
  for i in range(n):
    if a[i] % 2 != 0:
      isTrue = False
    else:
      a[i] = a[i] // 2

  if isTrue == False:
    break
  else:
    counter += 1

print(counter)
