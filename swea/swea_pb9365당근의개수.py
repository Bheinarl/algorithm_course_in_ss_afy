T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))

    max_index = 0
    max_carrot = 0
    for i in range(N):
        if C[i] >= max_carrot:
            max_index = i
            max_carrot = C[i]

    print(f'#{TEST_CASE} {max_index+1} {max_carrot}')