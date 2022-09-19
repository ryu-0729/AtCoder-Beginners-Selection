# NOTE: ビット演算の論理積、論理和、排他的論理和の計算(AND, OR, XOR)
def bitOperation(a: int, b: int):
  print(a & b)
  print(a | b)
  print(a ^ b)

# NOTE: 使用例
a, b = map(int, input().split())
bitOperation(a, b)
