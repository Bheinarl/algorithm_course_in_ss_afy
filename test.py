def dfs():

    ni, nj = si, sj
    noway = 0

    while stack:

        if ARR[ni][nj] == '3':
            break

        if noway == 0:
            ni, nj = stack[-1]
        else:
            ni, nj = stack.pop()
            noway = 0

        visited[ni][nj] = 1

        for k in range(4):
            if 0 <= ni + dij[k][0] < 16 and 0 <= nj + dij[k][1] < 16:
                if ARR[ni + dij[k][0]][nj + dij[k][1]] != '1' and visited[ni + dij[k][0]][nj + dij[k][1]] == 0:
                    stack.append((ni + dij[k][0], nj + dij[k][1]))
                    break
        else:
            noway = 1

    if ARR[ni][nj] == '3':
        return 1
    else:
        return 0


for ok in range(10):

    TEST_CASE = int(input())
    ARR = [list(input()) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if ARR[i][j] == '2':
                si, sj = i, j
            elif ARR[i][j] == '3':
                ei, ej = i, j

    dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    stack = []
    visited = [[0]*16 for _ in range(16)]
    stack.append((si, sj))
    result = 0
    ans = dfs()

    print(f'#{TEST_CASE} {ans}')