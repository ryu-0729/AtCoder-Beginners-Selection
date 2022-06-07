# 3.3.4
N = int(input())

Answer = 0
for i in range(1, N + 1):
  Answer += 1 * N / i

print('%.12f' % Answer)
