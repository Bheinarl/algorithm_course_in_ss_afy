def check_status(lst):
    status = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            status += ARR[lst[i]][lst[j]]

    return status


def f(idx, lst_A, lst_B):

    global min_diff

    if min_diff == 0:
        return

    if idx == N and len(lst_A) == 0:
        return
    elif idx == N and len(lst_B) == 0:
        return
    elif idx == N:
        sum_A = check_status(lst_A)
        sum_B = check_status(lst_B)
        diff = abs(sum_B - sum_A)

        min_diff = min(min_diff, diff)

    else:
        f(idx + 1, lst_A+[idx], lst_B)
        f(idx + 1, lst_A, lst_B+[idx])


N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]
min_diff = 100 * N**2
f(0, [], [])

print(min_diff)