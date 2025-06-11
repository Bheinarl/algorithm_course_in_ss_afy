from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def mark_island(x, y, num):
    q = deque()
    q.append((x, y))
    graph[x][y] = num
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = num
                q.append((nx, ny))

island_num = 2
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            mark_island(i, j, island_num)
            island_num += 1

edges = []
def find_bridges(x, y, island):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        length = 0
        while 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == island:
                break
            elif graph[nx][ny] == 0:
                length += 1
            else:
                if length >= 2:
                    edges.append((length, island, graph[nx][ny]))
                break
            nx += dx[d]
            ny += dy[d]

for i in range(N):
    for j in range(M):
        if graph[i][j] >= 2:
            find_bridges(i, j, graph[i][j])

edges.sort()
parent = [i for i in range(island_num)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return True
    return False

total = 0
count = 0
for cost, a, b in edges:
    if union(a, b):
        total += cost
        count += 1

if count == island_num - 3:
    print(total)
else:
    print(-1)
