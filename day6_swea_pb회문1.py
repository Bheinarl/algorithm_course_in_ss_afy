for test_case in range(1, 11):
    m = int(input())

    array_1 = []
    for _ in range(8):
        array_1 += list(map(list, input().split()))

    array_2 = [[0]*8 for _ in range(8)]

    for p in range(8):  # 뒤집힌 행렬 생성
        for q in range(8):
            array_2[p][q] = array_1[q][p]

    ans = 0

    for i in range(8):  # 멀쩡한 행렬에서 길이 m의 회문 찾기
        for j in range(9-m):
            for k in range(m//2):
                if array_1[i][j+k] != array_1[i][j+m-1-k]:  # 글자열을 반 접었을 때 다 다르다면 회문 X
                    break
            else:  # 글자열을 반 접었을 때 다 똑같다면(반복문을 끝까지 돌렸다면) 회문
                ans += 1

    for i in range(8):  # 뒤집힌 행렬에서 길이 m의 회문 찾기
        for j in range(9-m):
            for k in range(m//2):
                if array_2[i][j+k] != array_2[i][j+m-1-k]:  # 글자열을 반 접었을 때 다 다르다면 회문 X
                    break
            else:  # 글자열을 반 접었을 때 다 똑같다면(반복문을 끝까지 돌렸다면) 회문
                ans += 1

    print(f'#{test_case} {ans}')
