def forth(arr):
    stack = []
    for txt in arr:
        if txt == '+':
            if len(stack) >= 2:  # stack 에 pop 할 2개 이상의 원소가 있다면 덧셈 진행
                c = stack.pop()
                b = stack.pop()
                d = b + c
                stack.append(d)  # 결과 push
            else:  # 그렇지 않다면 error 반환
                return 'error'
        elif txt == '-':
            if len(stack) >= 2:  # stack 에 pop 할 2개 이상의 원소가 있다면 뺄셈 진행
                c = stack.pop()
                b = stack.pop()
                d = b - c
                stack.append(d)  # 결과 push
            else:  # 그렇지 않다면 error 반환
                return 'error'
        elif txt == '*':
            if len(stack) >= 2:  # stack 에 pop 할 2개 이상의 원소가 있다면 곱셈 진행
                c = stack.pop()
                b = stack.pop()
                d = b * c
                stack.append(d)  # 결과 push
            else:  # 그렇지 않다면 error 반환
                return 'error'
        elif txt == '/':
            if len(stack) >= 2:  # stack 에 pop 할 2개 이상의 원소가 있다면 나눗셈 진행
                c = stack.pop()
                b = stack.pop()
                d = b // c
                stack.append(d)  # 결과 push
            else:  # 그렇지 않다면 error 반환
                return 'error'
        elif txt == '.':
            if len(stack) == 1:  # stack 에 1개만 남아 있어야 정상 작동해서 반환
                return stack[0]
            else:  # 그렇지 않으면 error 반환
                return 'error'
        else:  # 연산자가 아닌 숫자라면 stack 에 숫자 append
            stack += [int(txt)]


T = int(input())
for TC in range(1, T+1):
    ARR = input().split()  # ['1', '+', ... ]

    result = forth(ARR)

    print(f'#{TC} {result}')
