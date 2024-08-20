def f():

    ans = []

    if len(A) <= len(B):
        for i in range(len(A)):
            ans += [A.pop(0)]
            ans += [B.pop(0)]

        if len(B) != 0:
            for j in range(len(B)):
                ans += [B.pop(0)]
    else:
        for i in range(len(B)):
            ans += [A.pop(0)]
            ans += [B.pop(0)]
        if len(A) != 0:
            for j in range(len(A)):
                ans += [A.pop(0)]

    return ans


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    RESULT = f()

    print(f'#{TEST_CASE}', end=' ')
    print(*RESULT)
