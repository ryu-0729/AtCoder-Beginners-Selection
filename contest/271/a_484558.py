# A - 484558
# https://atcoder.jp/contests/abc271/tasks/abc271_a
n = int(input())
x = format(n, 'x').upper()
if len(x) == 1:
  print('0' + x)
else:
  print(x)

# 解説確認
print("{:02X}".format(int(input())))
