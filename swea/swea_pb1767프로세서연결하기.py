"""
가운데에 있는 프로세서들 순열 써서 순서대로 연결
"""
di = [-1, 0, 1, 0]  # 상우하좌
dj = [0, 1, 0, -1]

def connect(p, d):
    connect_check = 0
    connecting_wire = 0
    ni, nj = list_core_x[p] + di[d], list_core_y[p] + dj[d]
    while 0 <= ni < N and 0 <= nj < N and ARR[ni][nj] == 0:
        ni += di[d]
        nj += dj[d]
    if ni < 0 or ni == N or nj < 0 or nj == N:  # 끝까지 순회했으니깐 연결할 수 있음
        connect_check = 1
        ni, nj = list_core_x[p] + di[d], list_core_y[p] + dj[d]
        while 0 <= ni < N and 0 <= nj < N and ARR[ni][nj] == 0:
            ARR[ni][nj] = 2
            connecting_wire += 1
            ni += di[d]
            nj += dj[d]

    return connect_check, connecting_wire


def disconnect(p, d):
    ni, nj = list_core_x[p] + di[d], list_core_y[p] + dj[d]
    while 0 <= ni < N and 0 <= nj < N:
        ARR[ni][nj] = 0
        ni += di[d]
        nj += dj[d]


def f1(p, connected_core, wire):  # p : 코어 번호, connected_core : 연결한 코어, wire : 현재 연결한 전선 길이
    global max_core
    global min_wire
    if p == num_core:
        if max_core < connected_core:
            max_core = connected_core
            min_wire = wire
        elif max_core == connected_core and min_wire > wire:
            min_wire = wire
    elif max_core > connected_core + num_core - p:  # 전망도 검사
        return
    else:
        for d in range(4):
            connect_check, connecting_wire = connect(p, d)
            f1(p+1, connected_core + connect_check, wire + connecting_wire)

            if connect_check == 1:
                disconnect(p, d)


T = int(input())
for TEST_CASE in range(1, T + 1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    list_core_x = []
    list_core_y = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if ARR[i][j] == 1:
                list_core_x += [i]
                list_core_y += [j]
    num_core = len(list_core_x)

    max_core = 0
    min_wire = N**2
    f1(0, 0, 0)

    print(f'#{TEST_CASE} {min_wire}')
