from collections import deque
import sys


def choose_virus(virus_counts, now_index, virus_list):

    global min_time

    if virus_counts == M:
        infection_time = bfs_infection(virus_list)  # 바이러스 확산해서 얼마나 걸리는지 추출
        if min_time >= infection_time:
            min_time = infection_time

    else:
        # 조합... 지겹다
        for idx in range(now_index, len(virus_location)):
            virus_list.append(virus_location[idx])  # 바이러스 위치 하나 선택
            choose_virus(virus_counts+1, idx+1, virus_list)
            virus_list.pop()  # 사용한 위치 제거


def bfs_infection(virus_list):

    visited = [[2501]*N for _ in range(N)]  # 기본값을 최대 시간을 설정

    que = deque()

    # 바이러스 위치 고른데로 바이러스 놓고 확산 시작
    for virus in virus_list:
        (ni, nj) = virus
        visited[ni][nj] = 0
        que.append((ni, nj))

    while que:
        ni, nj = que.popleft()

        for k in range(4):
            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < N:
                if ARR[ni+di[k]][nj+dj[k]] == 0 and visited[ni+di[k]][nj+dj[k]] == 2501:
                    que.append((ni + di[k], nj + dj[k]))
                    visited[ni + di[k]][nj + dj[k]] = visited[ni][nj] + 1

                # 연구소2와 다른점 1
                # 비활성화 상태인 (바이러스 자리이지만 바이러스는 아닌) 바이러스 활성화도 고려
                if ARR[ni+di[k]][nj+dj[k]] == 2 and (ni+di[k], nj+dj[k]) not in virus_list and visited[ni+di[k]][nj+dj[k]] == 2501:
                    que.append((ni + di[k], nj + dj[k]))
                    visited[ni + di[k]][nj + dj[k]] = visited[ni][nj] + 1

    max_time = 0

    for i in range(N):
        for j in range(N):
            # 연구소2와 다른점 2
            # 비활성화 바이러스는 시간 계산을 하지 않아도 된다.
            if ARR[i][j] != 1 and ARR[i][j] != 2 and visited[i][j] > max_time:
                max_time = visited[i][j]

    return max_time


N, M = map(int, sys.stdin.readline().split())
ARR = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

virus_location = deque()

min_time = 2501
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if ARR[i][j] == 2:  # 바이러스를 놓을 수 있는 자리면 저장
            virus_location.append((i, j))
            # 연구소2와 다른점 3
            # 아래처럼 바이러스가 남아있다고 판단할 필요가 있기에 초기화 X
            # ARR[i][j] = 0

choose_virus(0, 0, [])

if min_time == 2501:
    print(-1)
else:
    print(min_time)
