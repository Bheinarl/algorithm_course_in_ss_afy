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