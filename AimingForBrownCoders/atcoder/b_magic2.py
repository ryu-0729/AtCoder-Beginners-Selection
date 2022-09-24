# B - Magic 2
# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_b
A, B, C = map(int, input().split())
K = int(input())

# 貪欲法
# NOTE: A < B < Cかつ操作回数cnt <= K の時に条件が成り立つ
bCnt = 0
while True:
  if B > A: break
  B = B * 2
  bCnt += 1

cCnt = 0
while True:
  if C > B: break
  C = C * 2
  cCnt += 1

if bCnt + cCnt <= K:
  print('Yes')
else:
  print('No')

# 全探索
# NOTE: A, B, Cをそれぞれ2倍にする場合の操作を全探索する。1 << i = 2のi乗
isFlag = False
for i in range(K + 1):
  for j in range(K + 1):
    for k in range(K + 1):
      a = A * (1 << i)
      b = B * (1 << j)
      c = C * (1 << k)
      if i + j + k <= K and a < b and b < c:
        isFlag = True

if isFlag:
  print('Yes')
else:
  print('No')
