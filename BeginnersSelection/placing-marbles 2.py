s = str(input())

counter = 0
for i in range(3):
  if int(s[i]) == 1:
    counter += 1

print(counter)
