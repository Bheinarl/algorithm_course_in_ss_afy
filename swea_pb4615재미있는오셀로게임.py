T = int(input())
N, M = map(int, input().split())

ARR = [ [0] * (N+1) for _ in range(N+1)]
for _ in range(M):

    x, y, B_W = input().split()

    if B_W == 1:
        ARR[x][y] = 1
    else:
        ARR[x][y] = 2

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for k in range(4):
        z = 0
        while 0 <= x+di[k]*z < N and 0 <= y+dj[k]*z < N and ARR[x+di[k]*z][y+dj[k]*z] != 0:
            now_x = x+di[k]*z
            now_y = y+dj[k]*z
            z += 1
            if ARR[x+di[k]*z][y+dj[k]*z] == ARR[now_x][now_y]:
                break

        for _ in range(z):
            ARR[x+di[k]*z][y+dj[k]*z] == ARR[x][y]



