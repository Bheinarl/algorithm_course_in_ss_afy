def find_ladder(ladder):
    xi = 0
    xj = 0

    for i in range(100):            # X 위치 찾기
        for j in range(100):
            if ladder[i][j] == 2:
                xi = i
                xj = j

    current_point_i = xi  # 현재 위치를 X로 설정
    current_point_j = xj

    while current_point_i >= 0:  # 현재 위치의 i가 0이 되면 stop
        ladder[current_point_i][current_point_j] = 0  # 지나가면 0으로 전환
        if 0 < current_point_j < 99:  # j가 양 끝이 아니라면
            if ladder[current_point_i][current_point_j + 1] == 1:  # 오른쪽에 사다리가 있다면 이동
                current_point_j += 1
            elif ladder[current_point_i][current_point_j - 1] == 1:  # 왼쪽에 사다리가 있다면 이동
                current_point_j -= 1
            else:  # 좌우에 없으면 위로 이동
                current_point_i -= 1

        elif current_point_j == 99:  # j가 오른쪽 끝이라면
            if ladder[current_point_i][current_point_j - 1] == 1:  # 왼쪽에 사다리가 있다면 이동
                current_point_j -= 1
            else:  # 없으면 위로 이동
                current_point_i -= 1

        elif current_point_j == 0:  # j가 왼쪽 끝이라면
            if ladder[current_point_i][current_point_j + 1] == 1:  # 오른쪽에 사다리가 있다면 이동
                current_point_j += 1
            else:  # 없으면 위로 이동
                current_point_i -= 1

    return current_point_j  # 현재 j 좌표 반환


for _ in range(1, 11):

    test_case = int(input())
    arr = []

    for _ in range(100):
        arr += [list(map(int, input().split()))]

    result = find_ladder(arr)

    print(f'#{test_case} {result}')
