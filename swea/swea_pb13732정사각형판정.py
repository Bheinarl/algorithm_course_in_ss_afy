T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(input())]

    counts = 0
    num_lst = [n**2 for n in range(1, 21)]
    for i in range(N):
        for j in range(N):
            if counts == 0 and ARR[i][j] == '#':
                p = i
                q = j
            if ARR[i][j] == '#':
                counts += 1

    if counts not in num_lst:
        print(f'#{TEST_CASE} no')
    else:
        for a in range(1, 21):
            if a**2 == counts:
                b = a
                break
        g = 0
        for x in range(p, p+b):
            for y in range(q, q+b):
                if ARR[x][y] != '#':
                    g = 1
                    print(f'#{TEST_CASE} no')
                    break
            if g == 1:
                break
        else:
            print(f'#{TEST_CASE} yes')

"""
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
"""