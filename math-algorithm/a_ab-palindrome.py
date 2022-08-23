# A - AB Palindrome

# NOTE: 解説の確認
n = int(input())
s = input()
print('Yes' if (s[0] == 'B' or s[-1] == 'A') and s != 'BA' else 'No')
