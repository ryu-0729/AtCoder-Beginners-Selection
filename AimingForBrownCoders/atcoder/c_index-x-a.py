# C - Index × A(Continuous ver.)
# https://atcoder.jp/contests/abc267/tasks/abc267_c
# NOTE: 解説見て実装
# TODO: なんとなくの理解しかできていない。

N, M = map(int, input().split())
A = list(map(int, input().split()))
s, t = 0, 0

for i in range(M):
  s += A[i] * (i + 1)
  t += A[i]

ans = s
# NOTE: 組み合わせの通り数は(N - M)になる
for i in range(N - M):
  ns = s - t + A[i + M] * M
  nt = t - A[i] + A[i + M]
  s = ns
  t = nt
  ans = max(ans, s)

print(ans)
