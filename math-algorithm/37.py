# 072 - Max GCD 2
import math

a, b = map(int, input().split())

def isShouMondai(a, b, t):
  cl = math.floor(b / t)
  cr = math.ceil(a / t)
  if cl - cr >= 1: return True

  return False

answer = 0
for i in range(1, b + 1):
  if isShouMondai(a, b, i):
    answer = i

print(answer)
