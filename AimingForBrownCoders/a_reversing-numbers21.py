# Reversing Numbers
n = int(input())
a = list(map(int, input().split()))
lst = []

for i in range(1, n + 1):
  lst.append(a[-i])

print(' '.join(map(str, lst)))
