def dragon_curve(x, y, d, g):
    directions = [d]
    for _ in range(g):
        for i in range(len(directions)-1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    grid[y][x] = 1
    for dir in directions:
        x += dx[dir]
        y += dy[dir]
        if 0 <= x <= 100 and 0 <= y <= 100:
            grid[y][x] = 1

dx = [1, 0, -1, 0]  # 우 상 좌 하
dy = [0, -1, 0, 1]

grid = [[0]*101 for _ in range(101)]

N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve(x, y, d, g)

count = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i][j+1] and grid[i+1][j] and grid[i+1][j+1]:
            count += 1

print(count)
