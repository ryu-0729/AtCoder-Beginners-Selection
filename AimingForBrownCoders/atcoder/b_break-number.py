# B - Break Number
# https://atcoder.jp/contests/abc068/tasks/abc068_b
N = int(input())

def division(n):
  cnt = 0
  while True:
    div = n % 2
    if div == 0:
      n = n // 2
      cnt += 1
    else:
      break

  return cnt

cnt = 0
ans = 1
for i in range(1, N + 1):
  res = division(i)
  if cnt < res:
    cnt = res
    ans = i

print(ans)