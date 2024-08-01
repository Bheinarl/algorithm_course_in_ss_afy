def find_ladder(ladder):
    xi = 0
    xj = 0

    whole_arr = [[0] * (100 + 2)]
    for arr_in_arr in ladder:
        whole_arr += [[0] + arr_in_arr + [0]]
    whole_arr += [[0] * (100 + 2)]

    ic = []
    for i in range(1,100):
        for j in range(1,100):
            count = 0
            if whole_arr[i][j+1]==1:
                count += 1
            if whole_arr[i][j-1]==1:
                count += 1
            if whole_arr[i+1][j]==1:
                count +=1
            if whole_arr[i-1][j]==1:
                count +=1
            if count >=3:
                ic += [[i, j]]

    for i in range(100):            # X 위치 찾기
        for j in range(100):
            if ladder[i][j] == 2:
                xi = i
                xj = j

    now_i = xi
    now_j = xj

    while now_i > 0:  # now_i가 0일때까지
        if [now_i, now_j] in ic:  # 내 위치가 분기점에 있으면
            1 # 내 다음 인덱스 분기점으로 이동
            1 # i 한칸 위로 이동
        else: # 분기점에 없으면
            1 # i 한칸 위로로









    # for i in range(100):            # X 위치 찾기
    #     for j in range(100):
    #         if ladder[i][j] == 2:
    #             xi = i
    #             xj = j
    #
    # current_point_i = xi  # 현재 위치를 X로 설정
    # current_point_j = xj
    #
    # while current_point_i >= 0:  # 현재 위치의 i가 0이 되면 stop
    #     ladder[current_point_i][current_point_j] = 0  # 지나가면 0으로 전환
    #     if 0 < current_point_j < 99:  # j가 양 끝이 아니라면
    #         if ladder[current_point_i][current_point_j + 1] == 1:  # 오른쪽에 사다리가 있다면 이동
    #             current_point_j += 1
    #         elif ladder[current_point_i][current_point_j - 1] == 1:  # 왼쪽에 사다리가 있다면 이동
    #             current_point_j -= 1
    #         else:  # 좌우에 없으면 위로 이동
    #             current_point_i -= 1
    #
    #     elif current_point_j == 99:  # j가 오른쪽 끝이라면
    #         if ladder[current_point_i][current_point_j - 1] == 1:  # 왼쪽에 사다리가 있다면 이동
    #             current_point_j -= 1
    #         else:  # 없으면 위로 이동
    #             current_point_i -= 1
    #
    #     elif current_point_j == 0:  # j가 왼쪽 끝이라면
    #         if ladder[current_point_i][current_point_j + 1] == 1:  # 오른쪽에 사다리가 있다면 이동
    #             current_point_j += 1
    #         else:  # 없으면 위로 이동
    #             current_point_i -= 1

    # return current_point_j  # 현재 j 좌표 반환
    pass


for _ in range(1, 11):

    test_case = int(input())
    arr = []

    for _ in range(100):
        arr += [list(map(int, input().split()))]

    result = find_ladder(arr)

    print(f'#{test_case} {result}')