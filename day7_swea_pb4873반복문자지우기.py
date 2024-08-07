def f(txt):

    stack = [0] * len(txt)
    top = -1

    for i in range(len(txt)):

        top += 1

        stack[top] = txt[i]  # push() 한 번

        if txt[i] == stack[top-1]:  # 앞 문자와 중복되면 pop() 두 번
            top -= 2

        if -1 > top or top > len(txt)-1:  # 인덱스를 벗어나면 -1 반환
            return -1

    if top != -1:  # 글자가 남으면
        return top+1  # 남은 글자 수 반환
    else:  # 글자가 남지 않으면
        return 0  # 0 반환


T = int(input())
for tc in range(1, T+1):
    TXT = input()

    result = f(TXT)

    print(f'#{tc} {result}')
