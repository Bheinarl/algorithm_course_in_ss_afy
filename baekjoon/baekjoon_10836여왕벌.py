import sys
input = sys.stdin.readline

M, N = map(int, input().split())
len_growth = 2 * M - 1
diff = [0] * (len_growth + 1)

col_1st = [1] * M  # 아래에서 위로
row_1st = [1] * M  # 왼쪽에서 오른쪽으로
# 첫 원소는 col_1st 마지막 원소와 중복됨
# col_1st[-1] = row_1st[0]

for _ in range(N):
    growth_0, growth_1, growth_2 = map(int, input().split())
    boundary_01 = growth_0
    boundary_12 = growth_0 + growth_1

    diff[boundary_01] += 1
    if boundary_12 < len_growth:
        diff[boundary_12] += 1

growths = [0] * len_growth
cur = 0
for i in range(len_growth):
    cur += diff[i]
    growths[i] = cur

for p in range(M):
    col_1st[M - 1 - p] += growths[p]

for q in range(1, M):
    row_1st[q] += growths[M - 1 + q]

if M == 1:
    print(col_1st[0])
else:
    for i in range(M):
        row = []
        for j in range(M):
            if j == 0:
                row.append(col_1st[i])
            else:
                row.append(max(col_1st[i], row_1st[j]))
        print(*row)