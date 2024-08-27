def f(n):  # n은 노드 번호

    global ARR  # 프린트할 list

    if n == 0:  # 자식 노드가 없다면
        return
    else:                # 중위 순회
        f(child_L[n])    # 왼쪽 자식 노드
        ARR += txt[n-1]  # 해당 인덱스 순서의 글자를 삽입
        f(child_R[n])    # 오른쪽 자식 노드


for TEST_CASE in range(1, 11):
    N = int(input())

    txt = []
    ARR = []

    child_L = [0] * (N+1)
    child_R = [0] * (N+1)

    for i in range(N):
        lst = list(input().split())
        txt += [lst[1]]  # 입력 순서대로 글자 저장
        lst[0] = int(lst[0])

        if len(lst) == 4:  # 길이가 4면
            child_L[lst[0]] = int(lst[2])  # 왼쪽 자식 노드에 추가
            child_R[lst[0]] = int(lst[3])  # 오른쪽 자식 노드에 추가
        elif len(lst) == 3:  # 길이가 3이면
            child_L[lst[0]] = int(lst[2])  # 왼쪽 자식 노드에 추가

    f(1)  # 1번 노드부터 시작합니다~

    print(f'#{TEST_CASE}', end=' ')
    for j in range(N):
        print(ARR[j], end='')
    print()
