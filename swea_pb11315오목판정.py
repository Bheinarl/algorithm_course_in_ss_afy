def f1():

    for i in range(N):  # 가로 확인
        for j in range(N-4):
            if ARR[i][j] == 'o' and ARR[i][j + 1] == 'o' and ARR[i][j + 2] == 'o' and ARR[i][j + 3] == 'o' and ARR[i][j + 4] == 'o':
                return 'YES'

    for i in range(N-4):  # 세로 확인
        for j in range(N):
            if ARR[i][j] == 'o' and ARR[i + 1][j] == 'o' and ARR[i + 2][j] == 'o' and ARR[i + 3][j] == 'o' and ARR[i + 4][j] == 'o':
                return 'YES'

    for i in range(N - 4):  # 오른쪽 아래로 가는 대각선 확인
        for j in range(N - 4):
            if ARR[i][j] == 'o' and ARR[i + 1][j + 1] == 'o' and ARR[i + 2][j + 2] == 'o' and ARR[i + 3][j + 3] == 'o' and ARR[i + 4][j + 4] == 'o':
                return 'YES'

    for i in range(N-4):  # 왼쪽 아래로 가는 대각선 확인
        for j in range(4, N):
            if ARR[i][j] == 'o' and ARR[i+1][j-1] == 'o' and ARR[i+2][j-2] == 'o' and ARR[i+3][j-3] == 'o' and ARR[i+4][j-4] == 'o':
                return 'YES'

    return 'NO'


def f2():  # f1이 더 빠른거 같은데... 일단 델타 연습

    di = [1, -1, 0, 0, -1, -1, 1, 1]  # 상하좌우, 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래
    dj = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(N):
        for j in range(N):
            for k in range(8):
                if 0 <= i+di[k]*4 < N and 0 <= j+dj[k]*4 < N and ARR[i][j] == 'o':  # 5번째까지 범위 안에 들고 'o'라면
                    for l in range(1,5):  # l = 1, 2, 3, 4
                        if ARR[i+di[k]*l][j+dj[k]*l] != 'o':  # o가 아니라면
                            break  # for l 구문 break
                    else:  # 5개까지 버틴다면 오목
                        return 'YES'

    return 'NO'  # 다 순회했는데 아무것도 없으면 오목 없는 것


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]

    RESULT = f2()

    print(f'#{TEST_CASE} {RESULT}')
