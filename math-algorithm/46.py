# 024 - Answer Exam Randomly
n = int(input())
answer = 0.0

for i in range(n):
  p, q = map(int, input().split())
  answer += 1.0 * q / p

print(answer)
