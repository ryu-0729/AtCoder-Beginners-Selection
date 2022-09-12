# Shuffle
while True:
  S = str(input())
  if S == '-': break
  m = int(input())

  for i in range(m):
    h = int(input())
    subS = S[0:h]
    idx = S.find(subS)
    S = S[idx + len(subS):] + subS

  print(S)
