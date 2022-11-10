# C - Neo-lexicographic Ordering
# https://atcoder.jp/contests/abc219/tasks/abc219_c
# NOTE: 解説見て実装
x = str(input())
n = int(input())
s = ['' for _ in range(n)]
for i in range(n):
  s[i] = str(input())

# NOTE: 対応表を作る
f = {}
g = {}
for i in range(26):
  f[x[i]] = chr(ord('a') + i)
  g[chr(ord('a') + i)] = x[i]

# NOTE: 入力内容をa-zの形に変換
for i in range(n):
  newS = ''
  for j in range(len(s[i])):
    newS += f[s[i][j]]
  s[i] = newS
s.sort()
# NOTE: 元の対応表に戻す
for i in range(n):
  newS = ''
  for j in range(len(s[i])):
    newS += g[s[i][j]]
  s[i] = newS

for i in range(n):
  print(s[i])
