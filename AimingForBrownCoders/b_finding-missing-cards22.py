# Finding Missing Cards
n = int(input())
cards = [[False for _ in range(13)] for _ in range(4)]
marks = ['S', 'H', 'C', 'D']
# S = 0, H = 1, C = 2, D = 3

for i in range(n):
  mark, number = input().split()
  mark = str(mark)
  number = int(number)

  if mark == 'S':
    cards[0][number - 1] = True
    continue
  if mark == 'H':
    cards[1][number - 1] = True
    continue
  if mark == 'C':
    cards[2][number - 1] = True
    continue
  if mark == 'D':
    cards[3][number - 1] = True

for i in range(4):
  for j in range(13):
    if cards[i][j] == False:
      print(marks[i], end = ' ')
      print(j + 1)
