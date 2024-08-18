def sum_subset(N,K):

    A = [x for x in range(1,13)]

    counts = 0

    for i in range(1 << 12):
        sum_ele = 0
        num_ele = 0

        for j in range(12):
            if i & (1 << j):
                sum_ele += A[j] # 부분집합의 원소의 합
                num_ele += 1    # 부분집합의 원소의 갯수

        if sum_ele == K and num_ele ==N:
            counts += 1 # 부분집합의 원소의 합이 K고 부분집합의 원소의 갯수가 N개라면, 결과값 +1

    result = counts

    return result

T = int(input())

for test_case in range(1, T+1):

    N, K = map(int,input().split())
    result = sum_subset(N,K)

    print(f'#{test_case} {result}')

"""
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
"""