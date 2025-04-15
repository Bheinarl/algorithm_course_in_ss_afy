from collections import deque


def find_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bfs(maps):
    n = len(maps)
    visited = [0] * n
    Q = deque()
    Q.append(0)

    while Q:
        now_location_index = Q.popleft()

        if now_location_index == n - 1:
            return "happy"

        for i in range(n):
            if not visited[i] and find_dist(maps[now_location_index], maps[i]) <= 1000:
                visited[i] = 1
                Q.append(i)

    return "sad"


T = int(input())
for _ in range(T):
    N = int(input())
    maps = []
    for _ in range(N + 2):
        x, y = map(int, input().split())
        maps.append((x, y))

    print(bfs(maps))