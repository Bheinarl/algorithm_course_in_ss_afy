def f():

    for i in range(9):
        for j in range(8):
            for k in range(j+1, 9):
                if ARR[i][j] == ARR[i][k]:
                    return 0

                if ARR[j][i] == ARR[k][i]:
                    return 0

    for x in range(3):
        for y in range(3):
            visited = [0] * 10
            for p in range(3*x, 3*x+3):
                for q in range(3*y, 3*y+3):
                    if visited[ARR[p][q]] == 1:
                        return 0
                    else:
                        visited[ARR[p][q]] = 1

    return 1


T = int(input())
for TEST_CASE in range(1, T+1):

    ARR = []
    for _ in range(9):
        ARR += [list(map(int, input().split()))]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')
