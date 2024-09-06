from collections import deque


def f(i, j):
    global max_counts
    global min_num

    q.append((i, j))
    counts = 1
    # visited 도 필요없다. 어차피 다시 못돌아감
    while q:

        (ni, nj) = q.popleft()
        for k in range(4):

            if 0 <= ni+di[k] < N and 0 <= nj+dj[k] < N and ARR[ni+di[k]][nj+dj[k]] == ARR[ni][nj] + 1:
                q.append((ni+di[k], nj+dj[k]))
                counts += 1
                break  # 같은 숫자가 없으니깐 다음 단계로 넘겨

    if counts > max_counts:
        max_counts = counts
        min_num = ARR[i][j]
    elif counts == max_counts:
        if ARR[i][j] < min_num:
            min_num = ARR[i][j]


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    max_counts = 0
    min_num = 0
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for i in range(N):  # 안좋다고 했지만 저런 생각을 할 자신이 없는걸,,,
        for j in range(N):
            f(i, j)

    print(f'#{TEST_CASE} {min_num} {max_counts}')