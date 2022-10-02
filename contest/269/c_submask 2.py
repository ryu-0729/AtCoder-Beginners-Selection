# C - Submask
# https://atcoder.jp/contests/abc269/tasks/abc269_c

# NOTE: 他の人のソースを参考に実装
""" N = int(input())
A = []
cur = 0
x = N
while True:
  if x == 0: break
  if (x & 1) == 1:
    A.append(cur)

  cur += 1
  x >>= 1

M = len(A)
for i in range(1 << M):
  res = 0
  for j in range(M):
    if (i >> j) & 1:
      res += 1 << A[j]

  print(res) """

# NOTE: 解説動画見ての実装
N = int(input())
s = N
ans = []
while True:
  ans.append(s)
  if s == 0: break
  s = (s - 1) & N

ans.sort()
for i in range(len(ans)):
  print(ans[i])
