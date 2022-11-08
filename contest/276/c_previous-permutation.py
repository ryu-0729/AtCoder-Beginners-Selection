# C - Previous Permutation
# https://atcoder.jp/contests/abc276/tasks/abc276_c
# NOTE: 解説動画と参考記事を見て実装
# https://qiita.com/MoroeTachibana-oh/items/7083f8bd2634d70846da

n = int(input())
p = list(map(int, input().split()))

# NOTE: 順番を変更する場所を特定する
i = n - 2
while p[i] < p[i + 1]: i -= 1

# NOTE: 変更する場所までで後ろからみた時に最初にくる小さい値を探す
j = n - 1
while p[i] < p[j]: j -= 1

# NOTE: 値の入れ替え
p[i], p[j] = p[j], p[i]
# NOTE: 変更する箇所の反転処理
ans = p[:i+1] + p[i+1:][::-1]
for x in ans:
  print(x, end=' ')
