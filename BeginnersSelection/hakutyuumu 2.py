""" import re


S = str(input())

isMatch = re.match("^(dream|dreamer|erase|eraser)+$", S)
if isMatch:
  print('YES')
else:
  print('NO') """

S = str(input())
x = ['eraser', 'erase', 'dreamer', 'dream']

for i in range(4):
  S = S.replace(x[i], '0')

S = S.replace('0', '')

if len(S) <= 0:
  print('YES')
else:
  print('NO')
