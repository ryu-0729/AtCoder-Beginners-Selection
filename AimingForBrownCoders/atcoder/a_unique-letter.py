# A - A Unique Letter
# https://atcoder.jp/contests/abc260/tasks/abc260_a
S = str(input())
ans = '-1'
for i in range(len(S)):
  if S.count(S[i]) == 1:
    ans = S[i]

print(ans)
