T = int(input())
for TEST_CASE in range(1, T+1):
    num2 = list(input())
    num3 = list(input())

    N2 = len(num2)
    N3 = len(num3)

    miss_num2 = 0  # 실수한 2진수 값
    miss_num3 = 0  # 실수한 3진수 값

    i = N2-1
    n2 = 0
    num2_diff = []
    while i >= 0:
        if num2[i] == '0':  # 0이 실수면 더해야함
            num2_diff += [2**n2]
        else:  # 1이 실수면 뺴줘야 함
            num2_diff += [(-1) * 2**n2]
            miss_num2 += 2**n2
        n2 += 1
        i -= 1

    j = N3-1
    n3 = 0
    num3_diff = []
    while j >= 0:
        if num3[j] == '0':  # 0이 실수면 자릿수를 더하거나(1이 되야되거나) 2*자릿수를 더하거나 (2가 되야되거나)
            num3_diff += [3**n3]
            num3_diff += [2 * 3**n3]
        elif num3[j] == '1':  # 1이 실수면 자릿수를 빼주거나(0이 되야되거나) 자릿수를 더해주거나 (2가 되야되거나)
            num3_diff += [(-1) * 3**n3]
            num3_diff += [3**n3]
            miss_num3 += 3**n3
        else:  # 2가 실수면 2*자릿수를 빼주거나(0이 되야되거나) 자릿수를 빼주거나 (1이 되야되거나)
            num3_diff += [(-1) * 3**n3]
            num3_diff += [(-2) * 3**n3]
            miss_num3 += 2 * 3**n3
        n3 += 1
        j -= 1

    for p in range(len(num2_diff)):
        for q in range(len(num3_diff)):
            if miss_num2 + num2_diff[p] == miss_num3 + num3_diff[q]:  # 각각의 실수가 맞물려서 같은 수가 되었을 때
                origin_num = miss_num2 + num2_diff[p]

    print(f'#{TEST_CASE} {origin_num}')
