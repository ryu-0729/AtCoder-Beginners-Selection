n , a, b = map(int, input().split())

def total(n: int):
  total = 0
  while n > 0:
    total += n % 10
    n = n // 10
  return total

answer = 0
for i in range(1, n + 1):
  result = total(i)
  if a <= result <= b:
    answer += i

print(answer)
