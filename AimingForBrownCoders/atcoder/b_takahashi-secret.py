# B - Takahashi's Secret
# https://atcoder.jp/contests/abc228/tasks/abc228_b
n, x = map(int, input().split())
a = list(map(int, input().split()))
s = [False for _ in range(n)]
s[x - 1] = True

while True:
  s[x - 1] = True
  x = a[x - 1]
  if s[x - 1]: break

cnt = 0
for t in s:
  if t: cnt += 1

print(cnt)
