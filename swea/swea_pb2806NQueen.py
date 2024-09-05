def check(ii, jj):

    for iii in range(ii):
        if ARR[iii][jj] == 1:
            return 0

    iii, jjj = ii - 1, jj - 1
    while iii >= 0 and jjj >= 0:
        if ARR[iii][jjj] == 1:
            return 0
        iii -= 1
        jjj -= 1

    iii, jjj = ii - 1, jj + 1
    while iii >= 0 and jjj < N:
        if ARR[iii][jjj] == 1:
            return 0
        iii -= 1
        jjj += 1

    return 1


def dfs(i):
    global counts

    if i == N:
        counts += 1
        return
    else:
        for j in range(N):
            if check(i, j):
                ARR[i][j] = 1
                dfs(i+1)
                ARR[i][j] = 0


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = [[0]*N for _ in range(N)]
    counts = 0

    dfs(0)

    print(f'#{TEST_CASE} {counts}')