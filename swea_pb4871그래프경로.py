def dfs(sp, ep, v):
    visited = [0] * (v+1)
    stack = []
    visited[sp] = 1
    now_v = sp
    result = 0

    while True:
        if visited[ep] == 1:  # 목적 정점에 도달하면 1 반환
            return 1
        else:
            for w in adjL[now_v]:  # 갈 수 있는 길 순회
                if visited[w] == 0:  # 아직 간 적 없는 길이라면
                    stack.append(now_v)  # 내 위치 저장(push)
                    now_v = w  # 위치 이동
                    visited[w] = 1  # 방문한 적 있다고 표시
                    break  # for w 구문 break
            else:  # for 구문 전체를 다 순회하였다면
                if stack:  # stack 이 비어있지 않다면 (True)
                    now_v = stack.pop()  # stack 에서 pop(전 위치로 돌아감)
                else:  # stack 이 비어있다면
                    break  # while 구문 break

    return result  # 전체를 다 순회하였는데 목적 정점에 도달하지 못하였다면 0 반환


T = int(input())
for TC in range(1, T+1):
    V, E = map(int, input().split())

    adjL = [[] for _ in range(V + 1)]
    for i in range(E):
        V1, V2 = map(int, input().split())
        adjL[V1].append(V2)   # 단방향 그래프이므로 가는 길만 저장
        # adjL[V2].append(V1)   양방향 그래프면 다시 돌아오는 길이 있어야 하지만
    SP, EP = map(int, input().split())

    RESULT = dfs(SP, EP, V)

    print(f'#{TC} {RESULT}')
