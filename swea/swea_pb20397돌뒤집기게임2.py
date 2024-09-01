T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        index_i = i - 1

        for k in range(1, j+1):
            if 0 <= index_i - k and index_i + k < N and ARR[index_i - k] == ARR[index_i + k]:
                if ARR[index_i - k] == 1:
                    ARR[index_i - k] = 0
                    ARR[index_i + k] = 0
                elif ARR[index_i - k] == 0:
                    ARR[index_i - k] = 1
                    ARR[index_i + k] = 1

    print(f'#{TEST_CASE}', end=' ')
    print(*ARR)


"""
def f(n, arr, m, lst):
    for k in range(m):
        i = lst[2*k] - 1
        j = lst[2*k+1]

        p = 1
        while p <= j and i+p <= n-1 and i-p >= 0:
            if arr[i+p] == arr[i-p]:
                if arr[i+p] == 1:
                    arr[i+p] = 0
                    arr[i-p] = 0
                else:
                    arr[i+p] = 1
                    arr[i-p] = 1

            p += 1

    return arr


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))
    LST = []

    for _ in range(M):
        I, J = map(int, input().split())
        LST += [I, J]

    result = f(N, ARR, M, LST)

    print(f'#{TEST_CASE}', end=' ')
    print(*result)
"""