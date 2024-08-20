def sort_numbers_selection_sort(n, lst):  # 선택 정렬을 이용한 정렬

    for i in range(n-1):  # i부터 마지막 전까지 순회
        min_idx = i

        for j in range(i+1, n):  # 한 칸 앞부터 끝까지 순회해서 최솟값 검색
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]  # 현재 값과 최솟값 교환

    return lst


def sort_numbers_bubble_sort(n, lst):  # 버블 정렬을 이용한 정렬

    for i in range(n-1, 0, -1):  # 마지막 원소부터 하나씩 줄어드는
        for j in range(0, i):   # 처음 원소부터 하나씩 줄어든 마지막 원소까지 계속 최댓값 교환
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))

    # result = sort_numbers_selection_sort(N, arr)
    result = sort_numbers_bubble_sort(N, arr)

    print(f'#{test_case}', end=' ')
    for num in result:
        print(num, end=' ')
    print('')