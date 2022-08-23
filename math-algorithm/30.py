# 017 - Least Common Multiple of N Integers

# NOTE: 再帰関数のバージョン
def GCD(a, b):
  if b == 0: return a
  return GCD(b, a % b)

def LCM(a, b):
  result = GCD(a, b) if a > b else GCD(b, a)
  return int(a / result) * b

n = int(input())
a = list(map(int, input().split()))
answer = LCM(a[0], a[1])
for i in range(2, n):
  answer = LCM(answer, a[i])

print(answer)
