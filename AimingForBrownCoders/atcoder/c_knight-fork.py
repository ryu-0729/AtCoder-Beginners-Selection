# C - Knight Fork
# https://atcoder.jp/contests/abc239/tasks/abc239_c
# NOTE: 解説見て実装
x1, y1, x2, y2 = map(int, input().split())

def f(sx, sy):
  p = []
  for i in range(-2, 3):
    for j in range(-2, 3):
      if i ** 2 + j ** 2 != 5: continue
      p.append((sx + i, sy + j))
  return p

p1 = f(x1, y1)
p2 = f(x2, y2)

# NOTE: 2つの集合の共通部分判定
print('Yes') if set(p1) & set(p2) else print('No')
