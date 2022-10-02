# B - Better Students Are Needed!
# https://atcoder.jp/contests/abc260/tasks/abc260_b
# 解説見て実装
N, X, Y, Z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ok = [False for _ in range(N)]

P = []
for i in range(N):
  P.append([-a[i], i])
P.sort()
for i in range(X):
  ok[P[i][1]] = True

P = []
for i in range(N):
  if not ok[i]:
    P.append([-b[i], i])
P.sort()
for i in range(Y):
  ok[P[i][1]] = True

P = []
for i in range(N):
  if not ok[i]:
    P.append([-a[i] + -b[i], i])
P.sort()
for i in range(Z):
  ok[P[i][1]] = True

for i in range(N):
  if ok[i]: print(i + 1)
