from collections import deque


def bfs(i, j):

    que = deque()
    visited = [[0] * N for _ in range(N)]
    fish_lst = []

    que.append((i, j))
    visited[i][j] = 1
    eat_size = 0

    while que:
        ni, nj = que.popleft()

        # 위에서 보면 visited[i][j] = 1이고 eat_size = 0 이렇게 계속 1 차이가 나야한다.
        # 근데 같아진 순간이 되면, 그 크기는 다 먹어서 숫자가 바뀐것.
        # 아래 조건문은 같은 크기의 물고기는 다 찾았다는 의미이다.
        if eat_size == visited[ni][nj]:
            return fish_lst, eat_size - 1 # 먹은 크기를 돌려줘야하니깐 -1

        for k in range(4):
            if 0 <= ni + di[k] < N and 0 <= nj + dj[k] < N:
                if size >= ARR[ni + di[k]][nj + dj[k]] and visited[ni + di[k]][nj + dj[k]] == 0:
                # 지나가는건 크기가 같아도 상관없지만
                    que.append((ni + di[k], nj + dj[k]))
                    visited[ni + di[k]][nj + dj[k]] = visited[ni][nj] + 1
                    if size > ARR[ni + di[k]][nj + dj[k]] > 0:  # 여기서부터 먹을 물고기인데 먹는거는 크기가 작아야함
                        fish_lst.append((ni + di[k], nj + dj[k]))
                        eat_size = visited[ni + di[k]][nj + dj[k]]  # 먹는 크기를 저장을 해

    return fish_lst, eat_size - 1  # 다 순회했는데 없네..


N = int(input())
size = 2
ARR = [list(map(int, input().split())) for _ in range(N)]
moving_counts = 0
fish_counts = 0
shark_i, shark_j = 0, 0
for i in range(N):
    for j in range(N):
        if ARR[i][j] == 9:
            shark_i, shark_j = i, j
            ARR[i][j] = 0

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

ni, nj = shark_i, shark_j

while True:
    fish_lst, distance = bfs(ni, nj)

    if len(fish_lst) == 0:  # 더이상 먹을 물고기가 없으면 끝!
        break

    fish_lst.sort(key=lambda x: (x[0], x[1]))  # 가장 가까운 물고기를 찾는데 가장 위쪽, 가장 왼쪽인 것으로
    ni, nj = fish_lst[0]  # 위 조건에 맞는 가까운 물고기로 이동
    ARR[ni][nj] = 0  # 물고기 먹었으니깐 0으로

    fish_counts += 1
    moving_counts += distance  # 거리만큼 움직여서 먹었으니깐

    if size == fish_counts:  # 상어가 먹은 물고기와 크기가 같다면
        size += 1
        fish_counts = 0

print(moving_counts)