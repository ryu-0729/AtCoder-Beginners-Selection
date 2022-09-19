# D - Lucky PIN
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
N = int(input())
S = str(input())

cnt = 0
for i in range(1000):
  checkStr = str(i).zfill(3)
  f = 0
  for j in range(N):
    if S[j] == checkStr[f]: f += 1
    if f == 3: break
  if f == 3: cnt += 1

print(cnt)
