from copy import deepcopy

# 숫자 합치는 함수
def combine(line):

    new_line = [x for x in line if x != 0]  # 0 제거
    result = []
    is_same_num = False
    for i in range(len(new_line)):
        if is_same_num:
            is_same_num = False
            continue
        # 같은 숫자면 합치기
        if i + 1 < len(new_line) and new_line[i] == new_line[i + 1]:
            result.append(new_line[i] * 2)
            is_same_num = True
        else:
            result.append(new_line[i])
    # 부족한 부분은 0으로
    result += [0] * (N - len(result))
    return result

# 한 쪽으로 이동
def move(board, direction):

    new_board = [[0] * N for _ in range(N)]

    if direction == 0:  # 위
        for col in range(N):
            line = [board[row][col] for row in range(N)]
            combined = combine(line)
            for row in range(N):
                new_board[row][col] = combined[row]

    elif direction == 1:  # 아래
        for col in range(N):
            line = [board[row][col] for row in range(N - 1, -1, -1)]
            combined = combine(line)
            for row in range(N):
                new_board[N - 1 - row][col] = combined[row]

    elif direction == 2:  # 왼쪽
        for row in range(N):
            combined = combine(board[row])
            new_board[row] = combined

    elif direction == 3:  # 오른쪽
        for row in range(N):
            reversed_line = board[row][::-1]
            combined = combine(reversed_line)
            new_board[row] = combined[::-1]

    return new_board


def dfs(board, count):
    global max_block
    if count == 5:
        for row in board:
            max_block = max(max_block, max(row))
        return

    for d in range(4):  # 네 방향으로 이동
        moved = move(deepcopy(board), d)
        dfs(moved, count + 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_block = 0
dfs(board, 0)
print(max_block)
