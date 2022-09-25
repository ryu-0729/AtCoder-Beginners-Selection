# NOTE: 常に最適な方法をとる貪欲法では不正解
# TODO: dpで解くらしい（動的計画法）
N, K = map(int, input().split())
A = list(map(int, input().split()))

def maxStone(n, a):
  res = 0
  while True:
    maxS = max(a)
    if n >= maxS:
      res = maxS
      break
    a.remove(maxS)

  return res

cnt = 0
turn = 0
while True:
  if N <= 0: break
  x = maxStone(N, A)
  N -= x
  if turn % 2 == 0:
    cnt += x
  turn += 1

print(cnt)
