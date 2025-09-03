# 시간이 되돌아간다면 True 아니면 False 반환 함수
def has_negative_cycle(n, edges):
    dist = [0] * (n + 1)

    # 정점 수만큼 완화 시도
    for i in range(1, n + 1):
        is_negative = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
                # n번째 까지도 갱신된다면 음수 사이클 존재
                # 원래는 n-1번째에서 끝나야되는데 안끝나니깐 음수 사이클이 있다는 뜻
                if i == n:
                    return True
        if not is_negative:
            return False


T = int(input().strip())
out_lines = []
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []
    # 도로 - 양방향, +t
    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    # 웜홀 - 단방향, -t
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    ans = has_negative_cycle(N, edges)

    if ans:
        print("YES")
    else:
        print("NO")
