# C - Route Map
# https://atcoder.jp/contests/abc236/tasks/abc236_c
n, m = map(int, input().split())
s = list(map(str, input().split()))
t = list(map(str, input().split())) # NOTE: この値を集合で扱うことで楽に解けたみたい。。sの値が存在するか判定する
ans = [False for _ in range(n)]

sd = {}
for i in range(n):
  sd[s[i]] = i

now = 0
for i in range(m):
  if sd[t[i]] >= now:
    ans[sd[t[i]]] = True
    now = sd[t[i]]

for i in range(n):
  if ans[i]:
    print('Yes')
  else:
    print('No')
