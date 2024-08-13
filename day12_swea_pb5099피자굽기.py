def f(n, m, arr):

    front = 0
    # 크기 n짜리 [0]을 만들어
    circle_Q = [0] * n  # 피자 넣을 화로
    idx = [0] * n  # 몇 번째 피자인지 알려주는 인덱스 list

    # 피자를 하나씩 넣어
    i = 0
    while True:

        while i < m:
            if circle_Q[front] == 0:  # 도달했는데 1이면 0으로 바꾸고 다음 피자를 넣어
                circle_Q[front] = arr[i]
                idx[front] = i+1
                i += 1
                front = (front+1) % n
            if 0 not in circle_Q:  # 화로가 가득 차있다면
                break  # while i < m 의 break

        if circle_Q[front] == 1:  # 1로 들어왔으면 이제 완성된 피자니까 빼
            circle_Q[front] = 0
            idx[front] = -1
            if i < m:  # 아직 넣을 피자가 남아있다면 피자를 넣어
                circle_Q[front] = arr[i]
                idx[front] = i+1
                i += 1
        else:  # (front+1) % m 해서 해당 인덱스가 되면 치즈 반을 줄여
            circle_Q[front] //= 2

        front = (front+1) % n

        if i == m and sum(circle_Q) == 1:  # 피자가 다 화로에 들어갔고, (완성 직전의) 1개만 남아있다면 끝
            break  # while True의 Break

    for i in range(n):
        if idx[i] != -1:  # 남아있는 인덱스가 마지막 피자
            return idx[i]


T = int(input())
for TEST_CASE in range(1, T+1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))

    RESULT = f(N, M, ARR)

    print(f'#{TEST_CASE} {RESULT}')
