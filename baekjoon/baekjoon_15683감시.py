from copy import deepcopy

def check(i, j, dir, TEMP_check):
    while True:
        i += di[dir]
        j += dj[dir]

        if i < 0 or j < 0 or i >= N or j >= M:  # 범위를 벗어나면 종료
            return

        if TEMP_check[i][j] == 6:  # 벽이면 종료
            return

        if TEMP_check[i][j] > 0:  # CCTV가 있는 칸이면 그냥 넘어감
            continue

        TEMP_check[i][j] = -1  # 빈 칸이면 감시 영역 표시

def dfs(idx):
    global ans

    if idx == len(CCTV):  # 모든 CCTV 배치 완료
        counts = sum(row.count(0) for row in ROOM)  # 감시되지 않는 빈 칸 개수 계산
        ans = min(ans, counts)
        return

    i, j, cctv_type = CCTV[idx]
    backup_ROOM = deepcopy(ROOM)  # 현재 상태 저장

    for dir in range(4):  # 4가지 방향 탐색
        if cctv_type == 1:
            check(i, j, dir, ROOM)
        elif cctv_type == 2:
            check(i, j, dir, ROOM)
            check(i, j, (dir + 2) % 4, ROOM)  # 반대 방향 감시
        elif cctv_type == 3:
            check(i, j, dir, ROOM)
            check(i, j, (dir + 1) % 4, ROOM)  # 직각 방향 감시
        elif cctv_type == 4:
            check(i, j, dir, ROOM)
            check(i, j, (dir + 1) % 4, ROOM)
            check(i, j, (dir + 2) % 4, ROOM)  # 3방향 감시
        elif cctv_type == 5:
            check(i, j, 0, ROOM)
            check(i, j, 1, ROOM)
            check(i, j, 2, ROOM)
            check(i, j, 3, ROOM)  # 모든 방향 감시

        dfs(idx + 1)  # 다음 CCTV 처리
        ROOM[:] = deepcopy(backup_ROOM)  # 원상복구

N, M = map(int, input().split())
ROOM = [list(map(int, input().split())) for _ in range(N)]
CCTV = []

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if 1 <= ROOM[i][j] <= 5:
            CCTV.append((i, j, ROOM[i][j]))  # (행, 열, CCTV 종류)

ans = N * M  # 최대한 큰 값으로 설정
dfs(0)
print(ans)
