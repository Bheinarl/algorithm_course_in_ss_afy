import heapq


def dijk(idx):

    q = []
    for idk in adjL[idx]:
        heapq.heappush(q, idk)

    while q:
        ne, nw = heapq.heappop(q)

        if distance[ne] < nw:
            continue

        for next_data in adjL[ne]:
            next_idx = next_data[0]
            next_value = next_data[1]

            now_next_value = nw + next_value

            if distance[next_idx] <= now_next_value:
                continue

            distance[next_idx] = now_next_value
            heapq.heappush(q, (next_idx, now_next_value))

    return distance[N]


T = int(input())
for TEST_CASE in range(1, T+1):
    N, E = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    distance = [int(1e9)]*(N+1)
    for u in range(E):
        s, e, w = map(int, input().split())
        adjL[s] += [(e, w)]

    ans = dijk(0)

    print(f'#{TEST_CASE} {ans}')
