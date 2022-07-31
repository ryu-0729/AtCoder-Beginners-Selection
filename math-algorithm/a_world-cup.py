# A - World Cup

y = int(input())

answer = 0

if y == 3000:
  answer = 3002
else:
  result = y % 4
  if result == 0: answer = y + 2
  if result == 1: answer = y + 1
  if result == 2: answer = y
  if result == 3: answer = y + 3

print(answer)

# NOTE: 修正版
if y % 4 == 0: answer = y + 2
if y % 4 == 1: answer = y + 1
if y % 4 == 2: answer = y
if y % 4 == 3: answer = y + 3

print(answer)
