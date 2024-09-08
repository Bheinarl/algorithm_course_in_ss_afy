from collections import deque


def find_position(i, j):
    global counts
    q.append((i, j))
    visited[i][j] = 1
    counts += 1

    while q:
        (ni, nj) = q.popleft()

        for k in range(4):
            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < M and ARR[ni+di[k]][nj+dj[k]] != 0 and visited[ni+di[k]][nj+dj[k]] == 0:
                T_F = check_around(ARR[ni][nj], ARR[ni+di[k]][nj+dj[k]], k)
                if T_F == 1:
                    q.append((ni+di[k], nj+dj[k]))
                    visited[ni+di[k]][nj+dj[k]] = visited[ni][nj] + 1
                    if visited[ni+di[k]][nj+dj[k]] <= TIME:
                        counts += 1
                    elif visited[ni+di[k]][nj+dj[k]] > TIME:
                        break


def check_around(now_pipe, next_pipe, next_dirt):
    if next_dirt == 0:
        if now_pipe == 3 or now_pipe == 5 or now_pipe == 6:
            return 0
        else:
            if next_pipe != 3 and next_pipe != 4 and next_pipe != 7:
                return 1
            else:
                return 0
    if next_dirt == 1:
        if now_pipe == 2 or now_pipe == 6 or now_pipe == 7:
            return 0
        else:
            if next_pipe != 2 and next_pipe != 4 and next_pipe != 5:
                return 1
            else:
                return 0
    if next_dirt == 2:
        if now_pipe == 3 or now_pipe == 4 or now_pipe == 7:
            return 0
        else:
            if next_pipe != 3 and next_pipe != 5 and next_pipe != 6:
                return 1
            else:
                return 0
    if next_dirt == 3:
        if now_pipe == 2 or now_pipe == 4 or now_pipe == 5:
            return 0
        else:
            if next_pipe != 2 and next_pipe != 6 and next_pipe != 7:
                return 1
            else:
                return 0


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M, I, J, TIME = map(int, input().split())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    counts = 0
    q = deque()
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    visited = [[0]*M for _ in range(N)]

    find_position(I, J)

    print(f'#{TEST_CASE} {counts}')