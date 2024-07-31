def dif_maxhei_minhei(n, arr):

    while n > 0:

        count = 0
        max_hei = arr[0]
        min_hei = arr[0]
        max_idx = 0
        min_idx = 0

        for num in arr:
            if num > max_hei:
                max_hei = num
                max_idx = count

            if num < min_hei:
                min_hei = num
                min_idx = count

            count += 1

        arr[max_idx] -= 1
        arr[min_idx] += 1
        n -= 1

    min_height = arr[0]
    max_height = arr[0]

    for nbr in arr:
        if nbr > max_height:
            max_height = nbr

        if nbr < min_height:
            min_height = nbr

    result = max_height - min_height

    return result



for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = dif_maxhei_minhei(n, arr)

    print(f'#{test_case} {result}')