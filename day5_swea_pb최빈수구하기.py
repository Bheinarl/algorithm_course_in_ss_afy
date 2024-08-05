def find_mode(arr):

    already_num = []
    max_counts = 0
    max_num = 0

    for num in arr:
        counts = 0
        if num not in already_num:  # 해당 숫자가 한 번도 나온적이 없다면
            for num_arr in arr:
                if num == num_arr:  # 해당 숫자의 개수 세기
                    counts += 1
            already_num += [num]  # 해당 숫자는 나온 적이 있는 숫자 리스트에 넣기

        if counts > max_counts:  # 개수가 더 많으면 해당 숫자가 최빈수
            max_counts = counts
            max_num = num
        elif counts == max_counts and num > max_num:  # 개수가 같으면 값이 더 큰 숫자가 최빈수
            max_counts = counts
            max_num = num

    return max_num


T = int(input())
for _ in range(T):
    TEST_CASE_NUMBER = int(input())
    ARR = list(map(int, input().split()))

    result = find_mode(ARR)

    print(f'#{TEST_CASE_NUMBER} {result}')
