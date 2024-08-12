def f(n, arr):

    # for k in range(n-n//2):          N = 4, ARR = [1, 1, 2, 2]는 못 거름
    #     if arr[k] == arr[k+n//2]:
    #         return -1
    arr.sort()
    min_diff = 3000
    for i in range(n - 2):
        for j in range(i + 1, n - 1):  # 마지막 상자에 한 개 넣을 꺼 남겨 둬
            if arr[i] != arr[i + 1] and arr[j] != arr[j + 1]:  # small 과 medium 중복 방지 & medium 과 large 중복 방지
                small_num = i + 1
                medium_num = j - i
                large_num = n - j - 1
                if small_num <= n // 2 and medium_num <= n // 2 and large_num <= n // 2:  # 박스 다 개수 초과 금지
                    if min_diff >= max(small_num, medium_num, large_num) - min(small_num, medium_num, large_num):
                        min_diff = max(small_num, medium_num, large_num) - min(small_num, medium_num, large_num)

    if min_diff == 3000:
        return -1
    else:
        return min_diff


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))

    RESULT = f(N, ARR)

    print(f'#{TEST_CASE} {RESULT}')
