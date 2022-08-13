# B - Nice Grid
r, c = map(int, input().split())
isBlack = False

if r == 1 or r == 15:
  isBlack = True
elif (r == 2 or r == 14) and (c == 1 or c == 15):
  isBlack = True
elif (r == 3 or r == 13) and (c != 2 or c != 14):
  isBlack = True
elif (r == 4 or r == 12) and (c == 1 or c == 3 or c == 13 or c == 15):
  isBlack = True
elif (r == 5 or r == 11) and (c == 1 or c == 3 or c == 13 or (5 <= c <= 11) or c == 15):
  isBlack = True
elif (r == 6 or r == 10) and (c == 1 or c == 3 or c == 5 or c == 11 or c == 13 or c == 15):
  isBlack = True
elif (r == 7 or r == 9) and (c == 1 or c == 3 or c == 5 or (7 <= c <= 9) or c == 11 or c == 13 or c == 15):
  isBlack = True
elif r == 8 and (c == 1 or c == 3 or c == 5 or c == 7 or c == 9 or c == 11 or c == 13 or c == 15):
  isBlack = True
else:
  isBlack = False

if isBlack:
  print('black')
else:
  print('white')

# 解説解答 チェビシェフ距離（チェス盤距離）
if max(abs(r - 8), abs(c - 8)) % 2:
  print('black')
else:
  print('white')
