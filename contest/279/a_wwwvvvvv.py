# A - wwwvvvvvv
# https://atcoder.jp/contests/abc279/tasks/abc279_a
s = str(input())
vCnt = s.count('v')
wCnt = s.count('w')
ans = vCnt + (wCnt * 2)
print(ans)
