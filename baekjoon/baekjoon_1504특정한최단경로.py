import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 무방향

v1, v2 = map(int, input().split())

dist1  = dijkstra(1, graph, N)
distV1 = dijkstra(v1, graph, N)
distV2 = dijkstra(v2, graph, N)

# 경로 1: 1 -> v1 -> v2 -> N
route1 = dist1[v1] + distV1[v2] + distV2[N]
# 경로 2: 1 -> v2 -> v1 -> N
route2 = dist1[v2] + distV2[v1] + distV1[N]

ans = min(route1, route2)
print(-1 if ans >= INF else ans)