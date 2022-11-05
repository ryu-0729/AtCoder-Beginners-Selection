# 再帰関数 ユークリッドの互除法
A = list(map(int, input().split()))

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

if A[0] > A[1]:
  print(gcd(A[0], A[1]))
else:
  print(gcd(A[1], A[0]))
