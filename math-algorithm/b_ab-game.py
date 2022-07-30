# B - AB Game

# NOTE: 不正解例 TLE
n, a, b = map(int, input().split())
counter = 0

for i in range(1, n + 1):
  if i % a == 0 or ((i - (a * (i // a))) % b != 0 and i > a):
    counter += 1

print(counter)

# NOTE: 解説 Answer
n, a, b = map(int, input().split())

def f(x):
  return x // a * min(a, b) + min(x % a, b - 1)

print(max(f(n) - f(a - 1), 0))
