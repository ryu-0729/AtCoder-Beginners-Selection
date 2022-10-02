# NOTE: アホ回答
A, B = map(int, input().split())
ten1 = 1
ten2 = 2
ten4 = 4
ten = [1, 2, 4]

ans = 0
def check(n):
  res = [False for _ in range(3)]
  while True:
    if n == 0: break
    if n >= ten4:
      n -= ten4
      res[2] = True
    if n >= ten2:
      n -= ten2
      res[1] = True
    if n >= ten1:
      n -= ten1
      res[0] = True
  return res

checkA = check(A)
checkB = check(B)

for i in range(3):
  if not checkA[i] and not checkB[i]:
    continue
  if checkA[i] or checkB[i]:
    ans += ten[i]

print(ans)

# NOTE: 解説回答
# NOTE: 2進数で考える。得点が1, 2, 4で2進数の桁数のため
print(A | B)
