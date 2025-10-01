import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, adj, n):
    # 거리: 미방문은 -1, 시작점은 0
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])

    while q:
        cur = q.popleft()
        # 현재 노드와 연결된 모든 노드 확인
        for nxt, w in adj[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + w  # 거리 갱신
                q.append(nxt)

    # 어딘지 모르는 노드에서 시작했으므로, 이것과 가장 먼 노드를 찾아
    far_node = 1
    for i in range(2, n + 1):
        if dist[i] > dist[far_node]:
            far_node = i
    return far_node, dist

N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N):
    data = list(map(int, input().split()))
    v = data[0]
    i = 1
    # (a, w) 쌍으로 파싱
    while i < len(data) and data[i] != -1:
        a = data[i]
        w = data[i + 1]
        adj[v].append((a, w))
        adj[a].append((v, w))
        i += 2

# 1에서 가장 먼 정점 u 찾기 -> u에서 가장 먼 거리 = 지름
u, _ = bfs(1, adj, N)
v, dist_from_u = bfs(u, adj, N)
print(dist_from_u[v])