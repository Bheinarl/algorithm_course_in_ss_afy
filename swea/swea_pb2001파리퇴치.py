def f():

    max_sum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_fly = 0
            for p in range(i, i+M):
                for q in range(j, j+M):
                    sum_fly += ARR[p][q]

            if max_sum < sum_fly:
                max_sum = sum_fly

    return max_sum


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')

"""
T = int(input())

def kill_fly(N,M,arr):

    max_fly = 0

    # 파리채의 기준을 왼쪽 위로 설정
    # 파리채가 스캔할때 NxN 밖으로 나가지 않을 범위까지 파리채 기준을 설정
    # i = 0 ~ N-M+1, j = 0 ~ N-M+1

    for i in range(N-M+1):
        for j in range(N-M+1):

            fly = 0

            for p in range(i,i+M):      # 파리채의 영역 i = 0 ~ M
                for q in range(j,j+M):  # 파리채의 영역 j = 0 ~ M
                    fly += arr[p][q]

            if fly > max_fly:
                max_fly = fly

    result = max_fly

    return result

for test_case in range(1, T+1):
    N, M = map(int,input().split())

    arr = []
    for _ in range(N):
        arr += [list(map(int, input().split()))]


    result = kill_fly(N,M,arr)

    print(f'#{test_case} {result}')
"""