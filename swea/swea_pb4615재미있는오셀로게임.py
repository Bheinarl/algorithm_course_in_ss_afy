T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    ARR = [[0] * (N + 1) for _ in range(N + 1)]

    ARR[N // 2 + 1][N // 2] = 1
    ARR[N // 2][N // 2 + 1] = 1
    ARR[N // 2][N // 2] = 2
    ARR[N // 2 + 1][N // 2 + 1] = 2

    for _ in range(M):

        x, y, B_W = map(int, input().split())

        if B_W == 1:
            ARR[x][y] = 1
        else:
            ARR[x][y] = 2

        di = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상하좌우, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 순서
        dj = [0, 0, -1, 1, -1, 1, -1, 1]

        for k in range(8):
            z = 1
            now_x = 0
            now_y = 0

            # 범위 내에 있고, 0이 아니라면 (1 or 2)
            while 0 <= x + di[k] * z <= N and 0 <= y + dj[k] * z <= N and ARR[x + di[k] * z][y + dj[k] * z] != 0:

                now_x = x + di[k] * z
                now_y = y + dj[k] * z

                if ARR[now_x][now_y] == B_W:  # 방금 둔 돌과 같은 색이라면 그만!
                    break

                z += 1  # 다른 색이면 계속 순회 해
            # while 문을 빠져 나오려면 방금 둔 돌과 같은 색이거나, 끝까지 갔는데 없거나
            if ARR[now_x][now_y] != 0 and ARR[now_x][now_y] == B_W:  # 없는 경우 제외시켜주고 같은 색이라면
                for p in range(1, z):  # 그 사이에 있는 돌은 방금 둔 돌과 같은 색으로 변경
                    ARR[x + di[k] * p][y + dj[k] * p] = B_W

    counts_black = 0
    counts_white = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if ARR[i][j] == 1:
                counts_black += 1
            elif ARR[i][j] == 2:
                counts_white += 1

    print(f'#{TEST_CASE} {counts_black} {counts_white}')
