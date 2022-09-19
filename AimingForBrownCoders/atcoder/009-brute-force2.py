# 009 - Brute Force 2
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_i
N, S = map(int, input().split())
A = list(map(int, input().split()))

# NOTE: ビット全探索
answerflag = False
for i in range(2 ** N):
  sum = 0
  for j in range(N):
    # NOTE: >> はiをj桁分右シフトを行い、その桁が1だった場合に合計に含める
    if ((i >> j) & 1): sum += A[j]
  if sum == S:
    answerflag = True
    break

if answerflag:
  print('Yes')
else:
  print('No')
