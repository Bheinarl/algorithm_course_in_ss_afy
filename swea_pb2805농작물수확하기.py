T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR +=[list(input())]

    p = N//2
    q = N//2

    # 1 -> 1
    # 2 -> 3
    # 3 -> 5

    sum_num = 0
    for i in range(0, N//2):
        for j in range(q-i, q+i+1):
            sum_num += int(ARR[i][j])

    for j in range(N):
        sum_num += int(ARR[N//2][j])

    for i in range(N//2+1, N):
        k = N-i-1
        for j in range(q-k, q+k+1):
            sum_num += int(ARR[i][j])

    print(f'#{TEST_CASE} {sum_num}')