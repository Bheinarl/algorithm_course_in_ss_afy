T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR_A = list(map(int, input().split()))
    ARR_B = list(map(int, input().split()))
    counts = 0

    for i in range(N):
        if ARR_A[i] != ARR_B[i]:
            for j in range(i, N):
                if ARR_A[j] == 1:
                    ARR_A[j] = 0
                else:
                    ARR_A[j] = 1
            counts += 1

        if ARR_A == ARR_B:
            break

    print(f'#{TEST_CASE} {counts}')