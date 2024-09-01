def f(i):
    global min_diff
    global temp

    if i == N:

        A = lst[:N//2]
        B = lst[N//2:]

        if A in temp:
            return
        else:
            temp += [A]

        food_A = 0
        food_B = 0
        for a in range(len(A)-1):
            for b in range(a+1, len(A)):
                food_A += ARR[A[a]][A[b]] + ARR[A[b]][A[a]]

        for c in range(len(B) - 1):
            for d in range(c + 1, len(B)):
                food_B += ARR[B[c]][B[d]] + ARR[B[d]][B[c]]

        diff = abs(food_A - food_B)
        if diff < min_diff:
            min_diff = diff
    else:
        for j in range(i, N):
            lst[i], lst[j] = lst[j], lst[i]
            f(i+1)
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    lst = [n for n in range(N)]
    min_diff = 20000
    temp = []
    f(0)

    print(f'#{TEST_CASE} {min_diff}')
