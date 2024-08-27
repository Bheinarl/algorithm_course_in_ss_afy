def f(n):  # n은 노드 번호
    global idx  # idx 는 노드 안에 넣을 숫자

    if n == 0:  # 자식 노드가 없다면
        return
    else:              # 중위 순회
        f(child_L[n])  # 왼쪽 자식 노드
        ARR[n] = idx   # 본인 노드에 숫자 넣고
        idx += 1       # 다음 숫자로
        f(child_R[n])  # 오른쪽 자식 노드


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())

    ARR = [0] * (N+1)

    child_L = [0] * (N+1)
    child_R = [0] * (N+1)

    for i in range(1, N+1):  # 경로를 다 세팅해 놓자
        if 2 * i <= N:
            child_L[i] = 2 * i

        if 2 * i + 1 <= N:
            child_R[i] = 2 * i + 1

        if 2 * i > N and 2 * i + 1 > N:
            break

    idx = 1
    f(1)  # 1번 노드부터 시작

    ans_1 = ARR[1]
    ans_2 = ARR[N//2]

    print(f'#{TEST_CASE} {ans_1} {ans_2}')
