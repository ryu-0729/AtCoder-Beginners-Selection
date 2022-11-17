# C - Kaprekar Number
# https://atcoder.jp/contests/abc192/tasks/abc192_c
n, k = map(int, input().split())

def g1(x: int):
  xList = list(str(x))
  xList.sort(reverse=True)
  return int(''.join(xList))

def g2(x: int):
  xList = list(str(x))
  xList.sort()
  return int(''.join(xList))

def f(x):
  return g1(x) - g2(x)

ans = n
for i in range(k):
  ans = f(ans)

print(ans)
