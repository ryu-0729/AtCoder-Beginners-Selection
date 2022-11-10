# B - Mongeness
# https://atcoder.jp/contests/abc224/tasks/abc224_b
h, w = map(int, input().split())
a = []
for i in range(h):
  a.append(list(map(int, input().split())))

isAns = True
for i in range(h - 1):
  for j in range(w - 1):
    if not a[i][j] + a[i + 1][j + 1] <= a[i + 1][j] + a[i][j + 1]:
      isAns = False

print('Yes') if isAns else print('No')
