# 072 - Max GCD 2
import math

a, b = map(int, input().split())

def isShouMondai(a, b, t):
  cl = math.floor(b / t) # 床関数
  cr = math.ceil(a / t) # 天井関数
  if cl - cr >= 1: return True

  return False

answer = 0
for i in range(1, b + 1):
  if isShouMondai(a, b, i):
    answer = i

print(answer)
