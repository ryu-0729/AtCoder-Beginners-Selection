n = int(input())
a = list(map(int, input().split()))

aPoint = 0
bPoint = 0
for i in range(1, n + 1):
  selectCard = max(a)
  if i % 2 == 0:
    bPoint += selectCard
  else:
    aPoint += selectCard

  a.remove(selectCard)

print(aPoint - bPoint)
