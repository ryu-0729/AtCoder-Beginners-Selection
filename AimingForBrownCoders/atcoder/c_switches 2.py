# C - Switches
# https://atcoder.jp/contests/abc128/tasks/abc128_c
N, M = map(int, input().split())
switch = []
for _ in range(M):
  switch.append(list(map(int, input().split()))[1:])
p = list(map(int, input().split()))

answer = 0
for i in range(2 ** N):
  isOk = True
  for j in range(M):
    sum = 0
    for k in range(N):
      # TODO: k + 1の理解が不十分
      if (i >> k) & 1 and k + 1 in switch[j]: sum += 1

    if sum % 2 != p[j]:
      isOk = False
  if isOk: answer += 1

print(answer)
