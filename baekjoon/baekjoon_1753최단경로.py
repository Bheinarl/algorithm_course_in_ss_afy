import sys
import heapq

INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V + 1):
    print(distance[i] if distance[i] != INF else "INF")
