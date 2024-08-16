def f():

    counts_H = 0
    for p in range(N):
        for q in range(N):
            if ARR[p][q] == 'H':
                counts_H += 1

    di = [-1, 1, 0 ,0]  # 상하좌우
    dj = [0, 0, -1, 1]

    counts_H_A = 0

    for i in range(N):
        for j in range(N):
            if ARR[i][j] == 'H':
                for k in range(4):
                    now_i = i
                    now_j = j
                    gijiguk = 0
                    for z in range(3):
                        if 0 <= now_i+di[k] < N and 0 <= now_j+dj[k] < N:
                            now_i += di[k]
                            now_j += dj[k]
                            if z == 0 and ARR[now_i][now_j] == 'A':
                                counts_H_A += 1
                                gijiguk = 1
                                break
                            elif (z == 0 or z == 1) and ARR[now_i][now_j] == 'B':
                                counts_H_A += 1
                                gijiguk = 1
                                break
                            elif ARR[now_i][now_j] == 'C':
                                counts_H_A += 1
                                gijiguk = 1
                                break

                    if gijiguk == 1:
                        break

    return counts_H - counts_H_A


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())

    ARR = []
    for _ in range(N):
        ARR += [list(input())]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')
