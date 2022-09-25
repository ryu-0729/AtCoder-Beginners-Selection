# C - Count Order
# https://atcoder.jp/contests/abc150/tasks/abc150_c
# NOTE: 解説等見ないで初めて実装できた順列探索
import itertools


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

num = 1
a = 0
b = 0
for p in itertools.permutations(range(1, N + 1)):
  isA = True
  isB = True
  for i in range(N):
    if p[i] != P[i]:
      isA = False
    if p[i] != Q[i]:
      isB = False
  if isA:
    a = num
  if isB:
    b = num

  num += 1

print(abs(a - b))
