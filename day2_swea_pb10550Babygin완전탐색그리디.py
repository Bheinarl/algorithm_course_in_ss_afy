T = int(input())

def max_min_place_dif(arr):

    min_num = arr[0]
    max_num = arr[0]
    max_place = 0
    min_place = 0
    idx = 0

    for num in arr:
        if num < min_num:
            min_num = num
            min_place = idx


        if num >= max_num:
            max_num = num
            max_place = idx

        idx += 1

    if max_place - min_place >= 0:
        result = max_place - min_place
    else:
        result = min_place - max_place

    return result



for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = max_min_place_dif(arr)

    print(f'#{test_case} {result}')