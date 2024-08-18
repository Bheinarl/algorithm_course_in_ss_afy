def f1(n, arr):
    stack1 = []
    lst1 = []
    for i in range(n):
        if arr[i] == '*' or arr[i] == '/':  # *, / 는 무조건 스택에 쌓는다.
            stack1.append(arr[i])

        elif arr[i] == '+' or arr[i] == '-':
            j = len(stack1)
            while j >= 0:
                if stack1:  # 스택에 존재한다면
                    yeon_san_ja = stack1.pop()
                    j = len(stack1)

                    if yeon_san_ja == '+' or yeon_san_ja == '-':  # +, -가 나오면 스택에 쌓고 pop 한 것은 lst 에 넣는다.
                        lst1.append(yeon_san_ja)
                        stack1.append(arr[i])
                        break  # while 문

                    else:  # pop 했을 때 *, /가 나오면 lst 에 넣는다.
                        lst1.append(yeon_san_ja)

                else:  # 스택에 아무것도 없으면 무조건 스택에 넣는다.
                    stack1.append(arr[i])
                    break  # while 문
        else:  # 숫자가 나오면 무조건 lst 에 넣는다.
            lst1.append(arr[i])

    while len(stack1) > 0:  # 다 끝났는데 스택에 무언가가 남아있다면 다 lst 에 넣는다.
        res = stack1.pop()
        lst1.append(res)

    return lst1


def f2(n, arr):
    stack2 = []

    for i in range(n):
        if arr[i] in ['+', '-', '*', '/']:  # 연산자라면
            b = int(stack2.pop())  # 숫자 2개를 순서를 지켜서 pop 하고
            a = int(stack2.pop())
            if arr[i] == '+':  # + 라면 두 개 더해서 스택에 넣는다.
                ans = a + b
                stack2.append(ans)
            elif arr[i] == '-':  # - 라면 두 개 빼서 스택에 넣는다.
                ans = a - b
                stack2.append(ans)
            elif arr[i] == '*':  # * 라면 두 개 곱해서 스택에 넣는다.
                ans = a * b
                stack2.append(ans)
            elif arr[i] == '/':  # / 라면 두 개 나눠서 스택에 넣는다.
                ans = a / b
                stack2.append(ans)
        else:  # 숫자라면 스택에 무조건 넣는다.
            stack2.append(arr[i])

    if stack2:  # 계산 다 끝났는데 스택에 남아있다면 그 스택에 남아있는 것이 계산 결과이다. (오류가 없다면)
        result = stack2.pop()

    return result


for TEST_CASE in range(1, 11):

    N = int(input())
    ARR = input()

    LST = f1(N, ARR)
    RESULT = f2(N, LST)

    print(f'#{TEST_CASE} {RESULT}')
