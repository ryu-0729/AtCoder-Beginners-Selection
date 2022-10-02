# B - Rectangle Detection
# https://atcoder.jp/contests/abc269/tasks/abc269_b
""" strList = ['1111111111' for _ in range(12)]
for i in range(11):
  if i == 0:
    continue
  else:
    S = str(input())
    strList[i] = S

res = [0 for _ in range(4)]
for i in range(12):
  if i == 0 or i == 11: continue
  for j in range(10):
    if strList[i][j] == '#':
      if strList[i - 1][j] != '#':
        res[0] = i
      if strList[i + 1][j] != '#':
        res[1] = i
      if j == 0:
        res[2] = j + 1
      elif strList[i][j - 1] != '#':
        res[2] = j + 1
      if j == 9:
        res[3] = j + 1
      elif strList[i][j + 1] != '#':
        res[3] = j + 1

print(res[0], res[1])
print(res[2], res[3]) """

# 解説参考に修正
# https://atcoder.jp/contests/abc269/editorial/4843
strList = ['' for _ in range(10)]
for i in range(10):
  strList[i] = str(input())

a = 10 ** 9
b = -10 ** 9
c = 10 ** 9
d = -10 ** 9

for i in range(10):
  for j in range(10):
    if strList[i][j] == '#':
      a = min(a, i + 1)
      b = max(b, i + 1)
      c = min(c, j + 1)
      d = max(d, j + 1)

print(a, b)
print(c, d)
