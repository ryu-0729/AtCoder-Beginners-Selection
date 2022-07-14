# 064 - All Zero 数列の書き換え
n, k = map(int, input().split())
a = list(map(int, input().split()))
sum = sum(a)

if sum % 2 != k % 2 or sum > k:
  print('No')
else:
  print('Yes')
