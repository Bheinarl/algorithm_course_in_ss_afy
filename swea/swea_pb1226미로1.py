from collections import deque

for o in range(10):

    TEST_CASE = int(input())
    ARR = [list(input()) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if ARR[i][j] == '2':
                si, sj = i, j

    dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    que = deque()
    visited = [[0]*16 for _ in range(16)]
    que.append((si, sj))

    while que:
        ni, nj = que.popleft()
        visited[ni][nj] = 1

        if ARR[ni][nj] == '3':
            break

        for k in range(4):
            if 0 <= ni + dij[k][0] < 16 and 0 <= nj + dij[k][1] < 16:
                if ARR[ni + dij[k][0]][nj + dij[k][1]] != '1' and visited[ni + dij[k][0]][nj + dij[k][1]] == 0:
                    que.append((ni + dij[k][0], nj + dij[k][1]))

    if ARR[ni][nj] == '3':
        print(f'#{TEST_CASE} 1')
    else:
        print(f'#{TEST_CASE} 0')

"""
def dfs():

    ni, nj = si, sj
    noway = 0

    while stack:

        if ARR[ni][nj] == '3':
            break

        if noway == 0:
            ni, nj = stack[-1]
        else:
            ni, nj = stack.pop()
            noway = 0

        visited[ni][nj] = 1

        for k in range(4):
            if 0 <= ni + dij[k][0] < 16 and 0 <= nj + dij[k][1] < 16:
                if ARR[ni + dij[k][0]][nj + dij[k][1]] != '1' and visited[ni + dij[k][0]][nj + dij[k][1]] == 0:
                    stack.append((ni + dij[k][0], nj + dij[k][1]))
                    break
        else:
            noway = 1

    if ARR[ni][nj] == '3':
        return 1
    else:
        return 0


for ok in range(10):

    TEST_CASE = int(input())
    ARR = [list(input()) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if ARR[i][j] == '2':
                si, sj = i, j
            elif ARR[i][j] == '3':
                ei, ej = i, j

    dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    stack = []
    visited = [[0]*16 for _ in range(16)]
    stack.append((si, sj))
    result = 0
    ans = dfs()

    print(f'#{TEST_CASE} {ans}')
"""

"""
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
"""