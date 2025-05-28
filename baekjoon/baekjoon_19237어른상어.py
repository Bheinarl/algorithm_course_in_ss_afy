N, M, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

priority = [[[] for _ in range(4)] for _ in range(M + 1)]

for i in range(1, M + 1):
    for d in range(4):
        priority[i][d] = list(map(lambda x: int(x)-1, input().split()))

# 상어 위치, 방향 저장
sharks = dict()  # key: 상어번호, value: [x, y, direction]
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            shark_num = grid[i][j]
            sharks[shark_num] = [i, j, directions[shark_num - 1] - 1]

# 냄새 지도: [남은시간, 상어번호]
smell_grid = [[[0, 0] for _ in range(N)] for _ in range(N)]

def spread_smell():
    for i in range(N):
        for j in range(N):
            if smell_grid[i][j][0] > 0:
                smell_grid[i][j][0] -= 1
                if smell_grid[i][j][0] == 0:
                    smell_grid[i][j][1] = 0
    for num, (x, y, _) in sharks.items():
        smell_grid[x][y] = [K, num]

def move_sharks():
    candidates = dict()  # (x, y): [(shark_num, direction)]

    for num, (x, y, d) in sorted(sharks.items()):
        moved = False

        # 냄새 없는 칸 우선
        for nd in priority[num][d]:
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < N and 0 <= ny < N and smell_grid[nx][ny][0] == 0:
                candidates.setdefault((nx, ny), []).append((num, nd))
                moved = True
                break

        if not moved:
            for nd in priority[num][d]:
                nx, ny = x + dx[nd], y + dy[nd]
                if 0 <= nx < N and 0 <= ny < N and smell_grid[nx][ny][1] == num:
                    candidates.setdefault((nx, ny), []).append((num, nd))
                    break

    new_sharks = dict()
    for (x, y), shark_list in candidates.items():
        shark_list.sort()  # 번호 가장 작은 상어가 생존
        num, nd = shark_list[0]
        new_sharks[num] = [x, y, nd]

    return new_sharks


time = 0
spread_smell()  # 최초 냄새

while time < 1000:
    time += 1
    sharks = move_sharks()  # 이동 + 충돌 처리
    spread_smell()          # 살아남은 상어만 냄새 뿌림

    if len(sharks) == 1 and 1 in sharks:
        print(time)
        break
else:
    print(-1)