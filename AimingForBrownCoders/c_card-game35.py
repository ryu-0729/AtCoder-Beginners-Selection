# Card Game
n = int(input())
tPoint, hPoint = 0, 0
for i in range(n):
  tCard, hCard = map(str, input().split())
  if tCard == hCard:
    tPoint += 1
    hPoint += 1
    continue
  if tCard > hCard:
    tPoint += 3
    continue
  if hCard > tCard:
    hPoint += 3
    continue

print(tPoint, hPoint)
