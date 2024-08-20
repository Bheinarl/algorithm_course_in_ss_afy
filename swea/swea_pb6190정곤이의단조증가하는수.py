def f1():
    lst_ele_multiple = []

    for i in range(N-1):
        for j in range(i+1, N):
            lst_ele_multiple += [ARR[i]*ARR[j]]

    return lst_ele_multiple


def f2(num):

    num = str(num)

    for p in range(len(num)-1):
        if num[p] > num[p+1]:
            return 0
    else:
        return 1


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))
    max_mlt = -1

    lst_ele_multi = f1()  # nC2 해서 곱 구하는 함수

    for number in lst_ele_multi:
        T_F = f2(number)  # 단조 증가하는 수인가를 찾는 함수
        if T_F == 1 and max_mlt < number:
            max_mlt = number

    print(f'#{TEST_CASE} {max_mlt}')
