n = int(input())
a = list(map(int, input().split()))
b1 = [0 for _ in range(n + 1)]
b2 = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
  res = 0
  if a[i - 1] == 1: res = 1
  b1[i] = b1[i - 1] + res
for i in range(1, n + 1):
  res = 0
  if a[i - 1] == 0: res = 1
  b2[i] = b2[i - 1] + res

q = int(input())
for _ in range(q):
  l, r = map(int, input().split())
  x = b1[r] - b1[l - 1]
  y = b2[r] - b2[l - 1]
  if x == y:
    print('draw')
  if x > y:
    print('win')
  if x < y:
    print('lose')
