from collections import deque

def bfs_outside_air():
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = 1
    grid[0][0] = -1  # 겉 공기를 -1로 설정

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if grid[nx][ny] <= 0:  # 공기거나 이미 겉 공기라면
                    visited[nx][ny] = 1
                    grid[nx][ny] = -1  # 겉 공기로 설정
                    queue.append((nx, ny))

def count_and_melt_cheese():
    melted_cheese = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:  # 치즈라면
                outside_air = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == -1:
                        outside_air = 1
                        break

                if outside_air:
                    melted_cheese.append((i, j))

    for x, y in melted_cheese:
        grid[x][y] = -1  # 녹은 치즈를 겉 공기로 변경

    return len(melted_cheese)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

time = 0
cheese_count = []

while True:
    bfs_outside_air()  # 겉 공기 표시

    melted = count_and_melt_cheese()  # 치즈 녹이기
    cheese_count.append(melted)

    if melted == 0:  # 더 이상 녹을 치즈가 없다면 종료
        break

    time += 1

print(time)  # 치즈가 모두 녹는 데 걸리는 시간
print(cheese_count[-2])  # 마지막으로 녹기 직전의 치즈 개수