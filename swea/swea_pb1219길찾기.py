def dfs():
    stack = []
    visited = [0] * 101
    now_v = 0
    visited[now_v] = 1

    result = 0
    while True:
        if now_v == 99:  # 현재 위치가 종점에 도달하면 1 반환하고 종료
            return 1
        else:
            for w in adjL[now_v]:  # 가야할 곳 순회
                if visited[w] == 0:  # 아직 한 번도 안가본 정점이라면
                    stack.append(now_v)  # 내 위치를 stack 에 저장
                    now_v = w  # 내 위치 옮기고
                    visited[now_v] = 1  # 가본 적 있다고 표시
                    break  # for w 구문 break
            else:
                if stack:  # stack 이 비어있지 않다면
                    now_v = stack.pop()  # 내 위치를 전 위치로 변경, stack 에서 현재 위치는 제외
                else:
                    break  # while 구문 break  stack 이 비어있는데 갈 곳이 없으면 가는 길이 없는 것

    return result  # 길이 없으면 0 반환


for _ in range(10):
    test_case, E = map(int, input().split())
    adjL = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)

    RESULT = dfs()

    print(f'#{test_case} {RESULT}')
