# B - 1D Pawn
# https://atcoder.jp/contests/abc257/tasks/abc257_b
n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
P = [False for _ in range(n + 1)]
for i in range(k):
  P[A[i]] = True

for i in range(q):
  target = A[L[i] - 1]
  if target == n: continue
  if not P[target + 1]:
    P[target] = False
    P[target + 1] = True
    A[L[i] - 1] = target + 1

for i in range(len(A)):
  print(A[i], end=' ')
