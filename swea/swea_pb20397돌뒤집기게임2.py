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
