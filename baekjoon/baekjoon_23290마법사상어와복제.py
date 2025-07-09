import copy

fish_dx = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dy = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

M, S = map(int, input().split())
fish_map = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0]*4 for _ in range(4)]

for _ in range(M):
    fish_x, fish_y, d = map(int, input().split())
    fish_map[fish_x-1][fish_y-1].append(d-1)

sx, sy = map(int, input().split())
shark = (sx-1, sy-1)

def dfs_shark(x, y, depth, route, eat, visited_set, fish_map):  # 재귀 형태의 dfs
    global max_eat, best_route
    if depth == 3:
        if eat > max_eat:
            max_eat = eat
            best_route = route[:]
        elif eat == max_eat:
            best_route = min(best_route, route)  # 사전 순 정렬
        return

    for dir in range(4):
        nx, ny = x + shark_dx[dir], y + shark_dy[dir]
        if 0 <= nx < 4 and 0 <= ny < 4:
            added = 0
            if (nx, ny) not in visited_set:
                added = len(fish_map[nx][ny])
                visited_set.add((nx, ny))
                dfs_shark(nx, ny, depth+1, route+[dir], eat+added, visited_set, fish_map)
                visited_set.remove((nx, ny))
            else:
                dfs_shark(nx, ny, depth+1, route+[dir], eat, visited_set, fish_map)

def move_fish():
    new_map = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in fish_map[x][y]:
                moved = False
                for i in range(8):
                    nd = (d - i) % 8
                    nx, ny = x + fish_dx[nd], y + fish_dy[nd]
                    if 0 <= nx < 4 and 0 <= ny < 4 and smell[nx][ny] == 0 and (nx, ny) != shark:
                        new_map[nx][ny].append(nd)
                        moved = True
                        break
                if not moved:
                    new_map[x][y].append(d)
    return new_map

def move_shark():
    global shark, max_eat, best_route
    max_eat = -1
    best_route = []
    dfs_shark(shark[0], shark[1], 0, [], 0, set(), fish_map)

    x, y = shark
    for dir in best_route:
        x += shark_dx[dir]
        y += shark_dy[dir]
        if fish_map[x][y]:
            fish_map[x][y] = []
            smell[x][y] = 3  # 2턴동안 남아있다가 3턴이 시작할 때 냄새 사라짐
    shark = (x, y)

def decrease_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1

def fish_copy(copy_map):
    for i in range(4):
        for j in range(4):
            fish_map[i][j].extend(copy_map[i][j])

for _ in range(S):
    copy_map = copy.deepcopy(fish_map)   # 1. 복제 마법 시작
    fish_map = move_fish()               # 2. 물고기 이동
    move_shark()                         # 3. 상어 이동
    decrease_smell()                     # 4. 냄새 감소
    fish_copy(copy_map)                  # 5. 복제 마법 완료

result = 0
for i in range(4):
    for j in range(4):
        result += len(fish_map[i][j])
print(result)
