def f1(arr):  # 어디서부터 어디까지가 암호인지 알려주는 함수
    sp_arr = []
    ep_arr = []
    a = 0
    b = 0

    while True:

        while a < M:
            if arr[a] != '0':
                sp_arr += [a]
                b = a
                break
            else:
                a += 1

        if a == M:
            break

        while b < M-1:
            if arr[b] != '0' and arr[b+1] == '0' :
                ep_arr += [b]
                a = b + 1
                break
            else:
                b += 1

    return sp_arr, ep_arr


def f2(arr, sp, ep):  # 16진수 암호를 2진수로 바꿔주는 함수
    code = ''
    for i in range(sp, ep):
        code += arr[i]

    password_lst = list(bin(int(code, 16))[2:])

    while password_lst[-1] == '0':
        password_lst.pop()

    password = ''
    for u in range(len(password_lst)):
        password += password_lst[u]

    return password


def f3(pw):  # 받은 2진수 값을 비율 따져서 암호로 바꿔주는 함수
    ratio_01 = []
    counts = 1

    for i in range(1, len(pw)):
        if pw[i] == pw[i-1]:
            counts += 1
        else:
            ratio_01 += [counts]
            counts = 1
    else:
        ratio_01 += [counts]

    min_num = min(ratio_01)
    for v in range(len(ratio_01)):
        ratio_01[v] //= min_num

    ans_arr = []
    for j in range(8):
        password_arr = ratio_01[j*4:j*4+4]
        if password_arr == [3, 2, 1, 1]:
            password_digit = 0
        elif password_arr == [2, 2, 2, 1]:
            password_digit = 1
        elif password_arr == [2, 1, 2, 2]:
            password_digit = 2
        elif password_arr == [1, 4, 1, 1]:
            password_digit = 3
        elif password_arr == [1, 1, 3, 2]:
            password_digit = 4
        elif password_arr == [1, 2, 3, 1]:
            password_digit = 5
        elif password_arr == [1, 1, 1, 4]:
            password_digit = 6
        elif password_arr == [1, 3, 1, 2]:
            password_digit = 7
        elif password_arr == [1, 2, 1, 3]:
            password_digit = 8
        elif password_arr == [3, 1, 1, 2]:
            password_digit = 9
        else:
            return -1

        ans_arr += [password_digit]

        if len(ans_arr) != 8:
            return -1

    return ans_arr


def f4(lst):
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
    PASSWORD_sum = 0

    for _ in range(N):
        ARR += [list(input())]

    PW_history = []
    last_ARR = []
    for ARR_ARR in ARR:
        if last_ARR == ARR_ARR:
            continue
        else:
            last_ARR = ARR_ARR[:]

        if '1' in ARR_ARR or '2' in ARR_ARR or '3' in ARR_ARR or '4' in ARR_ARR or '5' in ARR_ARR or '6' in ARR_ARR or '7' in ARR_ARR or '8' in ARR_ARR or '9' in ARR_ARR or 'A' in ARR_ARR or 'B' in ARR_ARR or 'C' in ARR_ARR or 'D' in ARR_ARR or 'E' in ARR_ARR or 'F' in ARR_ARR:
            SP, EP = f1(ARR_ARR)
            for g in range(len(SP)):
                for h in range(len(EP)):
                    if SP[g] >= EP[h]:
                        continue

                    PW = f2(ARR_ARR, SP[g], EP[h])
                    if PW in PW_history:
                        continue
                    else:
                        PW_history += [PW]

                    while len(PW) % 56 != 0:
                        PW = '0' + PW

                    PW_LIST = f3(PW)
                    if PW_LIST == -1:
                        continue

                    PASSWORD_sum += f4(PW_LIST)

    print(f'#{TEST_CASE} {PASSWORD_sum}')
