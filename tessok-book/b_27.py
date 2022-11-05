a, b = map(int, input().split())

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

x = a * b
g = 0
if a > b:
  g = gcd(a, b)
else:
  g = gcd(b, a)

print(x // g)
