# A - Lacked Number
# https://atcoder.jp/contests/abc248/tasks/abc248_a
s = str(input())

for i in range(10):
  if not s.count(str(i)):
    print(i)
    break
