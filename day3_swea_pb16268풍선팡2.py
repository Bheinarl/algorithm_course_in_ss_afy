def max_balloon_pop_wsad(N,M,arr): # 상, 하, 좌, 우 값이 존재할 때, 자기자신 + 각각 더해주는 함수

    max_pop = 0

    for i in range(N):

        for j in range(M):

            sum_pop = 0
            sum_pop += arr[i][j]
            if i > 0:
                sum_pop += arr[i-1][j] # 위가 존재할 때, 위의 값 추가

            if i < N-1:
                sum_pop += arr[i+1][j] # 아래가 존재할 때, 아래 값 추가

            if j > 0:
                sum_pop += arr[i][j-1] # 왼쪽이 존재할 때, 왼쪽 값 추가

            if j < M-1:
                sum_pop += arr[i][j+1] # 오른쪽이 존재할 때, 오른쪽 값 추가

            if sum_pop > max_pop:
                max_pop = sum_pop

    result = max_pop

    return result

def max_balloon_pop_cover_zero(N,M,arr): # 받은 array를 0으로 둘러싸서 델타를 이용하는데 방해받지 않게하는 함수

    # 0으로 array를 둘러싼 행렬 whole_arr 생성
    whole_arr = [[0]*(M+2)]
    for arr_in_arr in arr:
        whole_arr += [[0] + arr_in_arr + [0]]
    whole_arr += [[0]*(M+2)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_pop = 0

    for i in range(1,N+1):
        for j in range(1,M+1):  # NxM 배열의 모든 원소에 대해
            sum_CNSWE = whole_arr[i][j] # 자기 자신 + i, j 원소의 4 방향 원소의 합 구하기
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                sum_CNSWE += whole_arr[ni][nj]

            if sum_CNSWE > max_pop:
                max_pop = sum_CNSWE

    result = max_pop

    return result

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr += [list(map(int,input().split()))]

    # result = max_balloon_pop_wsad(N,M,arr)     # 상하좌우가 존재할 때 값을 더하는 함수
    result = max_balloon_pop_cover_zero(N,M,arr) # 0으로 둘러싼 행렬로 델타 이용하는 함수
    print(f'#{test_case} {result}')