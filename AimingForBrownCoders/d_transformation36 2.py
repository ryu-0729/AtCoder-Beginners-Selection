# Transformation
str = str(input())
q = int(input())

for i in range(q):
  x = list(input().split())

  if x[0] == 'print':
    print(str[int(x[1]):int(x[2]) + 1])
    continue
  if x[0] == 'reverse':
    reversStr = str[int(x[1]):int(x[2]) + 1]
    str = str[:int(x[1])] + reversStr[::-1] + str[int(x[2]) + 1:]
    continue
  if x[0] == 'replace':
    replaceStr = str[int(x[1]):int(x[2]) + 1]
    replaceStr = replaceStr.replace(replaceStr, x[3])
    str = str[:int(x[1])] + replaceStr + str[int(x[2]) + 1:]
    continue
