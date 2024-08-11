def f(n, m, start_index, arr):
    global counts

    counts += start_index

    if arr[start_index] > m:
        arr[start_index] -= m
        counts += start_index
        return f(n, m, start_index, arr)

    elif arr[start_index] == m:
        arr[start_index] -= m
        counts += start_index
        return f(n, m, start_index+1, arr)

    else:
        arr[start_index] = 0


    pass


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))

    counts = 0
    RESULT = f(N, M, 1, ARR)

    print(f'#{TEST_CASE} {RESULT}')