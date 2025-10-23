import sys
input = sys.stdin.readline

# 방향: 1=오른쪽, 2=왼쪽, 3=위, 4=아래
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def in_range(n, x, y):
    return 0 <= x < n and 0 <= y < n

# 방향 전환
def reverse_directions(d):
    if d == 1 or d == 2:
        return 3 - d
    else:
        return 7 - d

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]

grid = [[[] for _ in range(N)] for _ in range(N)]  # 그 칸에 쌓인 말 번호 리스트
pieces = [[0, 0, 0] for _ in range(K)]  # x좌표, y좌표, 방향 순서

for i in range(K):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    pieces[i] = [r, c, d]
    grid[r][c].append(i)

turn = 0
answer = -1

while turn <= 1000:
    turn += 1

    for i in range(K):  # 말 번호 순회
        x, y, d = pieces[i]
        stack = grid[x][y]

        if stack[0] != i:
            continue

        nx, ny = x + dx[d], y + dy[d]

        # 파란색 칸이거나 범위 밖이면 방향 뒤집은 후 한 번 더 시도
        if not in_range(N, nx, ny) or color[nx][ny] == 2:
            d = reverse_directions(d)
            pieces[i][2] = d  # 방향만 갱신
            nx, ny = x + dx[d], y + dy[d]
            # 방향 전환 후 여전히 이동이 안되면 이동하지 않음
            if not in_range(N, nx, ny) or color[nx][ny] == 2:
                continue

        moving = stack[:]
        grid[x][y] = []

        if color[nx][ny] == 1:  # 빨간색이면 층수 반전
            moving.reverse()

        # 이동
        for piece_info in moving:
            pieces[piece_info][0] = nx
            pieces[piece_info][1] = ny
        grid[nx][ny].extend(moving)

        if len(grid[nx][ny]) >= 4:
            print(turn)
            sys.exit(0)

    if turn == 1000:
        break

print(-1)