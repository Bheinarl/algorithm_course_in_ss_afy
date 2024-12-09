from collections import deque

def bfs(i, j):

    Q = deque()
    Q.append((i, j))
    visited[i][j] = 1

    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and ICE[ni][nj] > 0 and not visited[ni][nj]:
                Q.append((ni, nj))
                visited[ni][nj] = 1


N, M = map(int, input().split())
ICE = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
years = 0

while True:
    years += 1

    melt_ice = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if ICE[i][j] > 0:
                count_sea = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni and 0 <= nj < M and ICE[ni][nj] == 0:
                        count_sea += 1
                melt_ice[i][j] = count_sea

    for i in range(N):
        for j in range(M):
            if ICE[i][j] > 0:
                ICE[i][j] = max(0, ICE[i][j] - melt_ice[i][j])

    visited = [[0] * M for _ in range(N)]

    island = 0

    for i in range(N):
        for j in range(M):
            if ICE[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                island += 1

    if island > 1:
        print(years)
        break
    elif island == 0:
        print(0)
        break