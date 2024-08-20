for tc in range(1, 11):
    hundred = int(input())

    ARR = []
    for _ in range(100):
        ARR += [list(map(int, input().split()))]

    counts = 0
    for j in range(100):
        np = 0
        for i in range(100):
            if ARR[i][j] == 1:
                np = 1
            elif ARR[i][j] == 2 and np == 1:
                counts += 1
                np = 0

    print(f'#{tc} {counts}')

"""
for TEST_CASE in range(1,11):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    counts = 0
    for j in range(N):
        check_number = 0
        for i in range(N):
            if ARR[i][j] == 1:
                check_number = 1
            elif ARR[i][j] == 2 and check_number == 1:
                counts += 1
                check_number = 0

    print(f'#{TEST_CASE} {counts}')
"""