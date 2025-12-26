import sys
input = sys.stdin.readline

def rotate_sticker(sticker):
    r, c = len(sticker), len(sticker[0])
    new = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new[j][r-1-i] = sticker[i][j]
    return new

def is_able_to_attach(board, sticker, x, y):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1 and board[x+i][y+j] == 1:
                return False
    return True

def attach_sticker(board, sticker, x, y):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                board[x+i][y+j] = 1

def calc_answer(board):
    ans = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                ans += 1
    return ans

N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]

    attached = False
    for _ in range(4):
        sr, sc = len(sticker), len(sticker[0])
        for i in range(N - sr + 1):
            for j in range(M - sc + 1):
                if is_able_to_attach(board, sticker, i, j):
                    attach_sticker(board, sticker, i, j)
                    attached = True
                    break
            if attached:
                break
        if attached:
            break
        sticker = rotate_sticker(sticker)

print(calc_answer(board))