import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def logs_coordinate(x, y, dirc):
    if dirc == 0:  # 가로
        return [(x, y - 1), (x, y), (x, y + 1)]
    else:  # 세로
        return [(x - 1, y), (x, y), (x + 1, y)]

def three_x_three_no_one(board, three_x_three):
    n = len(board)
    for (x, y) in three_x_three:
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        if board[x][y] == '1':
            return False
    return True

def can_rotate(board, x, y):
    n = len(board)
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i < 0 or i >= n or j < 0 or j >= n:
                return False
            if board[i][j] == '1':
                return False
    return True

# 통나무 가운데 좌표와 방향
def log_middle_coordinate_and_direction(points):
    points.sort()
    if points[0][0] == points[1][0] == points[2][0]:
        dirc = 0  # 가로
        cx, cy = points[1][0], points[1][1]
    else:
        dirc = 1  # 세로
        points.sort(key=lambda p: (p[0], p[1]))
        cx, cy = points[1][0], points[1][1]
    return cx, cy, dirc

# 입력 처리
n = int(input().strip())
board = [list(input().strip()) for _ in range(n)]

bs, es = [], []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'B':
            bs.append((i, j))
        elif board[i][j] == 'E':
            es.append((i, j))

start_x, start_y, start_dir = log_middle_coordinate_and_direction(bs)
end_x, end_y, end_dir = log_middle_coordinate_and_direction(es)

# B와 E를 0으로 취급
for x, y in bs + es:
    board[x][y] = '0'

# 3차원 배열로 x, y, 방향을 표시
visited = [[[False] * 2 for _ in range(n)] for __ in range(n)]
visited[start_x][start_y][start_dir] = True

Q = deque()
Q.append((start_x, start_y, start_dir, 0))

ans = 0
found = False

while Q:
    x, y, dirc, dist = Q.popleft()

    if x == end_x and y == end_y and dirc == end_dir:
        ans = dist
        found = True
        break

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        next_cells = logs_coordinate(nx, ny, dirc)
        if three_x_three_no_one(board, next_cells) and not visited[nx][ny][dirc]:
            visited[nx][ny][dirc] = True
            Q.append((nx, ny, dirc, dist + 1))

    ndir = 1 - dirc
    if can_rotate(board, x, y) and not visited[x][y][ndir]:
        visited[x][y][ndir] = True
        Q.append((x, y, ndir, dist + 1))

print(ans if found else 0)
