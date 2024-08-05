T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())

    array_1 = []
    for _ in range(n):
        array_1 += list(map(list, input().split()))

    array_2 = [[0]*n for _ in range(n)]

    for p in range(n):  # 뒤집힌 행렬 생성
        for q in range(n):
            array_2[p][q] = array_1[q][p]

    ans = 0

    for i in range(n):  # 멀쩡한 행렬에서 길이 m의 회문 찾기
        for j in range(n-m+1):
            for k in range(m//2):
                if array_1[i][j+k] != array_1[i][j+m-1-k]:  # 글자열을 반 접었을 때 다 다르다면 회문 X
                    break
            else:  # 글자열을 반 접었을 때 다 똑같다면(반복문을 끝까지 돌렸다면) 회문
                ans = array_1[i][j:j+m]

    for i in range(n):  # 뒤집힌 행렬에서 길이 m의 회문 찾기
        for j in range(n-m+1):
            for k in range(m//2):
                if array_2[i][j+k] != array_2[i][j+m-1-k]:  # 글자열을 반 접었을 때 다 다르다면 회문 X
                    break
            else:  # 글자열을 반 접었을 때 다 똑같다면(반복문을 끝까지 돌렸다면) 회문
                ans = array_2[i][j:j + m]

    print(f'#{test_case}', end=' ')
    for TXT in ans:
        print(f'{TXT}', end='')
    print('')

"""
def func(n, m, array_1):

    array_2 = []
    array_2 += [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            array_2[j][i] = array_1[i][j]

    for i in range(n):
        for j in range(n-m+1):
            if j == 0:
                if array_1[i][j:j+m] == array_1[i][j+m-1::-1]:
                    return array_1[i][j:j+m]
            else:
                if array_1[i][j:j+m] == array_1[i][j+m-1:j-1:-1]:
                    return array_1[i][j:j+m]

    for p in range(n):
        for q in range(n-m+1):
            if q == 0:
                if array_2[p][q:q+m] == array_2[p][q+m-1::-1]:
                    return array_2[p][q:q+m]
            else:
                if array_2[p][q:q+m] == array_2[p][q+m-1:q-1:-1]:
                    return array_2[p][q:q+m]


T = int(input())
for TEST_CASE in range(1, T + 1):
    N, M = map(int, input().split())

    ARR = []
    for _ in range(N):
        ARR += list(map(list, input().split()))

    RESULT = func(N, M, ARR)

    print(f'#{TEST_CASE}',end=' ')
    for TXT in RESULT:
        print(f'{TXT}',end='')
    print('')
"""