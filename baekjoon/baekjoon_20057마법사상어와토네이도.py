N = int(input())
sand_land = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌하우상

# 좌하우상 순서
sand_distribution = {
    # 좌
    0: [
        (-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07),
        (-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (1, -1, 0.1),
        (0, -2, 0.05), (0, -1, 'alpha')
    ],
    # 하
    1: [
        (-1, -1, 0.01), (-1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07),
        (0, -2, 0.02), (0, 2, 0.02), (1, -1, 0.1), (1, 1, 0.1),
        (2, 0, 0.05), (1, 0, 'alpha')
    ],
    # 우
    2: [
        (-1, -1, 0.01), (1, -1, 0.01), (-1, 0, 0.07), (1, 0, 0.07),
        (-2, 0, 0.02), (2, 0, 0.02), (-1, 1, 0.1), (1, 1, 0.1),
        (0, 2, 0.05), (0, 1, 'alpha')
    ],
    # 상
    3: [
        (1, -1, 0.01), (1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07),
        (0, -2, 0.02), (0, 2, 0.02), (-1, -1, 0.1), (-1, 1, 0.1),
        (-2, 0, 0.05), (-1, 0, 'alpha')
    ]
}

def tornado(x, y, d):
    global out_sand
    sand_move_pattern = sand_distribution[d]
    total = sand_land[x][y]
    scatter = 0

    for dx, dy, ratio in sand_move_pattern:
        nx, ny = x + dx, y + dy
        if ratio == 'alpha':
            sand = total - scatter
        else:
            sand = int(total * ratio)
            scatter += sand

        if 0 <= nx < N and 0 <= ny < N:
            sand_land[nx][ny] += sand
        else:
            out_sand += sand

    sand_land[x][y] = 0

x, y = N // 2, N // 2
length = 1
d = 0
out_sand = 0

while True:
    for _ in range(2):
        for _ in range(length):
            dx, dy = directions[d]
            x += dx
            y += dy
            tornado(x, y, d)
            if x == 0 and y == 0:
                print(out_sand)
                exit()
        d = (d + 1) % 4
    length += 1
