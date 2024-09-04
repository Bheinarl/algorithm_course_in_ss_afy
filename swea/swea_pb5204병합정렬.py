def merge_arr(arr):
    if len(arr) == 1:
        return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = merge_arr(left)
    right = merge_arr(right)

    return merge_sort(left, right)

def merge_sort(left, right):

    global counts

    result = [0] * (len(left) + len(right))

    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result[left_idx + right_idx] = left[left_idx]
            left_idx += 1
        else:
            result[left_idx + right_idx] = right[right_idx]
            right_idx += 1

    if right_idx == len(right):
        counts += 1

    while left_idx < len(left):
        result[left_idx + right_idx] = left[left_idx]
        left_idx += 1

    while right_idx < len(right):
        result[left_idx + right_idx] = right[right_idx]
        right_idx += 1

    return result


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))
    counts = 0
    ARR = merge_arr(ARR)


    print(f'#{TEST_CASE} {ARR[N//2]} {counts}')