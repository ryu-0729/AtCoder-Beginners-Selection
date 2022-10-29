n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [0 for _ in range(n + 1)]
# NOTE: 累積和を求める
for i in range(1, n + 1):
  b[i] = b[i - 1] + a[i - 1]

for _ in range(q):
  l, r = map(int, input().split())
  print(b[r] - b[l - 1])
