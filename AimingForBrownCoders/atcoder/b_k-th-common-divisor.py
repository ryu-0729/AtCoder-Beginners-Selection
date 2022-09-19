# B - K-th Common Divisor
A, B, K = map(int, input().split())
divisionList = []

for i in range(1, 101):
  if A % i == 0 and B % i == 0:
    divisionList.append(i)

divisionList.sort(reverse=True)
print(divisionList[K - 1])
