from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color, visited, board, N):
    q = deque()
    q.append((x, y))
    blocks = [(x, y)]
    rainbow_blocks = []

    visited[x][y] = True
    temp_visited = [[False]*N for _ in range(N)]
    temp_visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not temp_visited[nx][ny]:
                if board[nx][ny] == 0 or board[nx][ny] == color:
                    q.append((nx, ny))
                    temp_visited[nx][ny] = True
                    blocks.append((nx, ny))
                    if board[nx][ny] == 0:
                        rainbow_blocks.append((nx, ny))
                    else:
                        visited[nx][ny] = True
    return blocks, rainbow_blocks

# 가장 그룹 수가 많은 블럭 찾기
def find_large_block(board, N):
    visited = [[False]*N for _ in range(N)]
    best_group = []
    best_rainbow_count = -1
    best_standard_block = (-1, -1)

    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                group, rainbows = bfs(i, j, board[i][j], visited, board, N)
                if len(group) < 2:
                    continue
                rainbow_count = len(rainbows)
                standard_blocks = [b for b in group if board[b[0]][b[1]] > 0]
                standard = min(standard_blocks)  # 기준 블럭은 무지개 블럭이 아닌 블럭 중에서 행 -> 열이 가장 작은 것

                if len(group) > len(best_group):  # 그룹 수가 큰 것
                    best_group = group
                    best_rainbow_count = rainbow_count
                    best_standard_block = standard
                elif len(group) == len(best_group):  # 그룹 수가 같다면
                    if rainbow_count > best_rainbow_count:  # 무지개 블록 수가 가장 많은 그룹
                        best_group = group
                        best_rainbow_count = rainbow_count
                        best_standard_block = standard
                    elif rainbow_count == best_rainbow_count: # 기준 블럭의 행 -> 열이 가장 큰 것
                        if standard > best_standard_block:
                            best_group = group
                            best_standard_block = standard
    return best_group

# 중력 작용
def gravity(board, N):
    for j in range(N):
        for i in range(N - 2, -1, -1):
            if board[i][j] >= 0:
                r = i
                while r + 1 < N and board[r + 1][j] == -2:
                    board[r + 1][j] = board[r][j]
                    board[r][j] = -2
                    r += 1

# 반시계 방향으로 회전
def locate_clockwise(board, N):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N - j - 1][i] = board[i][j]
    return new_board

# 구현
def simulate(board, N):
    score = 0
    while True:
        group = find_large_block(board, N)
        if not group:
            break
        for x, y in group:
            board[x][y] = -2
        score += len(group) ** 2
        gravity(board, N)
        board = locate_clockwise(board, N)
        gravity(board, N)
    return score

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(simulate(board, N))