# C - Min Max Pair
# https://atcoder.jp/contests/abc262/tasks/abc262_c
# NOTE: 解説見て実装
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
  a[i] -= 1
ans = 0

# NOTE: iとa[i]が同一のものをxとするとxから2つ選択するためxC2
x = 0
for i in range(n):
  if i == a[i]: x += 1
ans = x * (x - 1) // 2

# NOTE: iが決まればjが決まることに関してはなんとなくの理解。。
for i in range(n):
  if i >= a[i]: continue
  if a[a[i]] == i: ans += 1

print(ans)
