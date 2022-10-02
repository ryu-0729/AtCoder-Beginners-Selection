n = int(input())
d = [None for _ in range(n)]
for i in range(n):
  d[i] = int(input())
d = list(set(d))
print(len(d))
