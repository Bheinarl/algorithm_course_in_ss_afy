hex2bin = {'0': [0, 0, 0, 0],
           '1': [0, 0, 0, 1],
           '2': [0, 0, 1, 0],
           '3': [0, 0, 1, 1],
           '4': [0, 1, 0, 0],
           '5': [0, 1, 0, 1],
           '6': [0, 1, 1, 0],
           '7': [0, 1, 1, 1],
           '8': [1, 0, 0, 0],
           '9': [1, 0, 0, 1],
           'A': [1, 0, 1, 0],
           'B': [1, 0, 1, 1],
           'C': [1, 1, 0, 0],
           'D': [1, 1, 0, 1],
           'E': [1, 1, 1, 0],
           'F': [1, 1, 1, 1]}


def ratio_password(password_arr):  # 비율 계산해서 숫자 찾는 함수

    min_num = min(password_arr)  # 가장 작은 값으로 비율 계산  비율상 1에 해당하는 부분이 뒤 3자리 안에 존재
    for v in range(len(password_arr)):
        password_arr[v] //= min_num

    if password_arr == [2, 1, 1]:
        password_digit = 0
    elif password_arr == [2, 2, 1]:
        password_digit = 1
    elif password_arr == [1, 2, 2]:
        password_digit = 2
    elif password_arr == [4, 1, 1]:
        password_digit = 3
    elif password_arr == [1, 3, 2]:
        password_digit = 4
    elif password_arr == [2, 3, 1]:
        password_digit = 5
    elif password_arr == [1, 1, 4]:
        password_digit = 6
    elif password_arr == [3, 1, 2]:
        password_digit = 7
    elif password_arr == [2, 1, 3]:
        password_digit = 8
    elif password_arr == [1, 1, 2]:
        password_digit = 9

    return password_digit


def password_check(lst):  # 옳은 암호인지 판단하는 함수
    pw_lst = 0
    for q in range(8):
        if q % 2 == 0:
            pw_lst += 3 * lst[q]
        else:
            pw_lst += lst[q]

    if pw_lst % 10 == 0:
        return sum(lst)
    else:
        return 0


T = int(input())
for TEST_CASE in range(1, T + 1):
    N, M = map(int, input().split())
    ARR = []

    for _ in range(N):
        ARR += [list(input())]

    binary_arr = [[] * M for _ in range(N)]

    for i in range(N):  # 이진수로 다 바꿔 엄청 크지만..
        for j in range(M):
            binary_arr[i] += hex2bin[ARR[i][j]]

    counts_num = []
    ans_arr = []
    password_sum = 0
    password_history = []
    for p in range(N):
        counts_change_num = 0
        counts_same_num = 0

        if 1 not in binary_arr[p]:  # 암호가 없는 행은 확인하지 않는다.
            continue

        for q in range(len(binary_arr[p]) - 1, -1, -1):  # 뒤에서부터 확인하면서
            if counts_change_num == 0 and binary_arr[p][q] == 1:  # 암호의 시작부분이라면
                counts_change_num = 1  # 숫자가 바뀌는 부분 표시
                counts_same_num = 1  # 같은 숫자 개수 count
                continue

            if counts_change_num != 0:  # 암호가 시작했다면
                if binary_arr[p][q] == binary_arr[p][q + 1]:  # 앞에서 본 숫자와 같으면
                    counts_same_num += 1  # 같은 숫자 개수 +1
                else:  # 다르다면
                    counts_num = [counts_same_num] + counts_num  # 얼마나 같은 숫자가 나왔는지 기록
                    counts_change_num += 1  # 숫자 바뀌었다고 표시
                    counts_same_num = 1  # 같은 숫자 개수 초기화

            # 글자가 3번 바뀌었으면
            # (암호문에 있는 맨 앞의 0은 생략해도 무관하다. 비율상 망가지는 것도 없고, 오히려 있으면 시작과 끝 판단 힘듦)
            if counts_change_num == 4:
                password_txt = ratio_password(counts_num)  # 비율 계산해서 숫자 해독해주는 함수
                ans_arr = [password_txt] + ans_arr  # 해독한 숫자 맨 앞으로 기록
                counts_num = []  # 초기화
                counts_change_num = 0  # 초기화
                counts_same_num = 0  # 초기화

            # 앞에서 사용한 암호가 아니고 해독한 숫자가 8개가 된다면 옳은 암호인지 판단
            if ans_arr not in password_history and len(ans_arr) == 8:
                password_sum += password_check(ans_arr)  # 옳은 비밀번호면 더하자 (아니여도 0이여서 더해봤자긴 함)
                password_history += [ans_arr]  # 이전에 사용한 비밀번호라고 기록
                ans_arr = []
            elif ans_arr in password_history:  # 이전에 사용한 비밀번호면 초기화
                ans_arr = []

    print(f'#{TEST_CASE} {password_sum}')