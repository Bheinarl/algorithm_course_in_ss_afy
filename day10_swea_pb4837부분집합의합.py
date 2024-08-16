def f(bit_start_index, amount_element, amount_element_subset, goal_sum_subset):
    global ans_count
    if bit_start_index == amount_element:
        sum_subset = 0
        count_element = 0
        for j in range(amount_element):
            if B[j]:  # if B[j] == 1:
                sum_subset += A[j]
                count_element += 1
        if sum_subset == goal_sum_subset and count_element == amount_element_subset:
            ans_count += 1

    else:
        B[bit_start_index] = 0  # 비트가 0일 때 = 부분집합에 해당 숫자가 들어갈 때
        f(bit_start_index+1, 12, N, K)
        B[bit_start_index] = 1  # 비트가 1일 때 = 부분집합에 해당 숫자가 들어갈 때
        f(bit_start_index+1, 12, N, K)


T = int(input())
for TEST_CASE in range(1, T+1):
    N, K = map(int, input().split())

    A = [i for i in range(1, 13)]
    B = [0] * 12
    ans_count = 0

    f(0, 12, N, K)

    print(f'#{TEST_CASE} {ans_count}')
