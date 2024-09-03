def block_count():  # 터트릴 블록들 다 저장
    global block_lst
    ni = i
    nj = j
    block_num = ARR[ni][nj]
    if block_num == 1:
        ARR[ni][nj] = 0
    else:
        for k in range(4):
            while block_num >= 0:
                pass



def f(i, counts):
    global min_counts

    if counts == N:
        pass
    else:
        pass






T = int(input())
for TEST_CASE in range(1, T+1):
    N, W, H = map(int, input().split())
    ARR = []
    for _ in range(H):
        ARR += [list(map(int, input().split()))]

    min_counts = W*H

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    block_lst = []

    for j in range(W):
        for i in range(H):
            if ARR[i][j] != 0:
                f(j, 0)