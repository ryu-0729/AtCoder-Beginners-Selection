# 解説を見ての回答

N = int(input())
p = list(map(int, input().split()))
cnt = [0 for _ in range(N)]

for i in range(N):
  for j in range(3):
    cnt[(p[i] - 1 - i + j + N) % N] += 1

answer = 0
for i in range(N):
  answer = max(answer, cnt[i])

print(answer)
