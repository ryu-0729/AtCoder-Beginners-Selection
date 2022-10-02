X, Y, Z = map(int, input().split())

ans = -1
if 0 < X:
  # 壁なし
  if 0 > Y or Y >= X:
    ans = X
  if 0 < Y < X:
    if 0 < Z < Y:
      ans = X
    if Z < 0:
      ans = (abs(Z) * 2) + X
else:
  if 0 < Y or Y <= X:
    ans = X * -1
  if 0 > Y > X:
    if 0 > Z > Y:
      ans = X * -1
    if Z > 0:
      ans = Z * 2 + (X * -1)

print(ans)
