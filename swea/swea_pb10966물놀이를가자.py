from collections import deque


def bfs():

    while queue:
        (ni, nj) = queue.popleft()

        for k in range(4):
            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < M and visited[ni+di[k]][nj+dj[k]] == -1:

                queue.append((ni+di[k], nj+dj[k]))
                visited[ni+di[k]][nj+dj[k]] = visited[ni][nj] + 1


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]
    land = []

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    queue = deque()
    visited = [[-1] * M for _ in range(N)]

    for p in range(N):
        for q in range(M):
            if ARR[p][q] == 'W':
                queue.append((p, q))
                visited[p][q] = 0

    bfs()

    RESULT = 0
    for i in range(N):
        for j in range(M):
            RESULT += visited[i][j]

    print(f'#{TEST_CASE} {RESULT}')
