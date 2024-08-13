def f(n, m, arr):

    max_counts = 0

    for i in range(n):
        counts_n = 0
        for j in range(m):
            if arr[i][j] == 1:
                counts_n += 1

            if counts_n >= 2 and max_counts <= counts_n:
                max_counts = counts_n

            if j <= m - 2 and arr[i][j+1] == 0:
                counts_n = 0

    for i in range(m):
        counts_m = 0
        for j in range(n):
            if arr[j][i] == 1:
                counts_m += 1

            if counts_m >= 2 and max_counts <= counts_m:
                max_counts = counts_m

            if j <= n-2 and arr[j+1][i] == 0:
                counts_m = 0

    return max_counts


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = f(N, M, ARR)

    print(f'#{TEST_CASE} {RESULT}')
