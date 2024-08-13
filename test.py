def f(blue, orange, bo_order):

    min_sec = 0

    B_location = 1
    O_location = 1

    B_len = len(blue)
    O_len = len(orange)

    blue_idx = 0
    orange_idx = 0

    # while True:
    for j in range(N):
        if bo_order[j] == 'B':
            if blue_idx < B_len and orange_idx < O_len:
                if abs(blue[blue_idx] - B_location) >= abs(orange[orange_idx] - O_location):
                    min_sec += abs(blue[blue_idx] - B_location) + 1
                    O_location = orange[orange_idx]
                    B_location = blue[blue_idx]
                    blue_idx += 1
                    orange_idx += 1
                elif abs(blue[blue_idx] - B_location) < abs(orange[orange_idx] - O_location):
                    min_sec += abs(orange[orange_idx] - O_location)
                    O_location = orange[orange_idx]
                    B_location = blue[blue_idx]
                    blue_idx += 1
                    orange_idx += 1
            elif blue_idx < B_len:
                min_sec += abs(blue[blue_idx] - B_location) + 1
                B_location = blue[blue_idx]
                blue_idx += 1
            elif orange_idx < O_len:
                min_sec += abs(orange[orange_idx] - O_location) + 1
                O_location = orange[orange_idx]
                orange_idx += 1
            else:
                min_sec += 1

        if bo_order[j] == 'O':
            if blue_idx < B_len and orange_idx < O_len:
                if abs(blue[blue_idx] - B_location) > abs(orange[orange_idx] - O_location):
                    min_sec += abs(blue[blue_idx] - B_location)
                    O_location = orange[orange_idx]
                    B_location = blue[blue_idx]
                    blue_idx += 1
                    orange_idx += 1
                elif abs(blue[blue_idx] - B_location) <= abs(orange[orange_idx] - O_location):
                    min_sec += abs(orange[orange_idx] - O_location) + 1
                    O_location = orange[orange_idx]
                    B_location = blue[blue_idx]
                    blue_idx += 1
                    orange_idx += 1
            elif blue_idx < B_len:
                min_sec += abs(blue[blue_idx] - B_location) + 1
                B_location = blue[blue_idx]
                blue_idx += 1
            elif orange_idx < O_len:
                min_sec += abs(orange[orange_idx] - O_location) + 1
                O_location = orange[orange_idx]
                orange_idx += 1
            else:
                min_sec += 1

    return min_sec


T = int(input())
for TEST_CASE in range(1, T+1):
    ARR = list(input().split())

    Blue = []
    Orange = []
    BO_order = []

    N = int(ARR[0])

    for i in range(1, len(ARR)):
        if i % 2 == 1:
            BO_order += ARR[i]
            if ARR[i] == 'B':
                Blue += [int(ARR[i+1])]
            elif ARR[i] == 'O':
                Orange += [int(ARR[i+1])]

    RESULT = f(Blue, Orange, BO_order)

    print(f'#{TEST_CASE} {RESULT}')
