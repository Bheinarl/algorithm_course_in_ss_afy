import heapq

INF = int(1e9)

pb_num = 1

while True:
    N = int(input())

    if N == 0:  # 0 이면 끝
        break

    cave = [list(map(int, input().split())) for _ in range(N)]


    # 다익스트라를 위한 최소 힙 설정
    min_cost = [[INF] * N for _ in range(N)]  # 각 좌표까지 최소 비용
    pq = []  # 우선순위 큐

    # 시작점 초기화
    heapq.heappush(pq, (cave[0][0], 0, 0))  # (비용, x좌표, y좌표)
    min_cost[0][0] = cave[0][0]  # 시작점 = 초기 비용

    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while pq:
        now_cost, x, y = heapq.heappop(pq)  # 현재 비용, 좌표

        if now_cost > min_cost[x][y]:  # 이미 계산되었다면 패스
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                cost = now_cost + cave[nx][ny]  # 현재 노드를 지나갈 때

                if cost < min_cost[nx][ny]:  # 비용이 최소 비용보다 작다면
                    min_cost[nx][ny] = cost  # 갱신
                    heapq.heappush(pq, (cost, nx, ny))

    print(f"Problem {pb_num}: {min_cost[N - 1][N - 1]}")
    pb_num += 1
