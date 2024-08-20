def f():

    counts = 0
    for i in range(N):
        for j in range(N):
            if ARR[i][j] == '#':
                counts += 1

    if counts not in [n**2 for n in range(1, N+1)]:  # 정사각형이 될 수 없는 갯수(n^2가 아닌)면 걸러
        return 'no'

    for n in range(1, N+1):  # 정사각형 size 구해
        if counts == n**2:
            break

    for p in range(N):
        for q in range(N):
            if ARR[p][q] == '#':  # 보이는 첫 #로 시작
                for x in range(p, p+n):
                    for y in range(q, q+n):
                        if ARR[x][y] != '#':
                            return 'no'
                else:
                    return 'yes'
    else:
        return 'no'


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())

    ARR = []
    for _ in range(N):
        ARR += [list(input())]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')
