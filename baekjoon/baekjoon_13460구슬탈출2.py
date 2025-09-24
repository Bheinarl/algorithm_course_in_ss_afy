import sys
from collections import deque
input = sys.stdin.readline

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def roll(board, x, y, dx, dy):

    moved = 0
    while True:
        nx, ny = x + dx, y + dy
        cell = board[nx][ny]
        if cell == '#':
            break
        x, y = nx, ny
        moved += 1
        if cell == 'O':
            return x, y, moved, True
    return x, y, moved, False


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

rx = -1
ry = -1
bx = -1
by = -1
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'  # 빈칸 처리
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'


visited = [[[[False]*M for _ in range(N)] for __ in range(M)] for ___ in range(N)]
visited[rx][ry][bx][by] = True

q = deque()
q.append((rx, ry, bx, by, 0))  # 마지막은 기울인 횟수

while q:
    crx, cry, cbx, cby, depth = q.popleft()
    if depth >= 10:
        continue

    for dx, dy in dir:
        # 각 방향으로 빨강, 파랑 굴리기
        nrx, nry, red_move, red_fell = roll(board, crx, cry, dx, dy)
        nbx, nby, blue_move, blue_fell = roll(board, cbx, cby, dx, dy)

        # 파랑이 구멍에 빠지면 이 경로는 x
        if blue_fell:
            continue

        # 빨강만 빠지면 o
        if red_fell:
            print(depth + 1)
            sys.exit()

        # 같은 칸에 멈췄다면(구멍 아님) 겹침 해결
        if nrx == nbx and nry == nby:
            # 더 멀리 움직인 구슬을 한 칸 뒤로
            if red_move > blue_move:
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy

        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            q.append((nrx, nry, nbx, nby, depth + 1))

# 불가능하면
print(-1)