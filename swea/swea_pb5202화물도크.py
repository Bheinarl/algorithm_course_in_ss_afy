T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    ARR.sort(key=lambda x: x[1])
    TIME = 0
    counts = 0
    while TIME <= 24:
        if TIME == 24:
            TIME += 1
            break

        for k in range(N):
            if ARR[k][0] >= TIME:
                TIME = ARR[k][1]
                counts += 1
                break
        else:
            TIME += 1

    print(f'#{TEST_CASE} {counts}')
