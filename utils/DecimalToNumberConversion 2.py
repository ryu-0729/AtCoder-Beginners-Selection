# NOTE: 10進数を2進数に変換
def decimalToNumberConversion(n):
  res = ''
  while n >= 1:
    if (n % 2 == 0): res = '0' + res
    if (n % 2 == 1): res = '1' + res
    n = n // 2

  return 0 if not res else res

# NOTE: 使用例
N = int(input())
print(decimalToNumberConversion(N))
