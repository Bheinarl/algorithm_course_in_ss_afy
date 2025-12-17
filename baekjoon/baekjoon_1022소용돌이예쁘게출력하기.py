import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

def find_vortex_num(r, c):
    vortex_size = max(abs(r), abs(c))
    max_num = (2 * vortex_size + 1) ** 2

    if r == vortex_size:  # 아래 변
        return max_num - (vortex_size - c)
    elif c == -vortex_size:  # 왼쪽 변
        return max_num - (2 * vortex_size) - (vortex_size - r)
    elif r == -vortex_size:  # 위쪽 변
        return max_num - (4 * vortex_size) - (vortex_size + c)
    else:  # c == vortex_size, 오른쪽 변
        return max_num - (6 * vortex_size) - (vortex_size + r)

board = []
max_len = 0

for i in range(r1, r2 + 1):
    row = []
    for j in range(c1, c2 + 1):
        v = find_vortex_num(i, j)
        row.append(v)
        max_len = max(max_len, len(str(v)))
    board.append(row)

for row in board:
    line = []
    for v in row:
        s = str(v)
        spaces = max_len - len(s)
        line.append(" " * spaces + s)
    print(" ".join(line))