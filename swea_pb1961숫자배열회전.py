T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR1 = []
    for _ in range(N):
        ARR1 += [list(input().split())]

    ANS = [[0] * 3 for _ in range(N)]

    ARR2 = [[0] * N for _ in range(N)]
    ARR3 = [[0] * N for _ in range(N)]
    ARR4 = [[0] * N for _ in range(N)]

    for i in range(N):
        txt = ''
        for j in range(N):
            ARR2[i][j] = ARR1[N-1-j][i]
            txt += str(ARR2[i][j])
        ANS[i][0] = txt

    for i in range(N):
        txt = ''
        for j in range(N):
            ARR3[i][j] = ARR2[N-1-j][i]
            txt += str(ARR3[i][j])
        ANS[i][1] = txt

    for i in range(N):
        txt = ''
        for j in range(N):
            ARR4[i][j] = ARR3[N-1-j][i]
            txt += str(ARR4[i][j])
        ANS[i][2] = txt

    print(f'#{TEST_CASE}')
    for ans_arr in ANS:
        print(*ans_arr)
