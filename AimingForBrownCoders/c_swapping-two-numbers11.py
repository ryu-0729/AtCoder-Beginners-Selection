# Swapping Two Numbers
while True:
  numbers = list(map(int, input().split()))

  if numbers[0] == 0 and numbers[1] == 0:
    break

  numbers.sort()
  print(numbers[0], numbers[1])
