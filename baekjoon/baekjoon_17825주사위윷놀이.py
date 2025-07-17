def dfs(round, total_score, positions, finished):
    global max_score

    if round == 10:
        max_score = max(max_score, total_score)
        return

    for i in range(4):
        if finished[i]:
            continue

        current_position = positions[i]
        move = dice[round]

        # 다음 위치 계산
        temp = current_position
        if temp in go_to_blue:
            temp = go_to_blue[temp]
            move -= 1

        for _ in range(move):
            temp = next_position[temp]

        if temp != 21 and temp in positions:  # 말 못 업으니깐
            continue

        # 저장
        prev_position = positions[i]
        positions[i] = temp
        prev_finished = finished[i]
        if temp == 21:
            finished[i] = True

        dfs(round + 1, total_score + board[temp], positions, finished)

        # 백트래킹
        positions[i] = prev_position
        finished[i] = prev_finished


dice = list(map(int, input().split()))

board = [0] * 33  # 윷놀이 판
next_position = [0] * 33  # 다음 어디로 가는지
go_to_blue = dict()

# 오직 빨간색만
for i in range(21):
    board[i] = i * 2
    next_position[i] = i + 1
board[21] = 0
next_position[21] = 21  # 도착점

# 10번에서 파란길 : 13[22] -> 16[23] -> 19[24] -> 25[25] -> 30[31]
board[22], board[23], board[24], board[25] = 13, 16, 19, 25
next_position[22], next_position[23], next_position[24], next_position[25] = 23, 24, 25, 31
go_to_blue[5] = 22

# 20에서 파란색 : 22[26] -> 24[27] -> 25[25]
board[26], board[27] = 22, 24
next_position[26], next_position[27] = 27, 25
go_to_blue[10] = 26

# 30번에서 파란길 : 28[28] -> 27[29] -> 26[30] -> 25[25]
board[28], board[29], board[30] = 28, 27, 26
next_position[28], next_position[29], next_position[30] = 29, 30, 25
go_to_blue[15] = 28

# 도착가는 공통 갈림길 30[31] -> 35[32] -> 40[20]
board[31], board[32] = 30, 35
next_position[31], next_position[32] = 32, 20

max_score = 0

dfs(0, 0, [0, 0, 0, 0], [False, False, False, False])

print(max_score)
