# A - You should output ARC, though this is ABC.
# https://atcoder.jp/contests/abc255/tasks/abc255_a
r, c = map(int, input().split())
a = []
for i in range(2):
  a.append(list(map(int, input().split())))

print(a[r - 1][c - 1])
