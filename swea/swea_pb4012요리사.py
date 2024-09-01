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
