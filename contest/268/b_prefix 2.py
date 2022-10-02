S = str(input())
T = str(input())

length = 0
if len(S) >= len(T):
  length = len(S)
else:
  length = len(T)

strT = ''
isAnswer = False
for i in range(length):
  if i > len(T) - 1: break
  strT += T[i]
  if strT == S:
    isAnswer = True

if isAnswer:
  print('Yes')
else:
  print('No')
