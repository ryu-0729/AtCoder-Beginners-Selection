# B - Let's Get a Perfect Score
# https://atcoder.jp/contests/abc282/tasks/abc282_b
n, m = map(int, input().split())
s = ['' for _ in range(n)]
for i in range(n):
    s[i] = str(input())

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        isPerfect = True
        for k in range(m):
            if s[i][k] == 'x' and s[j][k] == 'x':
                isPerfect = False
                break
        if isPerfect:
            cnt += 1

print(cnt)
