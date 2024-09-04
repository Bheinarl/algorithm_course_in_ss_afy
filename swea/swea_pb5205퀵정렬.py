def f1(left, right):
    mid = (left + right) // 2
    pivot = ARR[mid]  # 피벗을 중간 요소로 설정
    ARR[left], ARR[mid] = ARR[mid], ARR[left]  # 중간 요소를 왼쪽으로 이동 (필요 시)
    i = left + 1
    j = right

    while i <= j:
        while i <= j and ARR[i] <= pivot:
            i += 1
        while i <= j and ARR[j] >= pivot:
            j -= 1
        if i < j:
            ARR[i], ARR[j] = ARR[j], ARR[i]

    ARR[left], ARR[j] = ARR[j], ARR[left]
    return j


def f2(left, right):
    if left < right:

        pivot = f1(left, right)
        f2(left, pivot - 1)
        f2(pivot + 1, right)


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))

    f2(0, N-1)

    ans = ARR[N//2]

    print(f'#{TEST_CASE} {ans}')
