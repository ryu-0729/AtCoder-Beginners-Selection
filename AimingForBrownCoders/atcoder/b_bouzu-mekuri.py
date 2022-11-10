# B - Bouzu Mekuri
# https://atcoder.jp/contests/abc210/tasks/abc210_b
n = int(input())
s = str(input())

ans = ''
for i in range(n):
  if s[i] == '1':
    if i & 1:
      print('Aoki')
      exit()
    else:
      print('Takahashi')
      exit()
