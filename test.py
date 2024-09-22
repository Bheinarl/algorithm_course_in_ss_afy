from collections import deque


def choose_virus(virus_counts, now_index, virus_list):

    global min_time

    if virus_counts == M:
        infection_time = bfs_infection(virus_list)
        if min_time >= infection_time:
            min_time = infection_time

    else:
        for idx in range(now_index, len(virus_location)):
            virus_list.append(virus_location[idx])  # 바이러스 위치 하나 선택
            choose_virus(virus_counts+1, now_index+1, virus_list)
            virus_list.pop()  # 사용한 위치 제거


def bfs_infection(virus_list):

    visited = [[2501]*N for _ in range(N)]

    que = deque()

    for virus in virus_list:
        (ni, nj) = virus
        visited[ni][nj] = 0
        que.append((ni, nj))

    while que:
        ni, nj = que.popleft()

        for k in range(4):
            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < N and ARR[ni+di[k]][nj+dj[k]] == 0 and visited[ni+di[k]][nj+dj[k]] == 2501:
                que.append((ni + di[k], nj + dj[k]))
                visited[ni + di[k]][nj + dj[k]] = visited[ni][nj] + 1

    max_time = 0
    for i in range(N):
        for j in range(N):
            if ARR[i][j] != 1 and visited[i][j] > max_time:
                max_time = visited[i][j]

    return max_time


N, M = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]

virus_location = deque()

min_time = 2501
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if ARR[i][j] == 2:
            virus_location.append((i, j))
            ARR[i][j] = 0

choose_virus(0, 0, [])

if min_time == 2501:
    print(-1)
else:
    print(min_time)
