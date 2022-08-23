# 再帰関数 階乗
N = int(input())

def gmp(n):
  if n == 1:
    return 1

  return gmp(n - 1) * n

print('%.12f' % gmp(N))
