# B - Distance Between Tokens
# https://atcoder.jp/contests/abc253/tasks/abc253_b
h, w = map(int, input().split())
s = [[''] for _ in range(h)]
for i in range(h):
  s[i] = str(input())

x = 0
y = 0
for i in range(h):
  for j in range(w):
    if s[i][j] == 'o':
      x = abs(x - i)
      y = abs(y - j)

print(x + y)
