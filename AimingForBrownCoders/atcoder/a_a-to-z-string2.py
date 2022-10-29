# A - A to Z String 2
# https://atcoder.jp/contests/abc257/tasks/abc257_a
n, x = map(int, input().split())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''
for i in range(len(alpha)):
  ans += alpha[i] * n

print(ans[x - 1])
