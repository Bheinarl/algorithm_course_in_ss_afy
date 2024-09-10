def find_set(x):  # x의 대표 원소 찾기
    while rep[x] != x:  # 대표 원소가 아니면, 자기 자신을 가르키지 않으면
        x = rep[x]  # x가 가르키는 원소가 대표인지 확인, 값을 새로운 인덱스
    return x


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))

    # 대표 원소 make_set(1) ~ make_set(N)
    rep = [n for n in range(N+1)]
    for i in range(M):
        n1, n2 = ARR[i*2], ARR[i*2+1]
        rep[find_set(n2)] = find_set(n1)  # union(n1, n2)

    # 대표 원소의 수
    cnt = 0
    for i in range(1, N+1):
        if rep[i] == i:  # 자기 자신을 가르키는 경우
            cnt += 1

    print(f'#{TEST_CASE} {cnt}')

"""
def find_set(x):

    while rep[x] != x:
        x = rep[x]

    return x


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))
    rep = [n for n in range(N+1)]

    for i in range(M):
        n1, n2 = ARR[2*i], ARR[2*i+1]
        rep[find_set(n1)] = find_set(n2)

    visited = []
    counts = 0
    for j in range(1, len(rep)):
        if rep[j] == j:
            counts += 1

    print(f'#{TEST_CASE} {counts}')

"""