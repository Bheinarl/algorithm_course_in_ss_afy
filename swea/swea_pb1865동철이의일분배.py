def f(i, prb):
    global max_prb

    if prb == 0:
        return
    elif prb * 100 ** (N - i) < max_prb:
        return
    elif i == N:
        if max_prb < prb:
            max_prb = prb
    else:
        for j in range(N):
            if j not in path:
                path.append(j)
                f(i + 1, prb * ARR[i][j])
                path.pop()


T = int(input())
for TEST_CASE in range(1, T + 1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    path = []
    max_prb = 0
    f(0, 1)
    max_prb = max_prb * 100 ** (-N) * 100
    print(f'#{TEST_CASE} ', end='')
    print('%.6f' % max_prb)
