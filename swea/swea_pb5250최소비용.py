import heapq


def dijk(i, j):
    pq = []
    heapq.heappush(pq, (0, i, j))

    while pq:

        nfuel, ni, nj = heapq.heappop(pq)
        if visited[ni][nj] < nfuel:
            continue

        for k in range(4):
            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < N:
                fuel = nfuel + 1
                if ARR[ni][nj] < ARR[ni+di[k]][nj+dj[k]]:
                    fuel += (ARR[ni+di[k]][nj+dj[k]] - ARR[ni][nj])

                if visited[ni+di[k]][nj+dj[k]] <= fuel:
                    continue

                visited[ni+di[k]][nj+dj[k]] = fuel
                heapq.heappush(pq, (fuel, ni+di[k], nj+dj[k]))

    return visited[N-1][N-1]


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    visited = [[int(1e9)]*N for _ in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    ans = dijk(0, 0)

    print(f'#{TEST_CASE} {ans}')
