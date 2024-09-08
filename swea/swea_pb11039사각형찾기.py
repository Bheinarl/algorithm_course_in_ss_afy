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

"""
T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    max_area = 0

    for i in range(N):
        for j in range(N):
            if ARR[i][j] == 1:
                width = 0
                height = 0

                for p in range(i, N):
                    if ARR[p][j] == 1:
                        height += 1
                    else:
                        break

                for q in range(j, N):
                    if ARR[i][q] == 1:
                        width += 1
                    else:
                        break

                area = width * height
                if area > max_area:
                    max_area = area

    print(f'#{TEST_CASE} {max_area}')
"""