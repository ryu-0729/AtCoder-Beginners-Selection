# C - Poem Online Judge
# https://atcoder.jp/contests/abc251/tasks/abc251_c
# NOTE: 解説を見て微修正
n = int(input())
s = ['' for _ in range(n)]
t = [0 for _ in range(n)]
for i in range(n):
  S, T = map(str, input().split())
  s[i] = S
  t[i] = int(T)

st = set()
ori = [False for _ in range(n)]
for i in range(n):
  if not s[i] in st:
    ori[i] = True
  st.add(s[i])

maxP = 0
index = 0
for i in range(n):
  if not ori[i]: continue
  if maxP < t[i]:
    maxP = t[i]
    index = i

print(index + 1)
