# Spreadsheet
r, c = map(int, input().split())
cells = [[0 for _ in range(c)] for _ in range(r + 1)]

for i in range(r):
  numbers = list(map(int, input().split()))
  cells[i] = numbers
  cells[i].append(sum(numbers))

for i in range(r + 1):
  for j in range(c):
    if i != r:
      cells[r][j] += cells[i][j]

  if i == r:
    total = sum(cells[i])
    print(' '.join(map(str, cells[i])), total)
  else:
    print(' '.join(map(str, cells[i])))
