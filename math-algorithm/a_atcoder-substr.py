# A - "atcoder".substr()
l, r = map(int, input().split())
a = ['a', 't', 'c', 'o', 'd', 'e', 'r']

answer = ''
for i in range(r):
  if i < l - 1: continue
  answer += a[i]

print(answer)
