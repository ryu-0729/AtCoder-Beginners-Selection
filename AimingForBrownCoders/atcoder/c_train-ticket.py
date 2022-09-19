# C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c
A = [int(x) for x in input()]

for i in range(2 ** 3):
  op = ['-'] * 3
  for j in range(3):
    if ((i >> j) & 1): op[2 - j] = '+'

  op1, op2, op3 = op[0], op[1], op[2]
  b = op1 + str(A[1])
  c = op2 + str(A[2])
  d = op3 + str(A[3])
  total = A[0] + int(b) + int(c) + int(d)
  if total == 7:
    print(str(A[0]) + b + c + d + '=7')
    break
