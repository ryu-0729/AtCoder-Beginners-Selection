# A - Generalized ABC
# https://atcoder.jp/contests/abc282/tasks/abc282_a
import string


k = int(input())
alpha = string.ascii_uppercase

a = ''
for i in range(k):
    a = a + alpha[i]

print(a)
