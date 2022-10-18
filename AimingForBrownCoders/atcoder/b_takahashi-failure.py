# B - Takahashi's Failure
# https://atcoder.jp/contests/abc252/tasks/abc252_b
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

isTrue = False
maxA = max(a)
for i in range(n):
  if a[i] == maxA:
    if b.count(i + 1) > 0:
      isTrue = True

if isTrue:
  print('Yes')
else:
  print('No')
