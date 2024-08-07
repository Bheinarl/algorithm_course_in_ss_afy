def f(txt):
    stack = [0] * len(txt)
    top = -1

    for i in txt:
        if i == '(' or i == '{':  # '(' or '{' 를 받았을 때
            top += 1
            stack[top] = i  # stack 에 저장  push()
        elif i == ')':  # ')' 를 받았을 때
            if stack[top] != '(':  # 전 괄호가 '('가 아니라면
                return 0  # 오류
            else:
                top -= 1  # 전 괄호가 '('라면 pop()
        elif i == '}':  # '}' 를 받았을 때
            if stack[top] != '{':  # 전 괄호가 '{'가 아니라면
                return 0  # 오류
            else:
                top -= 1  # 전 괄호가 '{'라면 pop()

    if top == -1:  # 끝까지 순회했을 때 괄호가 남아있지 않다면
        return 1  # 1 반환
    else:
        return 0  # 남아있다면 오류


T = int(input())
for tc in range(1, T + 1):
    TXT = input()

    result = f(TXT)

    print(f'#{tc} {result}')
