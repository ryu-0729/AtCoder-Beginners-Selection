# B - Unique Nicknames
# https://atcoder.jp/contests/abc247/tasks/abc247_b
# TODO: 復習必要
n = int(input())
x = []
for i in range(n):
  x.append(list(map(str, input().split())))

for i in range(n):
  isAns = False
  for j in range(len(x[i])):
    isOk = True
    for k in range(n):
      if i == k: continue
      if x[k][0] == x[i][j] or x[k][1] == x[i][j]:
        isOk = False
    if isOk:
      isAns = True
  if not isAns:
    print('No')
    exit()

print('Yes')
