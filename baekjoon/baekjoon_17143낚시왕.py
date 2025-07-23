def move_shark():
    temp_grid = [[0 for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if grid[x][y]:
                s, d, z = grid[x][y]
                dir_idx = d - 1
                nx, ny = x, y
                for _ in range(s):
                    nx += dx[dir_idx]
                    ny += dy[dir_idx]
                    if not (0 <= nx < R and 0 <= ny < C):
                        # 방향 반대로 변경
                        if dir_idx == 0:
                            dir_idx = 1
                        elif dir_idx == 1:
                            dir_idx = 0
                        elif dir_idx == 2:
                            dir_idx = 3
                        elif dir_idx == 3:
                            dir_idx = 2
                        # 한 칸 반대 방향으로 다시 이동
                        nx += dx[dir_idx] * 2
                        ny += dy[dir_idx] * 2
                # 이동이 끝나면 맵 갱신
                new_d = dir_idx + 1  # 다시 d 값으로
                if temp_grid[nx][ny] == 0 or temp_grid[nx][ny][2] < z:
                    temp_grid[nx][ny] = [s, new_d, z]
    return temp_grid


R, C, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


grid = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    if d in [1, 2]:
        s %= (R - 1) * 2
    else:
        s %= (C - 1) * 2
    grid[r][c] = [s, d, z]

answer = 0

for fish_king_x in range(C):
    for fish_king_y in range(R):
        if grid[fish_king_y][fish_king_x]:
            answer += grid[fish_king_y][fish_king_x][2]
            grid[fish_king_y][fish_king_x] = 0
            break
    grid = move_shark()

print(answer)