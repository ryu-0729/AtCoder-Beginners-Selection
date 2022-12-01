# A - Shift
# https://atcoder.jp/contests/abc278/tasks/abc278_a
n, k = map(int, input().split())
a = list(map(int, input().split()))

while True:
  if k == 0: break
  a.remove(a[0])
  a.append(0)
  k -= 1

for x in a:
  print(x, end=' ')
