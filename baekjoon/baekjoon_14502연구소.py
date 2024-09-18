from collections import deque
from copy import deepcopy
import sys


def check_0():

    temp = deepcopy(ARR)
    que = deque()

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                que.append((i, j))

    while que:
        ni, nj = que.popleft()

        for k in range(4):
            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < M and temp[ni+di[k]][nj+dj[k]] == 0:
                temp[ni+di[k]][nj+dj[k]] = 2
                que.append((ni+di[k], nj+dj[k]))

    counts_zero = 0
    for lst_lst in temp:
        counts_zero += lst_lst.count(0)  # 이래도 시간초과

    return counts_zero


def check_0_lst(lst):

    temp = deepcopy(ARR)
    que = deque()

    for idx in lst:
        (x, y) = arr_none[idx]
        temp[x][y] = 1

    for virus in arr_virus:
        que.append(virus)

    while que:
        ni, nj = que.popleft()

        for k in range(4):
            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < M and temp[ni+di[k]][nj+dj[k]] == 0:
                temp[ni+di[k]][nj+dj[k]] = 2
                que.append((ni+di[k], nj+dj[k]))

    counts_zero = 0
    for lst_lst in temp:
        counts_zero += lst_lst.count(0)

    return counts_zero


N, M = map(int, sys.stdin.readline().split())
ARR = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_0 = 0
no_wall = []
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

arr_none = []
arr_virus = []

for i in range(N):
    for j in range(M):
        if ARR[i][j] == 0:
            arr_none.append((i, j))
        elif ARR[i][j] == 2:
            arr_virus.append((i, j))

for a in range(len(arr_none)-2):
    for b in range(a+1, len(arr_none)-1):
        for c in range(b+1, len(arr_none)):
            wall_list = [a, b, c]
            counts_zero1 = check_0_lst(wall_list)
            if max_0 < counts_zero1:
                max_0 = counts_zero1

print(max_0)

"""
이번엔 다르게 풀어보자라고 생각했는데 안되더라구요...
맨날 리스트에 사용할꺼 저장하는 식으로 하다가 <바꾸고, 저장하고, 원상복귀> 방법을 해보자 했는데
시간초과가 너무 떠서 포기했습니다.
"""