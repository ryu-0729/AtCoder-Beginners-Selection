n = int(input())
num = 0
mod = 10000

for i in range(n):
  t, a = map(str, input().split())
  a = int(a)
  if t == '+':
    num += a
  if t == '-':
    num -= a
  if t == '*':
    num *= a

  # NOTE: 桁数を抑える処理。余りをとるタイミングを変えても計算結果は変わらないため。
  if num < 0: num += mod
  num %= mod

  print(num)
