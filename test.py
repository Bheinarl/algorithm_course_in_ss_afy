def find_ladder(ladder):

    current_i = 0
    current_j = 0
    ladder_j = []

    for j in range(100):
        if ladder[0][j] == 1:
            ladder_j += [j]

    while ladder[99][current_j] == 2:
        for j in ladder_j:
            current_j = j
            ladder[current_i][current_j] = 0

            if current_j == 0:
                if ladder[current_i][current_j + 1] == 1:  # 오른쪽에 사다리가 있다면 이동
                    current_j += 1
                else:  # 없으면 위로 이동
                    current_i -= 1
            elif current_j == 99:
                pass
            else:
                pass







    return result
    # pass

for test_case in range(1, 11):

    test_case = int(input())
    arr = []

    for _ in range(100):
        arr += [list(map(int, input().split()))]

    result = find_ladder(arr)

    print(f'#{test_case} {result}')