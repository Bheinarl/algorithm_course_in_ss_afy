T = int(input())
for TEST_CASE in range(1, T+1):
    N, Q = map(int, input().split())
    ARR = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            ARR[j] = i

    print(f'#{TEST_CASE}', end=' ')
    print(*ARR)