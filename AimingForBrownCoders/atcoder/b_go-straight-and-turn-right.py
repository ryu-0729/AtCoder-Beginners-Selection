# B - Go Straight and Turn Right
# https://atcoder.jp/contests/abc244/tasks/abc244_b
n = int(input())
s = str(input())
x, y = 0, 0
d = 'b'

for i in range(n):
  if s[i] == 'S':
    if d == 'a':
      y += 1
    elif d == 'b':
      x += 1
    elif d == 'c':
      y -= 1
    elif d == 'd':
      x -= 1
  if s[i] == 'R':
    if d == 'a':
      d = 'b'
    elif d == 'b':
      d = 'c'
    elif d == 'c':
      d = 'd'
    elif d == 'd':
      d = 'a'

print(x, y)
