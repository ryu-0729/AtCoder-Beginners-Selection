# A - Rightmost
# https://atcoder.jp/contests/abc276/tasks/abc276_a
s = str(input())
ans = -1
for i in range(len(s)):
  if s[i] == 'a':
    ans = i + 1
print(ans)
