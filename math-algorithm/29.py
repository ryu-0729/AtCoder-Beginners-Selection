# 017 - Least Common Multiple of N Integers

def GCD(a, b):
  while a >= 1 and b >= 1:
    if a < b:
      b = b % a
    else:
      a = a % b

  if a >= 1:
    return a
  return b

def LCM(a, b):
  return int(a / GCD(a, b)) * b

n = int(input())
a = list(map(int, input().split()))
answer = LCM(a[0], a[1])
for i in range(2, n):
  answer = LCM(answer, a[i])

print(answer)
