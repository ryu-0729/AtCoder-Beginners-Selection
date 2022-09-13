# Toggling Cases
S = str(input())
# swapcase()を使用する場合
# print(S.swapcase())
answer = ''

for i in range(len(S)):
  if S[i].isupper():
    answer += S[i].lower()
  elif S[i].islower():
    answer += S[i].upper()
  else:
    answer += S[i]

print(answer)
