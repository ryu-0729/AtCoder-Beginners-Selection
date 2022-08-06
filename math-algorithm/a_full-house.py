# A - Full House
card = list(map(int, input().split()))
card3 = False
card2 = False

for i in range(len(card)):
  if card.count(card[i]) == 3:
    card3 = True

  if card.count(card[i]) == 2:
    card2 = True

  if card3 and card2:
    break

if card3 and card2:
  print('Yes')
else:
  print('No')

# NOTE: 下記解説の解答例
card.sort()
if (card[0] == card[2] and card[3] == card[4]) or (card[0] == card[1] and card[2] == card[4]):
  print('Yes')
else:
  print('No')