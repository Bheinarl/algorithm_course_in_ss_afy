N, M, P = map(int, input().split())
S = list(map(int, input().split()))
BOARD = [list(input()) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if BOARD[i][j] == '.':
            BOARD[i][j] = 0
        elif BOARD[i][j] == '#':
            BOARD[i][j] = -1
        else:
            BOARD[i][j] = int(BOARD[i][j])
