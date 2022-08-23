# 050 - Power
a, b = map(int, input().split())
print(pow(a, b, 1000000007))

# 繰り返し2乗法実装
def modPow(a, b, mod):
  p, answer = a, 1
  for i in range(30):
    # TODO: ビット演算子について学習する
    if (b & (1 << i) != 0):
      answer *= p
      answer %= mod

    p *= p
    p %= mod

  return answer

print(modPow(a, b, 1000000007))
