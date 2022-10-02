# C - March
# https://atcoder.jp/contests/abc089/tasks/abc089_c
S = 'MARCH'
N = int(input())
c = [0 for _ in range(5)]
for i in range(N):
  s = str(input())
  for j in range(5):
    if S[j] == s[0]:
      c[j] += 1

cnt = 0
# NOTE: 3人の選び方を全探索
for i in range(5):
  for j in range(i + 1, 5):
    for k in range(j + 1, 5):
      # NOTE: 積の法則により答えを導く
      cnt += c[i] * c[j] * c[k]

print(cnt)
