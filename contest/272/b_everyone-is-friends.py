# B - Everyone is Friends
# https://atcoder.jp/contests/abc272/tasks/abc272_b
n, m = map(int, input().split())
x = []
for i in range(m):
  x.append(list(map(int, input().split()))[1::])

a = [[False for _ in range(n)] for _ in range(n)]
# TODO: 少々無駄がある。。。
for i in range(m):
  for j in range(len(x[i])):
    for k in range(len(x[i])):
      key = x[i][j] - 1
      value = x[i][k] - 1
      a[key][value] = True
      a[value][key] = True

ans = True
for i in range(n):
  for j in range(n):
    if i == j: continue
    if not a[i][j]:
      ans = False
      break
  if not ans:
    break

if ans:
  print('Yes')
else:
  print('No')
