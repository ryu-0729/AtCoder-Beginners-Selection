# Grading
while True:
  m, f, r = map(int, input().split())
  if m == -1 and f == -1 and r == -1: break

  mf = m + f
  if (m == -1 or f == -1) or mf < 30:
    print('F')
    continue
  if mf >= 80:
    print('A')
    continue
  if 65 <= mf < 80:
    print('B')
    continue
  if 50 <= mf < 65:
    print('C')
    continue
  if 30 <= mf < 50:
    if r >= 50:
      print('C')
      continue
    print('D')
    continue
