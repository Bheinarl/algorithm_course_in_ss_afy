def f():

    min_counts = N*M+1
    for a in range(N-2):
        for b in range(a+1, N-1):
            counts = 0
            for j in range(M):
                for x in range(0, a+1):
                    if ARR[x][j] != 'W':
                        counts += 1
                for y in range(a+1, b+1):
                    if ARR[y][j] != 'B':
                        counts += 1
                for z in range(b+1, N):
                    if ARR[z][j] != 'R':
                        counts += 1

            if min_counts > counts:
                min_counts = counts

    return min_counts


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')
