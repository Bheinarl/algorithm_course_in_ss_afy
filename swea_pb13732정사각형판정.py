def find_start(): # bfs 처럼 풀면 되지않을까

    for i in range(N):
        for j in range(N):
            if ARR[i][j] == '#':
                pass
    pass





T = int(input())
for TEST_CASE in range(1, T+1):
    N= int(input())

    ARR = []
    for _ in range(N):
        ARR += [list(input())]

    RESULT = find_start()

    print(f'#{TEST_CASE} {RESULT}')
