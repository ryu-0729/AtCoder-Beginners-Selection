# A - When?
# https://atcoder.jp/contests/abc258/tasks/abc258_a
k = int(input())
h = 1260
x = h + k
h = x // 60
m = x % 60
if m < 10:
  m = '0' + str(m)

print(str(h) + ':' + str(m))
