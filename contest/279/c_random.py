# C - RANDOM
# https://atcoder.jp/contests/abc279/tasks/abc279_c
# NOTE: 解説見て実装
h, w = map(int, input().split())
s = [[] for _ in range(h)]
for i in range(h):
  x = str(input())
  for v in x:
    s[i].append(v)
# NOTE: sの転置を行う
st = [list(x) for x in zip(*s)]
st.sort()

t = [[] for _ in range(h)]
for i in range(h):
  x = str(input())
  for v in x:
    t[i].append(v)
# NOTE: tの転置を行う
tt = [list(x) for x in zip(*t)]
tt.sort()

print('Yes') if st == tt else print('No')
