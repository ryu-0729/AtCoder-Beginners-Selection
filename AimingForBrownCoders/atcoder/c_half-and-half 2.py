# C - Half and Half
# https://atcoder.jp/contests/abc095/tasks/arc096_a
A, B, C, X, Y = map(int, input().split())
AB = C * 2

res = 10 ** 10
for i in range((10 ** 5) + 1):
  total = i * AB + (max(0, X - i) * A) + (max(0, Y - i) * B)
  res = min(res, total)

print(res)
