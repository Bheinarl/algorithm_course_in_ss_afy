T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = input().split()

    A = []
    B = []

    for i in range((N+1)//2):
        A += [ARR[i]]

    for i in range((N+1)//2, N):
        B += [ARR[i]]

    print(f'#{TEST_CASE}', end=' ')
    for i in range((N)//2):
        print(A[i], end=' ')
        print(B[i], end=' ')
    else:
        if len(A) != len(B):
            print(A[-1], end=' ')
    print()