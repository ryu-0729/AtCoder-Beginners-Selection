# B - Papers, Please
# https://atcoder.jp/contests/abc155/tasks/abc155_b
n = int(input())
a = list(map(int, input().split()))

canApprove = True
for i in range(n):
  if not a[i] & 1:
    if a[i] % 3 == 0 or a[i] % 5 == 0:
      continue
    else:
      canApprove = False

if canApprove:
  print('APPROVED')
else:
  print('DENIED')
