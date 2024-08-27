def f(n):
    global counts
    if n == 0:
        return
    else:
        counts += 1
        f(child_1[n])
        f(child_2[n])


T = int(input())
for TEST_CASE in range(1, T+1):
    E, N = map(int, input().split())
    ARR = list(map(int, input().split()))

    max_node = max(ARR)
    child_1 = [0] * (max_node + 1)
    child_2 = [0] * (max_node + 1)

    for i in range(E):
        if child_1[ARR[2 * i]] == 0:  # left 가 비어있으면 left 에 삽입
            child_1[ARR[2 * i]] = ARR[2 * i + 1]
        else:  # left 가 비어있지 않다면 right 에 삽입
            child_2[ARR[2 * i]] = ARR[2 * i + 1]

    counts = 0
    f(N)

    print(f'#{TEST_CASE} {counts}')


"""
T = int(input())
for TEST_CASE in range(1, T+1):
    E, N = map(int, input().split())
    ARR = list(map(int, input().split()))

    max_node = max(ARR)
    child_1 = [0] * (max_node + 1)
    child_2 = [0] * (max_node + 1)

    for i in range(E):
        if child_1[ARR[2 * i]] == 0:  # left 가 비어있으면 left 에 삽입
            child_1[ARR[2 * i]] = ARR[2 * i + 1]
        else:  # left 가 비어있지 않다면 right 에 삽입
            child_2[ARR[2 * i]] = ARR[2 * i + 1]

    counts = 1
    stack = []

    while True:
        if child_1[N] == 0 and child_2[N] == 0 and stack == []:
            break

        elif child_1[N] == 0 and child_2[N] == 0:
            pass

        if child_1[N] != 0:
            stack.append(child_1[N])

        if child_2[N] != 0:
            stack.append(child_2[N])

        if stack == 0:
            break
        N = stack.pop(0)
        counts += 1

    print(f'#{TEST_CASE} {counts}')
"""