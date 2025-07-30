from copy import deepcopy

def move_fishes(board, fishes, shark_x, shark_y):
    for i in range(1, 17):
        if fishes[i][0] == -1:
            continue

        x, y, dirct = fishes[i]
        for _ in range(8):
            nx, ny = x + dx[dirct], y + dy[dirct]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == shark_x and ny == shark_y):
                if board[nx][ny] != 0:
                    other = board[nx][ny]
                    fishes[other][0], fishes[other][1] = x, y

                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                fishes[i] = [nx, ny, dirct]
                break
            dirct = (dirct + 1) % 8

        fishes[i][2] = dirct


def dfs(board, fishes, shark_x, shark_y, shark_dirct, total):
    global result
    board = deepcopy(board)
    fishes = deepcopy(fishes)

    move_fishes(board, fishes, shark_x, shark_y)

    can_move = False

    for step in range(1, 4):
        nx = shark_x + dx[shark_dirct] * step
        ny = shark_y + dy[shark_dirct] * step

        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != 0:
            can_move = True
            fish_num = board[nx][ny]
            nd = fishes[fish_num][2]

            board[nx][ny] = 0
            prev_fish = fishes[fish_num][:]
            fishes[fish_num] = [-1, -1, -1]

            dfs(board, fishes, nx, ny, nd, total + fish_num)

            board[nx][ny] = fish_num
            fishes[fish_num] = prev_fish

    if not can_move:
        result = max(result, total)


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

board = [[0]*4 for _ in range(4)]
fishes = dict()

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        num, d = data[2*j], data[2*j+1]-1
        board[i][j] = num
        fishes[num] = [i, j, d]

start = board[0][0]
sx, sy = 0, 0
sd = fishes[start][2]
board[0][0] = 0
fishes[start] = [-1, -1, -1]

result = 0
dfs(board, fishes, sx, sy, sd, start)
print(result)
