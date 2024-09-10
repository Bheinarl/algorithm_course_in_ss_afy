from collections import deque

M, N, H = map(int, input().split())
TOMATO = [list(map(int, input().split())) for _ in range(N*H)]
q = deque()
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
visited = [[0] * M for _ in range(N*H)]

for i in range(N*H):
    for j in range(M):
        if TOMATO[i][j] == 1:
            q.append((i,j))
            visited[i][j] = 1
        elif TOMATO[i][j] == -1:
            visited[i][j] = -1

while q:
    (ni, nj) = q.popleft()
    floor = ni // N
    for k in range(4):
        if N*floor <= ni+di[k] <= N*floor+(N-1) and 0 <= nj+dj[k] < M and visited[ni+di[k]][nj+dj[k]] == 0:
            q.append((ni+di[k], nj+dj[k]))
            visited[ni+di[k]][nj+dj[k]] = visited[ni][nj] + 1

    if ni+N < N*H and visited[ni+N][nj] == 0:
        q.append((ni+N, nj))
        visited[ni + N][nj] = visited[ni][nj] + 1

    if 0 <= ni-N and visited[ni-N][nj] == 0:
        q.append((ni-N, nj))
        visited[ni - N][nj] = visited[ni][nj] + 1

max_day = 0

for y in range(N*H):
    temp = max(visited[y]) - 1
    max_day = max(temp, max_day)

for x in range(N*H):
    if 0 in visited[x]:
        max_day = -1
        break
print(max_day)
