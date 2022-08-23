l1, r1, l2, r2 = map(int, input().split())

# 共通区間を求める公式
answer = max(0, min(r1, r2) - max(l1, l2))
print(answer)
