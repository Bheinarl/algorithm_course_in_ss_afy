def f1(arr):

    for k in range(M-1, -1, -1):
        if arr[k] == '1':
            num = k
            break

    start_idx = num - 55

    ans_arr = []
    for i in range(8):
        if arr[start_idx+7*i:start_idx+7*i+7] == ['0', '0', '0', '1', '1', '0', '1']:
            ans_arr += [0]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '0', '1', '1', '0', '0', '1']:
            ans_arr += [1]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '0', '1', '0', '0', '1', '1']:
            ans_arr += [2]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '1', '1', '1', '1', '0', '1']:
            ans_arr += [3]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '1', '0', '0', '0', '1', '1']:
            ans_arr += [4]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '1', '1', '0', '0', '0', '1']:
            ans_arr += [5]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '1', '0', '1', '1', '1', '1']:
            ans_arr += [6]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '1', '1', '1', '0', '1', '1']:
            ans_arr += [7]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '1', '1', '0', '1', '1', '1']:
            ans_arr += [8]
        elif arr[start_idx+7*i:start_idx+7*i+7] == ['0', '0', '0', '1', '0', '1', '1']:
            ans_arr += [9]

    return ans_arr


def f2(lst):
    pw_lst = 0
    for q in range(8):
        if q % 2 == 0:
            pw_lst += 3 * lst[q]
        else:
            pw_lst += lst[q]

    if pw_lst % 10 == 0:
        return sum(lst)
    else:
        return 0


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []

    for _ in range(N):
        ARR += [list(input())]

    for arr_idx in range(N):
        if '1' in ARR[arr_idx]:
            pw2digit = f1(ARR[arr_idx])
            break

    RESULT = f2(pw2digit)

    print(f'#{TEST_CASE} {RESULT}')
