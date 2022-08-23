# 070 - Axis-Parallel Rectangle
def checkNumpoints(n, x, y, lx, rx, ly, ry):
  cnt = 0
  for i in range(n):
    if lx <= x[i] <= rx and ly <= y[i] <= ry:
      cnt += 1

  return cnt

n, k = map(int, input().split())
x, y = [0] * n, [0] * n

for i in range(n):
  x[i], y[i] = map(int, input().split())

answer = 10 ** 20
for lx in range(n):
  for rx in range(n):
    for ly in range(n):
      for ry in range(n):
        cl = x[lx]
        cr = x[rx]
        dl = y[ly]
        dr = y[ry]
        if checkNumpoints(n, x, y, cl, cr, dl, dr) >= k:
          area = (cr - cl) * (dr - dl)
          answer = min(answer, area)

print(answer)
