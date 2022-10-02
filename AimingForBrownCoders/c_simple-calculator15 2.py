# Simple Calculator
while True:
  a, op, b = input().split()
  a = int(a)
  b = int(b)
  if op == '?':
    break

  if op == '+':
    print(a + b)
    continue
  if op == '-':
    print(a - b)
    continue
  if op == '*':
    print(a * b)
    continue
  if op == '/':
    print(a // b)
    continue
