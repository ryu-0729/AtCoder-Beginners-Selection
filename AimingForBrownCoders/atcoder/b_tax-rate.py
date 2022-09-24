# B - Tax Rate
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b
N = int(input())

isFlag = False
for i in range(N + 1):
  x = i * 1.08
  if N == int(x):
    isFlag = True
    print(i)

if not isFlag:
  print(':(')
