import sys

N = int(sys.stdin.readline())
LST = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# [가로 경우의 수, 세로 경우의 수, 대각선 경우의 수]
# 가로 경우의 수 = 전 칸이 (가로일 때의 경우의 수 + 대각선일 때의 경우의 수)
# 세로 경우의 수 = 전 칸이 (세로일 때의 경우의 수 + 대각선일 때의 경우의 수)
# 대각선 경우의 수 = 전 칸이 (가로일 때의 경우의 수 + 세로일 때의 경우의 수 + 대각선일 때의 경우의 수)

DP = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
# DP = [[0, 0, 0] * N for _ in range(N)]  # 어줍잖게 만드니깐 얕은 복사됨 주의!!!!

# 첫 파이프 표시
DP[0][1][0] = 1

# j = 0이면 파이프가 절대 올 수 없다.

# i = 0, j = 2 ~ N-1 (첫 파이프는 표시했으니깐)
for q in range(2, N):
    if LST[0][q] == 0:
        DP[0][q][0] = DP[0][q - 1][0]

for i in range(1, N):  # i = 0 은 다 처리함
    for j in range(1, N):  # j = 0 은 다 처리함

        if LST[i][j] == 0:  # 현재 위치가 벽이 아닐 때
            # 가로 파이프의 경우의 수
            DP[i][j][0] = DP[i][j - 1][0] + DP[i][j - 1][2]  # 전 칸(왼쪽 칸)이 가로일 때의 경우의 수 + 대각선일 때의 경우의 수

            # 세로 파이프의 경우의 수
            DP[i][j][1] = DP[i - 1][j][1] + DP[i - 1][j][2]  # 전 칸(위 칸)이 세로일 때의 경우의 수 + 대각선일 때의 경우의 수

        # 대각선
        if LST[i][j] == 0 and LST[i - 1][j] == 0 and LST[i][j - 1] == 0:  # 현재 위치, 현재 위치의 위, 현재 위치의 왼쪽이 벽이 아닐 때
            # 전 칸(대각선 왼쪽 위 칸)이 가로일 때의 경우의 수 + 세로일 떄의 경우의 수 + 대각선일 때의 경우의 수
            DP[i][j][2] = DP[i - 1][j - 1][0] + DP[i - 1][j - 1][1] + DP[i - 1][j - 1][2]

print(sum(DP[N - 1][N - 1]))

"""
def check_pipe_horizontal(i, j, pipe):
    if i != N - 1 and j >= N - 2:
        return False
    if pipe == 2 or LST[i][j+1] == 1:
        return False
    return True


def check_pipe_vertical(i, j, pipe):
    if j != N - 1 and i >= N - 2:
        return False
    if pipe == 1 or LST[i + 1][j] == 1:
        return False
    return True


def check_pipe_diogonal(i, j, pipe):
    if i >= N - 1 or j >= N - 1:
        return False
    if LST[i + 1][j] == 1 or LST[i][j + 1] == 1 or LST [i + 1][j + 1] == 1:
        return False
    return True


def find_pipe_route(i, j, pipe):

    global way_counts

    if i == N-1 and j == N-1:
        way_counts += 1
        return
    else:
        if check_pipe_horizontal(i, j, pipe):
            find_pipe_route(i, j + 1, 1)

        if check_pipe_vertical(i, j, pipe):
            find_pipe_route(i + 1,  j, 2)

        if check_pipe_diogonal(i, j, pipe):
            find_pipe_route(i + 1, j + 1, 3)


N = int(sys.stdin.readline())
LST = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# pipe = {1 : 가로, 2 : 세로, 3 : 대각선}

way_counts = 0

find_pipe_route(0, 1, 1)

print(way_counts)
"""