def f(i, lst_A, lst_B):
    global min_diff

    if i == N:
        if len(lst_A) == N//2:

            food_A = 0
            food_B = 0
            for a in range(N//2):
                for b in range(a+1, N//2):
                    food_A += ARR[lst_A[a]][lst_A[b]] + ARR[lst_A[b]][lst_A[a]]

            for c in range(N//2):
                for d in range(c + 1, N//2):
                    food_B += ARR[lst_B[c]][lst_B[d]] + ARR[lst_B[d]][lst_B[c]]

            diff = abs(food_A - food_B)
            if diff < min_diff:
                min_diff = diff
    else:
        f(i+1, lst_A+[i], lst_B)
        f(i+1, lst_A, lst_B+[i])


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    min_diff = 20000
    f(0, [], [])

    print(f'#{TEST_CASE} {min_diff}')

"""
def f1(idx, lstA, lstB):
    global min_diff

    if idx == N and len(lstA) == N//2:

        foodA = synergy(lstA)
        foodB = synergy(lstB)
        diff = abs(foodA - foodB)
        if min_diff > diff:
            min_diff = diff
    elif idx == N:
        return
    else:
        f1(idx + 1, lstA+[idx], lstB)
        f1(idx + 1, lstA, lstB+[idx])


def synergy(arr):
    sum_food = 0
    for p in range(len(arr)):
        for q in range(len(arr)):
            sum_food += ARR[arr[p]][arr[q]]

    return sum_food


T = int(input())
for TEST_CASE in range(1, 1+T):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    lst = [u for u in range(N)]
    min_diff = 20001
    f1(0, [], [])

    print(f'#{TEST_CASE} {min_diff}')
"""