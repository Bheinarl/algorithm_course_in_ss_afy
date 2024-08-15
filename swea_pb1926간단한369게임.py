N = int(input())

for i in range(1, N+1):  # 1 ~ N
    if '3' in str(i) or '6' in str(i) or '9' in str(i):  # string 일때 3, 6, 9가 있다면
        i = str(i)  # i를 string 으로 바꿔서
        for j in range(len(i)):  # 글자 수만큼 순회해서
            if i[j] in ['3', '6', '9']:  # 3, 6, 9가 나오면 - 을 출력
                print('-', end='')  # - 을 출력
        print(' ', end='')  # 다 순회해서 숫자 끝났으면 띄어쓰기

    else:  # 3, 6, 9가 없으면
        print(i, end=' ')  # int i를 출력하고 띄어쓰기