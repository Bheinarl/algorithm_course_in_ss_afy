def find_start():
    lst = []
    for j in range(100):
        if ARR[0][j] == 1:
            lst += [j]
    return lst


def f(x, y):
    visited = [[0]*100 for _ in range(100)]
    counts = 0
    while x < 100:
        if y+1 < 100 and ARR[x][y+1] == 1 and visited[x][y+1] == 0:
            visited[x][y] = 1
            y += 1
            counts += 1
        elif 0 <= y-1 and ARR[x][y-1] == 1 and visited[x][y-1] == 0:
            visited[x][y] = 1
            y -= 1
            counts += 1
        else:
            visited[x][y] = 1
            x += 1
            counts += 1

    return counts


for TEST_CASE in range(1, 11):
    tc = int(input())
    ARR = []
    for _ in range(100):
        ARR += [list(map(int, input().split()))]

    start_j_arr = find_start()

    min_counts = 10001
    min_start_j = -1
    for k in range(len(start_j_arr)):
        RESULT = f(0, start_j_arr[k])
        if RESULT < min_counts:
            min_counts = RESULT
            min_start_j = start_j_arr[k]

    print(f'#{TEST_CASE} {min_start_j}')
