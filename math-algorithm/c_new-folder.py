# C - NewFolder

# TLE
"""
NOTE: 処理手順
・入力文字列を配列に格納していく
・配列内の要素を数え、0以上かそうではないかで出力を変える
"""
n = int(input())
arrayS = []

for i in range(n):
  s = input()
  if arrayS.count(s) == 0:
    print(s)
  else:
    print(s + '(' + str(arrayS.count(s)) + ')')

  arrayS.append(s)

# 上記方法では、毎回配列内の文字列を検索するため、TLEする

# Fix
"""
NOTE: 処理手順
・既に同じ入力文字列を受け取ったかをカウントしておくオブジェクト（辞書？）を作成
・カウントオブジェクトのキーに入力文字列が存在するかで出力内容を変える
"""
n = int(input())
count = {}

for i in range(n):
  s = input()
  if s in count:
    print(s + '(' + str(count[s]) + ')')
    count[s] += 1
  else:
    print(s)
    count[s] = 1
