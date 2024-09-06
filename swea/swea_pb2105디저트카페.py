def f(i, j, d3, d1, lst):  # d3 : 오른쪽 아래로 몇번 갈껀지, d1 : 왼쪽 아래로 몇 번 갈껀지

    global max_counts

    if d1 >= 1:
        lst_check = lst[:]
        T_F = check(i, j, d3, d1, lst_check)  # 이게 가능한지 판별
        if T_F:
            if max_counts < 2 * (d3 + d1):
                max_counts = 2 * (d3 + d1)

    # 오른쪽 아래로 갈 수 있으면 가세요 근데 왼쪽 아래로 간 적 없어야해요
    if 0 <= i + di[0] < N and 0 <= j + dj[0] < N and d1 == 0 and ARR[i + di[0]][j + dj[0]] not in lst:
        f(i + di[0], j + dj[0], d3 + 1, d1, lst + [ARR[i + di[0]][j + dj[0]]])

    # 왼쪽 아래로 갈 수 있으면 가세요 오른쪽 아래로 간 적 있어야하고 이제 오른쪽 아래로 못가요
    if 0 <= i + di[1] < N and 0 <= j + dj[1] < N and d3 != 0 and ARR[i + di[1]][j + dj[1]] not in lst:
        f(i + di[1], j + dj[1], d3, d1 + 1, lst + [ARR[i + di[1]][j + dj[1]]])


def check(i, j, d3, d1, lst_check):  # 무조건 오른쪽 아래 간 횟수만큼 왼쪽 위로 가야되고, 왼쪽 아래로 간 만큼 오른쪽 위로 가야됨
                                     # 그러면 제자리에 돌아오게 되어있음

    if 0 <= i + ddi[0] * d3 < N and 0 <= j + ddj[0] * d3 < N:  # 끝까지 가도 괜찮을까요

        for u in range(d3):  # 오른쪽 아래로 횟수만큼 판별하면서 이동

            i += ddi[0]
            j += ddj[0]

            if ARR[i][j] in lst_check:
                return 0
            else:
                lst_check += [ARR[i][j]]

    else:
        return 0

    if 0 <= i + ddi[1] * d1 < N and 0 <= j + ddj[1] * d1 < N:  # 끝까지 가도 괜찮을까요

        for u in range(d1):  # 왼쪽 아래로 횟수만큼 판별하면서 이동

            i += ddi[1]
            j += ddj[1]

            if i == p and j == q:  # 제자리로 돌아오다면 굿
                return 1
            elif ARR[i][j] in lst_check:
                return 0
            else:
                lst_check += [ARR[i][j]]

    else:
        return 0

    return 1


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 1]  # 오른쪽 아래, 왼쪽 아래
    dj = [1, -1]

    ddi = [-1, -1]
    ddj = [-1, 1]

    max_counts = -1
    for p in range(N-1):  # 다 순회하면 편해
        for q in range(N-1):  # 근데 아래, 오른쪽 마지막 줄은 쓸모 없어
            if 0 <= p+di[0] < N and 0 <= q+dj[0] < N:
                f(p, q, 0, 0, [ARR[p][q]])

    print(f'#{TEST_CASE} {max_counts}')
