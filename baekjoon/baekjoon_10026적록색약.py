from collections import deque

def normal(i, j):

    now_color = LST[i][j]

    Qn = deque()
    Qn.append((i, j))
    visited_nor[i][j] = 1

    while Qn:
        ni, nj = Qn.popleft()

        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= ni + di < N and 0 <= nj + dj < N and visited_nor[ni + di][nj + dj] == 0:
                if LST[ni + di][nj + dj] == now_color:
                    Qn.append((ni + di, nj + dj))
                    visited_nor[ni + di][nj + dj] = 1

def color_weakness(i, j):

    if LST[i][j] in 'RG':  # 적록색약 색 구별
        now_color = 'RG'
    else:
        now_color = 'B'

    Qc = deque()
    Qc.append((i, j))
    visited_col[i][j] = 1

    while Qc:
        ni, nj = Qc.popleft()

        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= ni + di < N and 0 <= nj + dj < N and visited_col[ni + di][nj + dj] == 0:
                if LST[ni + di][nj + dj] in now_color:
                    Qc.append((ni + di, nj + dj))
                    visited_col[ni + di][nj + dj] = 1

N = int(input())

LST = [list(input().rstrip()) for _ in range(N)]

visited_nor = [[0] * N for _ in range(N)]
visited_col = [[0] * N for _ in range(N)]

count_area_nor = 0
count_area_col = 0

for i in range(N):
    for j in range(N):
        if visited_nor[i][j] == 0:
            normal(i, j)
            count_area_nor += 1

        if visited_col[i][j] == 0:
            color_weakness(i, j)
            count_area_col += 1

print(f'{count_area_nor} {count_area_col}')