# C - 100 to 105
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c
# TODO: 完璧に理解しているわけではない
X = int(input())

for i in range(X + 1):
  res = X - i * 100
  if 0 <= res and res <= 5 * i:
    print('1')
    exit()
  if res < 0: break

print('0')
