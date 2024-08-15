def find_start():

    for i in range(16):
        for j in range(16):
            if ARR[i][j] == '2':
                return i, j


def f(start_point_x, start_point_y):

    q = []
    visited = [[00] * 16 for _ in range(16)]
    q.append([start_point_x, start_point_y])
    visited[start_point_x][start_point_y] = 1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while q:
        [now_x, now_y] = q.pop(0)

        if ARR[now_x][now_y] == '3':
            return 1

        for k in range(4):
            if 0 <= now_x+di[k] < 16 and 0 <= now_y+dj[k] < 16 and ARR[now_x+di[k]][now_y+dj[k]] != '1' and visited[now_x+di[k]][now_y+dj[k]] == 0:
                q.append([now_x+di[k], now_y+dj[k]])
                visited[now_x+di[k]][now_y+dj[k]] = visited[now_x][now_y] + 1

    return 0


for _ in range(10):
    TEST_CASE = int(input())
    ARR = []

    for _ in range(16):
        ARR += [list(input())]

    start_point_x, start_point_y = find_start()
    RESULT = f(start_point_x, start_point_y)

    print(f'#{TEST_CASE} {RESULT}')
