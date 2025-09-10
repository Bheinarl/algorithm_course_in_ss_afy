import sys

def find_num_print(position):
    if position == len(empty_blanks):
        print('\n'.join(''.join(map(str, row)) for row in board))
        sys.exit()

    r, c = empty_blanks[position]
    box_index = (r//3)*3 + (c//3)

    for d in range(1, 10):
        if not used_row[r][d] and not used_col[c][d] and not used_box[box_index][d]:
            # 놓기
            board[r][c] = d
            used_row[r][d] = used_col[c][d] = used_box[box_index][d] = True

            find_num_print(position + 1)

            # 되돌리기
            board[r][c] = 0
            used_row[r][d] = used_col[c][d] = used_box[box_index][d] = False


board = [list(map(int, input().strip())) for _ in range(9)]

used_row = [[False]*10 for _ in range(9)]
used_col = [[False]*10 for _ in range(9)]
used_box = [[False]*10 for _ in range(9)]

empty_blanks = []
for r in range(9):
    for c in range(9):
        v = board[r][c]
        if v == 0:
            empty_blanks.append((r, c))
        else:
            used_row[r][v] = True
            used_col[c][v] = True
            used_box[(r//3)*3 + (c//3)][v] = True

find_num_print(0)