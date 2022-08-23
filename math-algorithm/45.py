# 023 - Dice Expectation
n = int(input())
b = list(map(int, input().split()))
r = list(map(int, input().split()))

blue, red = 0.0, 0.0
for i in range(n):
  blue += b[i] / n
  red += r[i] / n

print(blue + red)
