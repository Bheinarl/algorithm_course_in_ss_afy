def calculate(a, b, oper_num):
    if oper_num == 0:
        return a + b
    elif oper_num == 1:
        return a - b
    elif oper_num == 2:
        return a * b
    elif oper_num == 3:
        return int(a/b)


def f(i, ans):
    global min_sum
    global max_sum

    if i == N-1:

        if ans > max_sum:
            max_sum = ans

        if ans < min_sum:
            min_sum = ans

    else:
        for j in range(4):
            if oper[j] != 0:
                oper[j] -= 1
                f(i+1, calculate(ans, ARR[i+1], j))
                oper[j] += 1


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    oper = list(map(int, input().split()))

    ARR = list(map(int, input().split()))
    max_sum = -100000000
    min_sum = 100000000
    tmp = ARR[0]

    f(0, tmp)

    print(f'#{TEST_CASE} {max_sum - min_sum}')
