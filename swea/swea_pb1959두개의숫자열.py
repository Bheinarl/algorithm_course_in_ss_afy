def f(arr1, arr2):

    max_sum = 0

    for i in range(len(arr2)-len(arr1)+1):
        sum_num = 0
        for j in range(len(arr1)):
            sum_num += arr1[j] * arr2[i+j]

        if max_sum < sum_num:
            max_sum = sum_num

    return max_sum


T = int(input())
for TEST_CASE in range (1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) < len(B):
        RESULT = f(A, B)
    else:
        RESULT = f(B, A)

    print(f'#{TEST_CASE} {RESULT}')

"""
def f(n, m, arr_a, arr_b):

    max_sum_number = -999999  # 진짜 이렇게 하기 싫은데 max 초기값 설정

    if n <= m:  # B의 길이가 더 길거나 같을 때
        for i in range(0, m-n+1):  # 움직일 범위 설정
            sum_number = 0
            for j in range(n):  # 고정 됐을 때, 계산 수행
                sum_number += arr_a[j] * arr_b[j+i]  # B가 더 길기 때문에 B의 인덱스를 j + i
            if max_sum_number <= sum_number:
                max_sum_number = sum_number

    else:  # A의 길이가 더 길 때
        for i in range(0, n-m+1):  # 움직일 범위 설정
            sum_number = 0
            for j in range(m):  # 고정 됐을 때, 계산 수행
                sum_number += arr_a[j+i] * arr_b[j]  # A가 더 길기 때문에 A의 인덱스를 j + i
            if max_sum_number <= sum_number:
                max_sum_number = sum_number

    return max_sum_number


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR_A = list(map(int, input().split()))
    ARR_B = list(map(int, input().split()))

    RESULT = f(N, M, ARR_A, ARR_B)

    print(f'#{TEST_CASE} {RESULT}')
"""