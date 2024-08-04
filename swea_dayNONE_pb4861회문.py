def func(n, m, array_1):

    array_2 = []
    array_2 += [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            array_2[j][i] = array_1[i][j]

    for i in range(n):
        for j in range(n-m+1):
            if j == 0:
                if array_1[i][j:j+m] == array_1[i][j+m-1::-1]:
                    return array_1[i][j:j+m]
            else:
                if array_1[i][j:j+m] == array_1[i][j+m-1:j-1:-1]:
                    return array_1[i][j:j+m]

    for p in range(n):
        for q in range(n-m+1):
            if q == 0:
                if array_2[p][q:q+m] == array_2[p][q+m-1::-1]:
                    return array_2[p][q:q+m]
            else:
                if array_2[p][q:q+m] == array_2[p][q+m-1:q-1:-1]:
                    return array_2[p][q:q+m]


T = int(input())
for TEST_CASE in range(1, T + 1):
    N, M = map(int, input().split())

    ARR = []
    for _ in range(N):
        ARR += list(map(list, input().split()))

    RESULT = func(N, M, ARR)

    print(f'#{TEST_CASE}',end=' ')
    for TXT in RESULT:
        print(f'{TXT}',end='')
    print('')
