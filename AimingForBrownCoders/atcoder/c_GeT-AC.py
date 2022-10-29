# C - GeT AC
# https://atcoder.jp/contests/abc122/tasks/abc122_c
# NOTE: 解説見ずに初めて解けた累積和
n, q = map(int, input().split())
s = str(input())
a = [0 for _ in range(n)]
for i in range(1, n):
  if s[i] == 'C' and s[i - 1] == 'A':
    a[i] = a[i - 1] + 1
  else:
    a[i] = a[i - 1]

for i in range(q):
  l, r = map(int, input().split())
  print(a[r - 1] - a[l - 1])
