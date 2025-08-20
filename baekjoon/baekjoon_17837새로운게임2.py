def move_piece(i):
    r, c, d = chess_pieces[i]
    stack = chess_piece_order[r][c]

    idx = stack.index(i)
    moving = stack[idx:]
    chess_piece_order[r][c] = stack[:idx]

    nr, nc = r + dr[d], c + dc[d]

    if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
        d = flip[d]
        chess_pieces[i][2] = d
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
            chess_piece_order[r][c].extend(moving)
            return len(chess_piece_order[r][c]) >= 4

    if board[nr][nc] == 1:
        moving.reverse()

    for p in moving:
        chess_pieces[p][0], chess_pieces[p][1] = nr, nc
        chess_piece_order[nr][nc].append(p)

    return len(chess_piece_order[nr][nc]) >= 4


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

chess_pieces = []
conv = {1:0, 2:1, 3:2, 4:3}  # 입력 -> 내부 방향 인덱스로 변환
for _ in range(K):
    r, c, d = map(int, input().split())
    chess_pieces.append([r-1, c-1, conv[d]])

chess_piece_order = [[[] for _ in range(N)] for __ in range(N)]
for i, (r, c, _) in enumerate(chess_pieces):
    chess_piece_order[r][c].append(i)

# 상우하좌
dr = [0,  0, -1, 1]
dc = [1, -1,  0, 0]
flip = {0:1, 1:0, 2:3, 3:2}

turn = 0
done = False
while turn <= 1000 and not done:
    turn += 1
    for i in range(K):
        if move_piece(i):
            print(turn)
            done = True
            break
    if turn == 1000:
        break

if not done:
    print(-1)