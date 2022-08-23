# 3.4.3
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Answer = 0
for i in range(N):
  Result = (A[i] * (1 / 3)) + (B[i] * (2 / 3))
  Answer += Result

print('%.12f' % Answer)
