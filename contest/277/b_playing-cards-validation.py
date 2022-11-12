n = int(input())
isAns = True

s = ['' for _ in range(n)]
for i in range(n):
  s[i] = str(input())

def first(x):
  if x[0] == 'H' or x[0] == 'D' or x[0] == 'C' or x[0] == 'S':
    return True
  return False
def second(x):
  xList = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
  if x[1] in xList:
    return True
  return False

sList = []
for x in s:
  if not first(x):
    isAns = False
    break
  if not second(x):
    isAns = False
    break
  if x in sList:
    isAns = False
    break
  sList.append(x)
  
print('Yes') if isAns else print('No')
