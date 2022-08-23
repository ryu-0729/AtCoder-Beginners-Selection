# 024 - Answer Exam Randomly
n = int(input())
answer = 0.0

for i in range(n):
  p, q = map(int, input().split())
  answer += q / p

print(answer)
