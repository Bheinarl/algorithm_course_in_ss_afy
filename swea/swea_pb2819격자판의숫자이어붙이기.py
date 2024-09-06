def f(i, j, counts, txt):

    if counts == 7:
        txt = int(txt)
        if txt not in lst:
            lst.append(txt)
    else:
        for k in range(4):
            if 0 <= i+di[k] < 4 and 0 <= j+dj[k] < 4:
                f(i+di[k], j+dj[k], counts + 1, txt + str(ARR[i+di[k]][j+dj[k]]))


T = int(input())
for TEST_CASE in range(1, T+1):
    ARR = [list(map(int, input().split())) for _ in range(4)]

    lst = []
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for p in range(4):
        for q in range(4):
            f(p, q, 0, '')

    print(f'#{TEST_CASE} {len(lst)}')