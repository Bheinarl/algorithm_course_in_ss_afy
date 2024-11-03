import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
DIRECTION = {1:(0, -1), 2:(-1, -1), 3:(-1, 0), 4:(-1, 1), 5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}
LST = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 위에서 1 빼서 N + 1

CLOUD = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}  # 시간 줄이려고 set 도 써봅니다.. list 가 문제인 거 같아요 (정답)

for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    s %= N  # 계산을 미리 해버려서 시간을 줄입시다
    d_i, d_j = DIRECTION[d]

    MOVING_CLOUD = set()  # 움직인 구름 생성 및 이전 데이터 초기화
    for cloud_i, cloud_j in CLOUD:
        cloud_i, cloud_j = (cloud_i + d_i * s) % N, (cloud_j + d_j * s) % N
        LST[cloud_i][cloud_j] += 1
        MOVING_CLOUD.add((cloud_i, cloud_j))

    TEMP_LST = [[0] * N for _ in range(N)]
    CLOUD = set()  # 구름 다 움직여주었으니 초기화

    for i in range(N):
        for j in range(N):
            TEMP_LST[i][j] = LST[i][j]  # TEMP_LST를 사용하지 않으면 순차적으로 흘러가서 물이 생겨서 추가될 듯하여 사용
            if (i, j) in MOVING_CLOUD:  # 구름이면 대각선을 다 확인
                if 0 <= i - 1 < N and 0 <= j - 1 < N and LST[i - 1][j - 1] != 0:  # ↖
                    TEMP_LST[i][j] += 1
                if 0 <= i - 1 < N and 0 <= j + 1 < N and LST[i - 1][j + 1] != 0:  # ↗
                    TEMP_LST[i][j] += 1
                if 0 <= i + 1 < N and 0 <= j - 1 < N and LST[i + 1][j - 1] != 0:  # ↙
                    TEMP_LST[i][j] += 1
                if 0 <= i + 1 < N and 0 <= j + 1 < N and LST[i + 1][j + 1] != 0:  # ↘
                    TEMP_LST[i][j] += 1
            else:  # 구름이 없는 곳에서는 물이 2 이상인지 확인 후, 2 이상이면 새로운 구름이 만들어진다.
                if TEMP_LST[i][j] >= 2:
                    CLOUD.add((i, j))
                    TEMP_LST[i][j] -= 2

    LST = TEMP_LST

sum_water = 0
for lst_LST in LST:
    sum_water += sum(lst_LST)
print(sum_water)
