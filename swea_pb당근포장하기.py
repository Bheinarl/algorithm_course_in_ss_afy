def f(n, arr):

    for a in range(0, n - n//2):
        if arr[a] == arr[a+n//2]:
            return -1

    carrot_size = [0] * (arr[-1]+1)
    carrot_max_size = arr[-1]
    for num in arr:
        carrot_size[num] += 1

    ans = 1001
    for i in range(carrot_max_size):  # 3분할 하기 위해서 2중 for문 사용
        for j in range(i + 1, carrot_max_size + 1):
            # print(i, j)
            small_box = 0  # i를 기준으로 앞 부분은 작은 박스
            for small in range(i):
                small_box += carrot_size[small]
            if small_box == 0 or small_box > n//2:  # 만약 용량보다 많거나, 1개도 들지 않았다면 다음 루프로
                continue

            mid_box = 0
            for mid in range(i, j):  # i와 j 사이의 부분은 중간 박스
                mid_box += carrot_size[mid]
            if mid_box == 0 or mid_box > n//2:
                continue

            big_box = 0
            for big in range(j, carrot_max_size + 1):  # j를 기준으로 이후는 큰 박스
                big_box += carrot_size[big]
            if big_box == 0 or big_box > n//2:
                continue

            # print('@@@', [small_box, mid_box, big_box])

            min_d, max_d = 1001, -1  # 최소값, 최대값 측정
            for box in [small_box, mid_box, big_box]:
                if min_d > box:
                    min_d = box
                if max_d < box:
                    max_d = box
            temp_d = max_d - min_d  # 둘의 차이의 최소값을 확인 후 할당
            if ans >= temp_d:
                ans = temp_d

    return ans


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))

    RESULT = f(N, ARR)

    print(f'#{TEST_CASE} {RESULT}')

