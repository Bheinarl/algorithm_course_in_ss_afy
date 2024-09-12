import heapq


def f(i, j):

    if i == j:  # 똑같으면 그냥 돌아가쇼
        return 0

    visited = [int(1e9)] * (N+1)
    q = []

    heapq.heappush(q, (0, i))  # 걸린 시간, 현재 위치  (지금은 이제 출발했으니깐 시간은 0, 위치는 출발지)
    visited[i] = 0

    while q:  # 이정도면 그냥 프리셋으로 외워도 되겠어요
        go_time, idx = heapq.heappop(q)
        if visited[idx] < go_time:
            continue

        for data in adjL[idx]:
            new_go_time = data[0]
            new_idx = data[1]
            new_time = visited[idx] + new_go_time

            if visited[new_idx] <= new_time:
                continue
            visited[new_idx] = new_time
            heapq.heappush(q, (new_time, new_idx))

    return visited[j]  # 다 돌려보았을 때 도착지까지 걸리는 최소 시간을 알고 싶다.


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M, X = map(int, input().split())
    EDGE = [list(map(int, input().split())) for _ in range(M)]
    adjL = [[] for _ in range(N+1)]

    for o in range(M):
        adjL[EDGE[o][0]] += [(EDGE[o][2], EDGE[o][1])]  # heapQ 쓰려고 시간을 먼저 앞에다가 배치

    max_time = 0
    for u in range(1, 1+N):
        sum_time = 0
        sum_time += f(u, X)  # 왔다
        sum_time += f(X, u)  # 갔다
        if sum_time > max_time:
            max_time = sum_time

    print(f'#{TEST_CASE} {max_time}')
