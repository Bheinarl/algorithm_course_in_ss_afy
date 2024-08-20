def f(n, arr):

    min_i = -1
    min_diff = -1

    for i in range(1, n):

        if i == 1:
            diff = abs(arr[0] - sum(arr[1:]))
        else:
            diff = abs(sum(arr[:i]) - sum(arr[i:]))

        if min_diff == -1:
            min_diff = diff
            min_i = i
        elif min_diff >= diff:
            min_diff = diff
            min_i = i

    return min_i, min_diff


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))

    RESULT1, RESULT2 = f(N, ARR)

    print(f'#{TEST_CASE} {RESULT1} {RESULT2}')
