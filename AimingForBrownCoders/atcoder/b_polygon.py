# B - Polygon
# https://atcoder.jp/contests/abc117/tasks/abc117_b
n = int(input())
l = list(map(int, input().split()))
maxL = max(l)
l.remove(maxL)
suml = sum(l)
if maxL < suml:
  print('Yes')
else:
  print('No')
