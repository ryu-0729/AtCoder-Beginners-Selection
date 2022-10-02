# C - Guess The Number
# https://atcoder.jp/contests/abc157/tasks/abc157_c
N, M = map(int, input().split())
S = [0 for _ in range(M)]
C = [0 for _ in range(M)]
for i in range(M):
  s, c = map(int, input().split())
  S[i] = s
  C[i] = c

num = -1
for i in range(1000):
  strI = str(i)
  if len(strI) != N: continue
  isFlag = True
  for j in range(M):
    if int(strI[S[j] - 1]) != C[j]: isFlag = False

  if isFlag:
    num = i
    break

print(num)
