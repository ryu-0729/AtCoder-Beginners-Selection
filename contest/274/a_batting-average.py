a, b = map(int, input().split())
x = b / a
ans = str(round(x, 3))
print(ans.ljust(5, '0'))
