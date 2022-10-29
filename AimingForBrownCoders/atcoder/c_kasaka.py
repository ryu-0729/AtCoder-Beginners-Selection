# C - kasaka
# https://atcoder.jp/contests/abc237/tasks/abc237_c
# NOTE: 解説見て実装
s = str(input())
n = len(s)
l, r = 0, n - 1

while l < r and s[l] == 'a' and s[r] == 'a':
  l += 1
  r -= 1
while l < r and s[r] == 'a':
  r -= 1
while l < r and s[l] == s[r]:
  l += 1
  r -= 1

print('Yes') if l >= r else print('No')
