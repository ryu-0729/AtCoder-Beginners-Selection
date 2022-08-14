# 023 - Dice Expectation
n = int(input())
b = list(map(int, input().split()))
r = list(map(int, input().split()))

blue, red = 0.0, 0.0
for i in range(n):
  blue += 1.0 * b[i] / n
  red += 1.0 * r[i] / n

print(blue + red)
