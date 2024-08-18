def f():
    for N in range(100, -1, -1):
        for i in range(100):
            for j in range(101 - N):
                for k in range(N):
                    if ARR[i][j + k] != ARR[i][j + N - k - 1]:
                        break
                else:
                    return N

        for j in range(100):
            for i in range(101 - N):
                for l in range(N):
                    if ARR[i + l][j] != ARR[i + N - l - 1][j]:
                        break
                else:
                    return N

for TEST_CASE in range(1, 11):
    tc = int(input())
    ARR = []
    for _ in range(100):
        ARR += [input()]

    RESULT = f()

    print(f'#{tc} {RESULT}')
