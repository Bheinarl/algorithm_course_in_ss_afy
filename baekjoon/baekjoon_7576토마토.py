from collections import deque

M, N = map(int, input().split())
TOMATO = [list(map(int, input().split())) for _ in range(N)]
q = deque()
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if TOMATO[i][j] == 1:
            q.append((i,j))
            visited[i][j] = 1
        elif TOMATO[i][j] == -1:
            visited[i][j] = -1

while q:
    (ni, nj) = q.popleft()

    for k in range(4):
        if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < M and visited[ni+di[k]][nj+dj[k]] == 0:
            q.append((ni+di[k], nj+dj[k]))
            visited[ni+di[k]][nj+dj[k]] = visited[ni][nj] + 1

max_day = 0
for y in range(N):
    temp = max(visited[y])-1
    max_day = max(temp, max_day)
for x in range(N):
    if 0 not in visited[x]:
        TF = 1
    else:
        TF = 0
        max_day = -1
        break
print(max_day)