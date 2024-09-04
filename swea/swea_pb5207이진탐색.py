def f1(low, high, target, up_down):
    global counts

    if low > high:
        return

    m = (low + high) // 2

    if A[m] == target:
        counts += 1
        return
    elif up_down != 'down' and A[m] > target:
        f1(low, m-1, target, 'down')
    elif up_down != 'up' and A[m] < target:
        f1(m+1, high, target, 'up')


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    counts = 0

    for i in range(len(B)):
        f1(0, N-1, B[i], None)


    print(f'#{TEST_CASE} {counts}')
