def f():

    weight = 0
    w = 0
    for t in range(M):
        while w <= N-1:
            if W_ARR[w] <= T_ARR[t]:
                weight += W_ARR[w]
                w += 1
                break
            w += 1

    return weight


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    W_ARR = list(map(int, input().split()))
    T_ARR = list(map(int, input().split()))

    W_ARR.sort(reverse=True)
    T_ARR.sort(reverse=True)

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')
