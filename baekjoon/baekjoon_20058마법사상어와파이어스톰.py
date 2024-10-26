from collections import deque
import sys

def rotate_ice_clockwise(arr, l):
    temp_list = [[0] * N for _ in range(N)]
    L = 2 ** l
    for i in range(0, N, L):  # 0부터 N까지 L만큼 띄엄띄엄 단계 별 조각난? 얼음 돌리기
        for j in range(0, N, L):  # 0부터 N까지 L만큼 띄엄띄엄 단계 별 조각난? 얼음 돌리기
            for p in range(L):  # 그 나뉘어진 얼음에서
                for q in range(L):  # 그 나뉘어진 얼음에서
                    temp_list[i + p][j + q] = arr[i + (L - q - 1)][j + p]  # 시계 방향 회전
                #   temp_arr[i + p][j + q] = arr[i + q][j + (L - p - 1)]  # 반시계 방향 회전
    return temp_list


def melt_ice(NOW_ICE):
    # temp_list = deepcopy(NOW_ICE)  이렇게 하니깐 한 번에 바뀌는게 아니라 순서대로 바뀌는 거라서 뒤 얼음에 영향을 줌
    temp_list = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ice_counts = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and NOW_ICE[ni][nj] > 0:
                    ice_counts += 1
            if ice_counts < 3:
                temp_list[i][j] = NOW_ICE[i][j] - 1
            else:
                temp_list[i][j] = NOW_ICE[i][j]

    return temp_list


def find_big_ice(i, j):

    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    big_ice_count = 1

    while que:

        i, j = que.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and NOW_ICE[ni][nj] > 0:
                visited[ni][nj] = 1
                que.append((ni, nj))
                big_ice_count += 1

    return big_ice_count


n, Q = map(int, sys.stdin.readline().split())  # Q는 L_lst 의 원소 개수
N = 2 ** n
NOW_ICE = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
L_list = list(map(int, sys.stdin.readline().split()))

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for L in range(Q):
    NOW_ICE = rotate_ice_clockwise(NOW_ICE, L_list[L])  # 시계방향으로 돌리고
    NOW_ICE = melt_ice(NOW_ICE)

ice_sum = 0
max_big_ice = 0
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if NOW_ICE[i][j] > 0:
            ice_sum += NOW_ICE[i][j]  # 조건 안넣으니깐 음수도 다 더해짐
            max_big_ice = max(max_big_ice, find_big_ice(i, j))  # 조건 안넣으니깐 첫 que 에 0인데도 들어감

print(ice_sum)
print(max_big_ice)
