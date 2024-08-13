def f(n, arr):

    sum_max = 0

    for i in range(n):
        for j in range(n):
            sum_ij = 0
            sum_ij += sum(arr[i])
            for k in range(n):
                sum_ij += arr[k][j]
            sum_ij -= arr[i][j]

            if sum_ij >= sum_max:
                sum_max = sum_ij

    return sum_max


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())

    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = f(N, ARR)

    print(f'#{TEST_CASE} {RESULT}')
