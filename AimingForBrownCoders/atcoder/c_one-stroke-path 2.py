# C - One-stroke Path
# https://atcoder.jp/contests/abc054/tasks/abc054_c
# TODO: パターンの全列挙はできたが処理がうまくできていない。。。
import itertools


N, M = map(int, input().split())
A = [0 for _ in range(M)]
B = [0 for _ in range(M)]
for i in range(M):
  a, b = map(int, input().split())
  A[i] = a
  B[i] = b

print(A)
print(B)

cnt = 0
for p in itertools.permutations(range(1, N + 1)):
  patrn = []
  for i in range(M - 1):
    if p[0] != 1:
      break
    patrn = p

  if len(patrn) <= 0: continue
  cnt += 1

print(cnt)
