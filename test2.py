from collections import deque


def f(i, lst):

    global min_counts

    if min_counts == 0:
        return

    if len(lst) == N:
        block_temp = [a[:] for a in ARR]
        # 블록 남아있는 거 카운트
        counts = 0
        break_block(lst,block_temp)

        for p in range(H):
            for q in range(W):
                if block_temp[p][q] != 0:
                    counts += 1

        if min_counts > counts:
            min_counts = counts
    elif i == H:
        return
    else:
        for jj in range(W):
            f(i+1, lst+[jj])


def break_block(lst, block_temp):

    for jj in range(len(lst)):

        for ii in range(H):
            if block_temp[ii][lst[jj]] != 0:
                break

        q.append((ii, lst[jj]))
        visited = [[0] * W for _ in range(H)]
        q_break = deque()
        while q:
            (ni, nj) = q.popleft()
            q_break.append((ni, nj))
            visited[ni][nj] = 1

            for kk in range(block_temp[ni][nj]):
                for k in range(4):
                    if 0 <= ni + di[k]*kk < H and 0 <= nj + dj[k]*kk < W and visited[ni + di[k]*kk][nj + dj[k]*kk] != 1 and block_temp[ni + di[k]*kk][nj + dj[k]*kk] != 0:
                        q.append((ni + di[k]*kk, nj + dj[k]*kk))

        while q_break:
            (nii, njj) = q_break.popleft()
            block_temp[nii][njj] = 0

        for jjj in range(W):
            stack = []
            for iii in range(H):
                if block_temp[iii][jjj] != 0:
                    stack.append(block_temp[iii][jjj])
                    block_temp[iii][jjj] = 0

            iii_idx = H - 1
            while stack:
                block_temp[iii_idx][jjj] = stack.pop()
                iii_idx -= 1


T = int(input())
for TEST_CASE in range(1, T+1):
    N, W, H = map(int, input().split())
    ARR = []
    for _ in range(H):
        ARR += [list(map(int, input().split()))]

    min_counts = W*H
    storage = []
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = deque()

    f(0, [])

    print(f'#{TEST_CASE} {min_counts}')