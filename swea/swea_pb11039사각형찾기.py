def f():

    max_area = 0
    for i in range(N):
        for j in range(N):
            if ARR[i][j] == 1:
                now_i = i
                now_j = j
                width = 0
                length = 0
                while ARR[i][now_j] == 1:
                    width += 1
                    if now_j + 1 < N:
                        now_j += 1
                    else:
                        break

                while ARR[now_i][j] == 1:
                    length += 1
                    if now_i + 1 < N:
                        now_i += 1
                    else:
                        break

                if max_area < width * length:
                    max_area = width * length

    return max_area


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')