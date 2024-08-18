def f(n, m, arr):

    front = arr[0]  # 시작은 맨 앞 숫자
    for i in range(1, m+1):  # 한 칸씩 앞으로 땡겨
        front = arr[i % n]  # 앞으로 땡겼을 때 맨 앞에 있는 숫자

    return front  # 다 끝났을 때 마지막 숫자 반환


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))

    RESULT = f(N, M, ARR)

    print(f'#{TEST_CASE} {RESULT}')
