# C - たくさんの数式
# https://atcoder.jp/contests/abc045/tasks/arc061_a
S = str(input())
N = len(S) - 1

total = 0
for i in range(1 << N):
  res = ''
  for j in range(len(S)):
    res += S[j]
    if (i >> j) & 1:
      res += '+'

  total += eval(res)

print(total)

# NOTE: 別回答
""" for i in range(1 << N):
  res = ''
  for j, s in enumerate(S):
    print(s)
    res += s
    if (i >> j) & 1:
      res += '+'

  total += eval(res)

print(total) """
