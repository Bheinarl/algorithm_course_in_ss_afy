R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(x, y):
    if y == C - 1:
        return 1

    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True
    return False

result = 0
for i in range(R):
    if dfs(i, 0):
        result += 1

print(result)