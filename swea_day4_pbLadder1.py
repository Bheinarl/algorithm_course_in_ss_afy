def find_ladder_w_hj(ladder):
    xi = 0
    xj = 0

    # 사다리에서 가로로 지나가야 하는 곳(이하 분기점) 찾는데 방해받지 않게 0으로 둘러싼 행렬 생성
    whole_arr = [[0] * (100 + 2)]
    for arr_in_arr in ladder:
        whole_arr += [[0] + arr_in_arr + [0]]
    whole_arr += [[0] * (100 + 2)]

    """
    whole_arr = [[0]*(N+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    """

    for i in range(102):            # X(값이 2인 곳) 위치 찾기
        for j in range(102):
            if whole_arr[i][j] == 2:
                xi = i
                xj = j

    now_i = xi
    now_j = xj

    corners = find_all_corner(whole_arr)  # 전체 분기점 찾기

    while now_i > 0:
        whole_arr[now_i][now_j] = 0
        [now_i, now_j] = find_next_corner(now_i, now_j, corners)  # 분기점에서 이어진 분기점으로 이동
        now_i -= 1  # 분기점 사이에서 무한으로 좌우좌우 움직일 것을 방지하여 바로 한 칸 위로 이동

    return now_j-1  # 위에서 행렬을 0으로 둘러싸서 인덱스가 밀렸기 때문에 1을 빼줘야 함


def find_all_corner(whole_arr):  # 모든 분기점 찾아주는 함수
    corners = []
    for i in range(1, 101):
        for j in range(1, 101):
            count = 0
            if whole_arr[i][j] == 1:  # 현재 위치 중 1인 곳에서 상하좌우 중 3면이 1인 곳의 좌표를 분기점으로 저장
                if whole_arr[i][j + 1] == 1:
                    count += 1
                if whole_arr[i][j - 1] == 1:
                    count += 1
                if whole_arr[i + 1][j] == 1:
                    count += 1
                if whole_arr[i - 1][j] == 1:
                    count += 1
            if count >= 3:
                corners += [[i, j]]
    return corners


def find_index(element, array):

    idx = 0
    for ele in array:
        if ele == element:
            return idx
        else:
            idx += 1


def find_next_corner(now_i, now_j, corners):  # 현재 위치, 모든 분기점을 받아서 분기점에서 다음 갈 곳을 찾아주는 함수
    if [now_i, now_j] in corners:  # 현재 위치가 분기점이라면

        idx_corner = find_index([now_i, now_j], corners)
        # idx_corner = corners.index([now_i, now_j])  # 분기점의 인덱스를 받아서 이어진 분기점으로 이동 후 현재 위치 반환

        if idx_corner % 2 == 1:
            [new_now_i, new_now_j] = corners[idx_corner - 1]
        else:
            [new_now_i, new_now_j] = corners[idx_corner + 1]
    else:  # 현재 위치가 분기점이 아니라면 현재 위치 그대로 반환
        [new_now_i, new_now_j] = [now_i, now_j]

    return [new_now_i, new_now_j]


def find_ladder_self(ladder):
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

    result = find_ladder_w_hj(arr)
    # result = find_ladder_self(arr)

    print(f'#{test_case} {result}')
