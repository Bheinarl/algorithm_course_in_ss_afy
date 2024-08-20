for TEST_CASE in range(1, 11):
    N = int(input())
    ARR = []
    for _ in range(8):
        ARR += [input()]

    counts = 0
    for i in range(8):
        for j in range(9-N):
            for k in range(N):
                if ARR[i][j+k] != ARR[i][j+N-k-1]:
                    break
            else:
                counts += 1

    for j in range(8):
        for i in range(9-N):
            for l in range(N):
                if ARR[i+l][j] != ARR[i+N-l-1][j]:
                    break
            else:
                counts += 1

    print(f'#{TEST_CASE} {counts}')

"""
T = int(input())
for tc in range(1, T+1):
    s = input()
    n = len(s)
    ans = 1
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            ans = 0
            break
    print(f'#{tc} {ans}')
"""
