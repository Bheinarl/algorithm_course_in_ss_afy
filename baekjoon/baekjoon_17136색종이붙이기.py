def able_to_attach(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != 1:
                return False
    return True

def attach(x, y, size, value):
    for i in range(x, x + size):
        for j in range(y, y + size):
            board[i][j] = value

def dfs(x, y, used):
    global min_count

    if used >= min_count:
        return

    while x < 10 and board[x][y] != 1:
        y += 1
        if y == 10:
            x += 1
            y = 0

    if x == 10:
        min_count = min(min_count, used)
        return

    for size in range(5, 0, -1):
        if papers[size] > 0 and able_to_attach(x, y, size):
            attach(x, y, size, 0)
            papers[size] -= 1
            dfs(x, y, used + 1)
            attach(x, y, size, 1)
            papers[size] += 1

board = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
min_count = 26

dfs(0, 0, 0)

if min_count == 26:
    print(-1)
else:
    print(min_count)
