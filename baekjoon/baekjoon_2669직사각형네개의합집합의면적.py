min_x = 101
max_x = 0
min_y = 101
max_y = 0

arr = [[0]*101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    if min_x > x1:
        min_x = x1

    if max_x < x2:
        max_x = x2

    if min_y > y1:
        min_y = y1

    if max_y < y2:
        max_y = y2

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

counts = 0
for p in range(min_x, max_x+1):
    for q in range(min_y, max_y+1):
        if arr[p][q] == 1:
            counts += 1

print(counts)
