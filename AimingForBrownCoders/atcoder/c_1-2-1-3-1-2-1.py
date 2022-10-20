# C - 1 2 1 3 1 2 1
# https://atcoder.jp/contests/abc247/tasks/abc247_c
# NOTE: 再帰関数でも実装する
n = int(input())
s = ['' for _ in range(n + 1)]
s[1] = '1 '
for i in range(2, n + 1):
  s[i] = s[i - 1] + str(i) + ' ' + s[i - 1]

print(s[n])
