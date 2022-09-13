# Sum of Numbers
while True:
  x = str(input())
  if int(x) == 0: break

  answer = 0
  for i in range(len(x)):
    answer += int(x[i])

  print(answer)
