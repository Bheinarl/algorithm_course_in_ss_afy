def bfs(start_i, start_j, n, maze):
    q = []  # 큐 생성
    visited = [[0] * (n+1) for _ in range(n+1)]  # visit 생성
    q.append([start_i, start_j])  # 출발지 인큐
    visited[start_i][start_j] = 1  # 출발지 visit

    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]  # 상하좌우

    while q:
        [now_i, now_j] = q.pop(0)
        if maze[now_i][now_j] == 3:
            return visited[now_i][now_j] - 2  # 출발점 빼주고, 도착점 뺴주고

        for i in range(4):
            if 0 <= now_i+di[i] < n and 0 <= now_j+dj[i] < n and maze[now_i+di[i]][now_j+dj[i]] != 1 and visited[now_i+di[i]][now_j+dj[i]] == 0:
                q.append([now_i+di[i], now_j+dj[i]])
                visited[now_i+di[i]][now_j+dj[i]] = visited[now_i][now_j] + 1

    return 0


def find_start(n):
    for i in range(n):
        for j in range(n):
            if MAZE[i][j] == 2:
                return i, j


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    MAZE = [list(map(int, input())) for _ in range(N)]

    START_I, START_J = find_start(N)

    RESULT = bfs(START_I, START_J, N, MAZE)

    print(f'#{TEST_CASE} {RESULT}')
