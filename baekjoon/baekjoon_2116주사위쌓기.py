def f(idx, arr):

    global sum_num

    if idx == 0:
        sum_num += max(arr[1], arr[2], arr[3], arr[4])
        return arr[5]
    elif idx == 1:
        sum_num += max(arr[0], arr[2], arr[4], arr[5])
        return arr[3]
    elif idx == 2:
        sum_num += max(arr[0], arr[1], arr[2], arr[3])
        return arr[4]
    elif idx == 3:
        sum_num += max(arr[0], arr[2], arr[4], arr[5])
        return arr[1]
    elif idx == 4:
        sum_num += max(arr[0], arr[1], arr[3], arr[5])
        return arr[2]
    elif idx == 5:
        sum_num += max(arr[1], arr[2], arr[3], arr[4])
        return arr[0]


N = int(input())

ARR = []
for _ in range(N):
    ARR += [list(map(int, input().split()))]

max_sum_num = 0
for k in range(6):
    sum_num = 0
    dice_bottom = f(k, ARR[0])
    for i in range(1, N):
        for j in range(6):
            if ARR[i][j] == dice_bottom:
                q = j
                break
        dice_bottom = f(q, ARR[i])

    if max_sum_num < sum_num:
        max_sum_num = sum_num

print(max_sum_num)