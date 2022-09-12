# Finding a Word
w = str(input())
counter = 0
while True:
  t = list(map(str, input().split()))
  if t[0] == 'END_OF_TEXT': break
  for i in range(len(t)):
    if t[i].lower() == w:
      counter += 1

print(counter)
