# Counting Characters
import re


numbersCount = [0 for _ in range(26)]
alpha = [chr(i) for i in range(97, 97 + 26)]
while True:
  try:
    S = str(input())
    S = S.lower()
    replaceS = re.sub(r"[^a-z]", '', S)
    for i in range(len(replaceS)):
      num = ord(replaceS[i]) - ord('a')
      numbersCount[num] += 1
  except EOFError:
    break

for i in range(26):
  print(alpha[i] + ' :', numbersCount[i])
