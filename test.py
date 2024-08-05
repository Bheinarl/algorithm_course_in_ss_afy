def f(A, B):
    N = len(A)
    M = len(B)
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if A[j + i] != B[j]:
                break
        else:
            cnt += 1
    result = N - (M - 1) * cnt
    return result


T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())
    press_cnt = f(A, B)
    print(f'#{tc} {press_cnt}')