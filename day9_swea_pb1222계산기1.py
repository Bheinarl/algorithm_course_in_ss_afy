for TC in range(1, 11):
    n = int(input())
    txt = input()
    words = ''
    stack_1 = []

    while True:  # 후위표현법으로 계산식 표현 - words
        for alpha in txt:  # input 값을 순회하면서
            if alpha == '+':  # 연산자 + 라면
                if stack_1:  # 스택이 비어있지 않다면
                    sanja = stack_1.pop()  # 기존에 있던 연산자를 꺼내서 계산
                    words += sanja  # words 에 추가

                stack_1.append(alpha)  # 현재 연산자 stack 에 저장

            else:  # 연산자가 아닌 숫자라면
                words += alpha  # words 에 숫자 추가
        else:  # 다 순회하였는데
            for _ in range(len(stack_1)):  # stack 에 남아있다면
                sanja = stack_1.pop()  # stack 에 있는 것 모두 words 에 추가
                words += sanja
        break

    stack_2 = []
    while True:  # 후위표현법으로 된 계산식을 계산
        for t in words:
            if t != '+':  # 숫자라면
                stack_2.append(t)  # stack 에 저장
            else:  # 연산자라면
                b = int(stack_2.pop())  # 순서에 맞게 2개를 꺼내서
                a = int(stack_2.pop())
                c = a + b  # 연산
                stack_2.append(c)  # 연산한 값 다시 stack 에 저장
        else:  # 다 순회하였는데
            for _ in range(len(stack_2)):  # stack 에 남아있다면
                ans = stack_2.pop()  # 다 출력

        break

    print(f'#{TC} {ans}')
