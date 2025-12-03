import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

viruses = []

for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            viruses.append((grid[i][j], 0, i, j))

viruses.sort()

q = deque(viruses)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while q:
    virus, time, i, j = q.popleft()

    if time == S:
        break

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 0:
            grid[ni][nj] = virus
            q.append((virus, time + 1, ni, nj))

print(grid[X - 1][Y - 1])