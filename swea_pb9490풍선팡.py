def func(n, m, arr):

    max_pop_counts = 0
    for i in range(n):
        # pop_counts = 0
        for j in range(m):
            pop_counts = 0
            pop_num = arr[i][j]
            pop_counts += arr[i][j]
            if i < pop_num:
                for k in range(i):
                    pop_counts += arr[k][j]
            else:
                for k in range(1, pop_num+1):
                    pop_counts += arr[i-k][j]

            if i + pop_num >= n-1:
                for k in range(1, n-i):
                    pop_counts += arr[n-k][j]
            else:
                for k in range(1, pop_num+1):
                    pop_counts += arr[i+k][j]

            if j <= pop_num:
                for k in range(j):
                    pop_counts += arr[i][k]
            else:
                for k in range(1, pop_num+1):
                    pop_counts += arr[i][j-k]

            if j + pop_num >= m-1:
                for k in range(1, m-j):
                    pop_counts += arr[i][m-k]
            else:
                for k in range(1, pop_num+1):
                    pop_counts += arr[i][j+k]

            if pop_counts >= max_pop_counts:
                max_pop_counts = pop_counts

    return max_pop_counts


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = func(N, M, ARR)

    print(f'#{TEST_CASE} {RESULT}')
