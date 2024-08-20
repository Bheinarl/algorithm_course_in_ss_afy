def f1():
    global arr_num
    global arr_area
    global arr_ij

    for i in range(N):
        for j in range(N):
            if ARR[i][j] != 0:
                length = 0
                width = 0
                now_i = i
                now_j = j
                while ARR[now_i][j] != 0:
                    length += 1
                    if now_i + 1 < N:
                        now_i += 1
                    else:
                        break

                while ARR[i][now_j] != 0:
                    width += 1
                    if now_j + 1 < N:
                        now_j += 1
                    else:
                        break

                arr_num += 1
                arr_area += [length*width]
                arr_ij += [length, width]

                for p in range(i, i+length):
                    for q in range(j, j+width):
                        ARR[p][q] = 0


def f2():

    while len(arr_area) > 0:
        min_area = N * N + 1
        min_idx = []
        for z in range(len(arr_area)):
            if arr_area[z] < min_area:
                min_area = arr_area[z]
                min_idx = [z]
            elif arr_area[z] == min_area:
                min_idx += [z]

        if arr_area.count(min_area) == 1:
            arr_area.pop(min_idx[0])
            ans.append(arr_ij.pop(2*min_idx[0]))
            ans.append(arr_ij.pop(2*min_idx[0]))

        else:
            min_length = 100
            min_length_idx = 0
            for q in range(len(min_idx)):
                if arr_ij[2*min_idx[q]] < min_length:
                    min_length = arr_ij[2*min_idx[q]]
                    min_length_idx = min_idx[q]
            arr_area.pop(min_length_idx)
            ans.append(arr_ij.pop(2*min_length_idx))
            ans.append(arr_ij.pop(2 * min_length_idx))


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    ans = []
    arr_ij = []
    arr_area = []
    arr_num = 0
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    f1()
    ans.append(arr_num)
    f2()

    print(f'#{TEST_CASE}', end=' ')
    print(*ans, end=' ')
    print()
