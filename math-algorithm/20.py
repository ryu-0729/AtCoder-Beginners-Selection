# 059 - Power of Two Nの階乗の一の位
n = int(input())

answer = 0
if n % 4 == 1:
  answer = 2
if n % 4 == 2:
  answer = 4
if n % 4 == 3:
  answer = 8
if n % 4 == 0:
  answer = 6

print(answer)
