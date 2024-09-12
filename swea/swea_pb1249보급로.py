from collections import deque

T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ARR[i][j] = int(ARR[i][j])

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    visited = [[int(1e9)]*(N+1) for _ in range(N+1)]

    q = deque()
    q.append((0, 0))
    visited[0][0] = 0

    while q:
        (ni, nj) = q.popleft()

        for k in range(4):
            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < N:
                if visited[ni+di[k]][nj+dj[k]] > visited[ni][nj] + ARR[ni+di[k]][nj+dj[k]]:
                    visited[ni+di[k]][nj+dj[k]] = visited[ni][nj] + ARR[ni+di[k]][nj+dj[k]]
                    q.append((ni+di[k], nj+dj[k]))

    print(f'#{TEST_CASE} {visited[N-1][N-1]}')
