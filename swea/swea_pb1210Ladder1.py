def find_start():
    for i in range(100):
        for j in range(100):
            if ARR[i][j] == 2:
                return i, j


def f(x, y):
    while x > 0:
        if y + 1 < 100 and ARR[x][y + 1] == 1:
            ARR[x][y] = 0
            y += 1
        elif 0 <= y - 1 and ARR[x][y - 1] == 1:
            ARR[x][y] = 0
            y -= 1
        else:
            x -= 1

    return y


for TEST_CASE in range(1, 11):
    tc = int(input())
    ARR = []
    for _ in range(100):
        ARR += [list(map(int, input().split()))]

    start_x, start_y = find_start()
    RESULT = f(start_x, start_y)

    print(f'#{TEST_CASE} {RESULT}')

"""
def find_ladder_w_hj(ladder):
    xi = 0
    xj = 0

    # 사다리에서 가로로 지나가야 하는 곳(이하 분기점) 찾는데 방해받지 않게 0으로 둘러싼 행렬 생성
    whole_arr = [[0] * (100 + 2)]
    for arr_in_arr in ladder:
        whole_arr += [[0] + arr_in_arr + [0]]
    whole_arr += [[0] * (100 + 2)]

    # whole_arr = [[0]*(N+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]

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

def find_ladder_hj(ladder):
    # 처음 시작 j 값
    first_j = []
    for j in range(1, 101):
        if ladder[0][j] == 1:
            first_j += [j - 1]
        if ladder[99][j] == 2:
            last_j = j - 1
            ladder[99][j] = 1000000000  # 분기점 파악할때 2 그대로면 더했을때 3인 경우가 생겨버림
    '''
    print(first_j)
    [0, 3, 12, 18, 20, 31, 37, 47, 57, 61, 67, 74, 81, 84, 93, 96]
    print(last_j)
    57
    '''

    # 0으로 둘러싸인 102*102 whole_arr 생성
    whole_arr = [[0] * 102]
    whole_arr += ladder
    whole_arr += [[0] * 102]

    # 분기점 목록 리스트 ic
    ic_total = []
    for i in range(1, 101):  # index 1~100 까지
        ic = []
        for j in range(1, 101):
            if whole_arr[i][j] == 1 and whole_arr[i][j + 1] + whole_arr[i][j - 1] + whole_arr[i + 1][j] + \
                    whole_arr[i - 1][j] == 3:
                ic += [j - 1]  # 실제 arr에서 j값은 j-1이니까
        ic_total += [ic]  # 어차피 j값만 필요함
    '''
    print(ic_total)
    [[], [81, 84], [3, 12, 84, 93], [12, 18, 57, 61], [47, 57, 93, 96], [0, 3, 18, 20, 61, 67, 84, 93], [57, 61, 67, 74], [18, 20], [31, 37, 57, 61, 84, 93], [3, 12, 81, 84], [96, 99], [20, 31, 67, 74], [12, 18], [0, 3, 31, 37, 47, 57], [61, 67], [81, 84], [57, 61], [0, 3, 74, 81], [], [12, 18, 67, 74], [0, 3, 31, 37, 61, 67, 93, 96], [12, 18], [], [12, 18, 84, 93], [31, 37, 96, 99], [], [31, 37, 57, 61, 96, 99], [93, 96], [], [18, 20, 31, 37], [12, 18, 61, 67], [57, 61, 67, 74, 96, 99], [20, 31, 84, 93], [81, 84], [], [37, 47, 57, 61, 81, 84], [74, 81], [31, 37, 67, 74], [3, 12, 84, 93], [12, 18, 57, 61], [], [0, 3], [20, 31], [31, 37, 47, 57, 61, 67, 84, 93], [20, 31, 37, 47, 74, 81, 93, 96], [0, 3, 47, 57], [18, 20, 57, 61], [37, 47, 74, 81], [61, 67], [], [12, 18, 74, 81], [20, 31, 37, 47, 81, 84, 96, 99], [], [3, 12, 81, 84], [12, 18, 61, 67, 96, 99], [18, 20, 47, 57, 67, 74, 81, 84], [0, 3, 57, 61, 74, 81], [12, 18, 84, 93, 96, 99], [57, 61, 67, 74], [0, 3, 20, 31, 61, 67], [3, 12, 31, 37, 47, 57], [0, 3, 12, 18, 67, 74, 93, 96], [18, 20, 57, 61, 74, 81, 84, 93], [20, 31, 37, 47], [47, 57, 61, 67, 93, 96], [37, 47, 57, 61], [81, 84], [96, 99], [84, 93], [81, 84], [], [31, 37, 74, 81], [], [12, 18, 57, 61], [47, 57, 81, 84], [20, 31, 84, 93], [18, 20, 61, 67], [57, 61], [93, 96], [12, 18, 57, 61, 67, 74], [84, 93], [12, 18, 20, 31, 61, 67], [0, 3, 37, 47], [84, 93, 96, 99], [74, 81], [37, 47], [47, 57], [31, 37, 61, 67, 93, 96], [37, 47, 57, 61, 74, 81], [], [61, 67], [20, 31, 74, 81], [81, 84, 93, 96], [3, 12, 74, 81], [81, 84, 93, 96], [57, 61, 67, 74, 96, 99], [37, 47, 81, 84], [84, 93], [12, 18, 37, 47, 57], []]
    # 실제 i값이 각각 0~99일 때 분기점들의 실제 j값을 모아둔 것. (1,81) (1,84) (2,3) (2,12) ...
    # 분기점은 순서대로 2개씩 연결되어 있음. in-out 순서 : 81-84 / 3-12, 84-93 / 12-18, ...
    '''
    pairs = []
    for sub_list in ic_total:
        for i in range(0, len(sub_list) - 1, 2):
            pairs += [[sub_list[i], sub_list[i + 1]]]
    '''
    print(pairs)
    [[81, 84], [3, 12], [84, 93], [12, 18], [57, 61], [47, 57], [93, 96], [0, 3], [18, 20], [61, 67], [84, 93], [57, 61], [67, 74], [18, 20], [31, 37], [57, 61], [84, 93], [3, 12], [81, 84], [96, 99], [20, 31], [67, 74], [12, 18], [0, 3], [31, 37], [47, 57], [61, 67], [81, 84], [57, 61], [0, 3], [74, 81], [12, 18], [67, 74], [0, 3], [31, 37], [61, 67], [93, 96], [12, 18], [12, 18], [84, 93], [31, 37], [96, 99], [31, 37], [57, 61], [96, 99], [93, 96], [18, 20], [31, 37], [12, 18], [61, 67], [57, 61], [67, 74], [96, 99], [20, 31], [84, 93], [81, 84], [37, 47], [57, 61], [81, 84], [74, 81], [31, 37], [67, 74], [3, 12], [84, 93], [12, 18], [57, 61], [0, 3], [20, 31], [31, 37], [47, 57], [61, 67], [84, 93], [20, 31], [37, 47], [74, 81], [93, 96], [0, 3], [47, 57], [18, 20], [57, 61], [37, 47], [74, 81], [61, 67], [12, 18], [74, 81], [20, 31], [37, 47], [81, 84], [96, 99], [3, 12], [81, 84], [12, 18], [61, 67], [96, 99], [18, 20], [47, 57], [67, 74], [81, 84], [0, 3], [57, 61], [74, 81], [12, 18], [84, 93], [96, 99], [57, 61], [67, 74], [0, 3], [20, 31], [61, 67], [3, 12], [31, 37], [47, 57], [0, 3], [12, 18], [67, 74], [93, 96], [18, 20], [57, 61], [74, 81], [84, 93], [20, 31], [37, 47], [47, 57], [61, 67], [93, 96], [37, 47], [57, 61], [81, 84], [96, 99], [84, 93], [81, 84], [31, 37], [74, 81], [12, 18], [57, 61], [47, 57], [81, 84], [20, 31], [84, 93], [18, 20], [61, 67], [57, 61], [93, 96], [12, 18], [57, 61], [67, 74], [84, 93], [12, 18], [20, 31], [61, 67], [0, 3], [37, 47], [84, 93], [96, 99], [74, 81], [37, 47], [47, 57], [31, 37], [61, 67], [93, 96], [37, 47], [57, 61], [74, 81], [61, 67], [20, 31], [74, 81], [81, 84], [93, 96], [3, 12], [74, 81], [81, 84], [93, 96], [57, 61], [67, 74], [96, 99], [37, 47], [81, 84], [84, 93], [12, 18], [37, 47]]
    '''

    '''
    first_j [0, 3, 12, 18, 20, 31, 37, 47, 57, 61, 67, 74, 81, 84, 93, 96] 여기서 출발해서
    사다리 0 - 3 - 12 - 18 - 12 ...
    사다리 3 - 12 - 18 - 20 - 18 ...
    사다리 12 - 2 - ...
    '''
    # find 인덱스로 시작하는 사다리의 결과값 인덱스 도출 - 결과값이 문제에서 찾는 last_j 라면 그게 답
    for first in first_j:
        i = 0
        find = first
        while i < len(pairs):
            if find == pairs[i][0]:
                find = pairs[i][1]
                i += 1
            elif find == pairs[i][1]:
                find = pairs[i][0]
                i += 1
            else:
                i += 1
        if find == last_j:
            return first


for _ in range(1, 11):

    test_case = int(input())
    arr = []

    for _ in range(100):
        arr += [list(map(int, input().split()))]

    result = find_ladder_w_hj(arr)
    # result = find_ladder_self(arr)

    print(f'#{test_case} {result}')
"""