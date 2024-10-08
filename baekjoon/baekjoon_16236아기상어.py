from collections import deque

N = int(input())
size = 2
ARR = [list(map(int, input().split())) for _ in range(N)]

fish_counts = 0
for i in range(N):
    for j in range(N):
        if ARR[i][j] == 9:
            shark_i, shark_j = i, j
        elif ARR[i][j] != 0:
            fish_counts += 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

que = deque()
que.append((shark_i, shark_j))

while que:
    ni, nj = que.popleft()

    visited = [[0] * N for _ in range(N)]
    visited[ni][nj] = 1

    pass