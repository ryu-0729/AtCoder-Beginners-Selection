# C - One More aab aba baa
# https://atcoder.jp/contests/abc215/tasks/abc215_c
import itertools


s, k = map(str, input().split())
k = int(k)
x = set()
for p in itertools.permutations(range(len(s))):
  newS = ''
  for i in p:
    newS += s[i]
  x.add(newS)

y = list(x)
y.sort()
print(y[k - 1])
