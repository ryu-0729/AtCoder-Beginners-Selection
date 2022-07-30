# 068 - Number of Multiples 2

def GCD(a, b):
  if b == 0: return a
  return GCD(b, a % b)

def LCM(a, b):
  result = GCD(a, b) if a > b else GCD(b, a)
  return int(a / result) * b

n, k = map(int, input().split())
v = list(map(int, input().split()))
answer = 0

# NOTE: ビット全探索についての理解が不十分
for i in range(1, (1 << k)):
  cnt = 0
  lcm = 1
  for j in range(k):
    if (i & (1 << j)) != 0:
      cnt += 1
      lcm = LCM(lcm, v[j])
  num = n // lcm
  if cnt % 2 == 1: answer += num
  if cnt % 2 == 0: answer -= num

print(answer)
