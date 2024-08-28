for TEST_CASE in range(1, 11):
    N = int(input())

    child_L = [0] * (N+1)
    child_R = [0] * (N+1)

    ARR = [0] * (N+1)

    for _ in range(N):
        lst = list(input().split())
        lst[0] = int(lst[0])
        if len(lst) == 4:
            ARR[lst[0]] = lst[1]
            child_L[lst[0]] = int(lst[2])
            child_R[lst[0]] = int(lst[3])
        else:
            ARR[lst[0]] = int(lst[1])

    for i in range(N, 0, -1):  # 자식 왼쪽 오른쪽에 몇번 인덱스를 써야되는지 저장해놓고 연산자가 나오면 해당 인덱스의 숫자 가져다 쓰기
        if type(ARR[i]) is not int:
            if ARR[i] == '+':
                ARR[i] = ARR[child_L[i]] + ARR[child_R[i]]
            elif ARR[i] == '-':
                ARR[i] = ARR[child_L[i]] - ARR[child_R[i]]
            elif ARR[i] == '*':
                ARR[i] = ARR[child_L[i]] * ARR[child_R[i]]
            elif ARR[i] == '/':
                ARR[i] = ARR[child_L[i]] // ARR[child_R[i]]

    print(f'#{TEST_CASE} {ARR[1]}')
