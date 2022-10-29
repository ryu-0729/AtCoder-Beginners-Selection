# A - Not Overflow
# https://atcoder.jp/contests/abc237/tasks/abc237_a
n = int(input())
x = -2 ** 31
y = 2 ** 31
print('Yes') if x <= n < y else print('No')
