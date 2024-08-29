T = int(input())
for TEST_CASE in range(1, T+1):
    N = float(input())

    n = -1
    counts = 0
    arr = []

    while N != 0 and counts <= 12:
        if N >= 2**n:
            N -= 2**n
            arr += [1]
        else:
            arr += [0]

        n -= 1
        counts += 1

    if counts > 12:
        print(f'#{TEST_CASE} overflow')
    else:
        print(f'#{TEST_CASE} ', end='')
        for k in range(len(arr)):
            print(arr[k], end='')
        print()