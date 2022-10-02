# B - Triangle (Easier) 
# https://atcoder.jp/contests/abc262/tasks/abc262_b
N, M = map(int, input().split())
UV = [[False for _ in range(N)] for _ in range(N)]
# NOTE: どこに辺があるのか
for i in range(M):
  u, v = map(int, input().split())
  UV[u - 1][v - 1] = True
  UV[v - 1][u - 1] = True

ans = 0
for i in range(N):
  for j in range(i, N):
    for k in range(j, N):
      # NOTE: 辺が存在していればオッケー
      if UV[i][j] and UV[j][k] and UV[i][k]:
        ans += 1

print(ans)
