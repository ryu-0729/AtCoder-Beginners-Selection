# 061 - Stones Game 2
n = int(input())

answer = 'First'
for i in range(1, 61):
  if 2 ** i - 1 == n:
    answer = 'Second'

print(answer)
