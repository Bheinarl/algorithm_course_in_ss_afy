def where_in_word(n, k, arr):

    # input_arr 에서 위쪽, 왼쪽에 각 한 칸, 오른쪽, 아래쪽에 각 k 칸을 8으로 채워서 검색에 방해 X
    whole_arr = [[8]*(n+k+1)]
    for arr_in_arr in arr:
        whole_arr += [[8] + arr_in_arr + [8] * k]
    whole_arr += [[8]*(n+k+1)] * k

    counts = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if whole_arr[i][j] == 1:
                num_i = i
                num_j = j
                # num_j 가 j ~ j+k-1 까지고, 행렬 끝을 넘어가지 않고 1일때 계속 반복
                while j <= num_j < j+k and num_j < n+k-1 and whole_arr[i][num_j] == 1:
                    if num_j == j+k-1:  # 단어 길이와 칸의 길이가 똑같으면 counts+1
                        if whole_arr[i][num_j+1] != 1 and whole_arr[i][j-1] != 1:
                            counts += 1
                    num_j += 1
                # num_i 가 i ~ i+k-1 까지고, 행렬 끝을 넘어가지 않고 1일때 계속 반복
                while i <= num_i < i+k and num_i < n+k-1 and whole_arr[num_i][j] == 1:
                    if num_i == i+k-1:  # 단어 길이와 칸의 길이가 똑같으면 counts+1
                        if whole_arr[num_i+1][j] != 1 and whole_arr[i-1][j] != 1:
                            counts += 1
                    num_i += 1

    return counts


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    result = where_in_word(N, K, ARR)

    print(f'#{test_case} {result}')
