# B - Mex
# https://atcoder.jp/contests/abc245/tasks/abc245_b
n = int(input())
a = set(map(int, input().split()))

for i in range(2001):
  if not i in a:
    print(i)
    break
