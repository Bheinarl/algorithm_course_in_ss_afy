import sys
input = sys.stdin.readline

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

def roll_dice(dice, direction):
    top, bottom, north, south, west, east = dice

    if direction == 1:  # 동
        dice[0] = west
        dice[1] = east
        dice[2] = north
        dice[3] = south
        dice[4] = bottom
        dice[5] = top
    elif direction == 2:  # 서
        dice[0] = east
        dice[1] = west
        dice[2] = north
        dice[3] = south
        dice[4] = top
        dice[5] = bottom
    elif direction == 3:  # 북
        dice[0] = south
        dice[1] = north
        dice[2] = top
        dice[3] = bottom
        dice[4] = west
        dice[5] = east
    elif direction == 4:  # 남
        dice[0] = north
        dice[1] = south
        dice[2] = bottom
        dice[3] = top
        dice[4] = west
        dice[5] = east

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move_directions = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

i, j = x, y

for md in move_directions:
    ni = i + di[md]
    nj = j + dj[md]

    if not (0 <= ni < N and 0 <= nj < M):
        continue

    i, j = ni, nj

    roll_dice(dice, md)

    if board[i][j] == 0:
        board[i][j] = dice[1]  # 바닥 -> 칸
    else:
        dice[1] = board[i][j]  # 칸 -> 바닥
        board[i][j] = 0

    print(dice[0])