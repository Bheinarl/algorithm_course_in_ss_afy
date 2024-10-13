from collections import deque


def check_pop(si, sj):  # bfs

    que = deque()
    que.append((si, sj))
    visited[si][sj] = 1
    union_list = [(si, sj)]
    sum_pop = ARR[si][sj]

    while que:
        ni, nj = que.popleft()

        for k in range(4):
            if 0 <= ni + di[k] < N and 0 <= nj + dj[k] < N:  # 범위 안에 있어야하고
                if visited[ni + di[k]][nj + dj[k]] == 0 and L <= abs(ARR[ni + di[k]][nj + dj[k]] - ARR[ni][nj]) <= R:
                    # 방문한적 없어야하고 (방문했으면 연합인지 이미 확인 했으니깐) 문제에서 준 인구 차이 범위안에 있어야하고
                    que.append((ni + di[k], nj + dj[k]))
                    visited[ni + di[k]][nj + dj[k]] = 1
                    union_list.append((ni + di[k], nj + dj[k]))
                    sum_pop += ARR[ni + di[k]][nj + dj[k]]

    if len(union_list) > 1:  # 연합 국가가 1개 이상이여야 의미가 있지
        for union_i, union_j in union_list:
            ARR[union_i][union_j] = sum_pop // len(union_list)  # 인구 이동
        return 1  # 연합이 있었다를 반환
    else:
        return 0  # 연합이 없었다를 반환


N, L, R = map(int, input().split())

ARR = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

day = 0

while True:

    visited = [[0]*N for _ in range(N)]
    union_TF = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:  # 한 번도 확인하지 않은 곳이라면
                union_TF = max(union_TF, check_pop(i, j))  # 확인을 해봐봐

    if union_TF == 0:  # 연합이 없으면 더 이상 할 필요가 없어요
        break
    day += 1  # 연합이 더 존재하면 하루 추가

print(day)
