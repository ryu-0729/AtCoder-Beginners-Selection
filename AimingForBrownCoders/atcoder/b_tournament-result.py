# B - Tournament Result
# https://atcoder.jp/contests/abc261/tasks/abc261_b
N = int(input())
A = ['' for _ in range(N)]

for i in range(N):
  A[i] = str(input())

ans = 'correct'
for i in range(N):
  if ans == 'incorrect': break
  for j in range(N):
    if A[i][j] == '-': continue
    if A[i][j] == 'W' and A[j][i] != 'L':
      ans = 'incorrect'
      break
    if A[i][j] == 'L' and A[j][i] != 'W':
      ans = 'incorrect'
      break
    if A[i][j] == 'D' and A[j][i] != 'D':
      ans = 'incorrect'
      break

print(ans)
