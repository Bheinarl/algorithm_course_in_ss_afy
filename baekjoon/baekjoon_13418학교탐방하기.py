import heapq
import sys
input = sys.stdin.readline

def MST(graph):
    visited=[True]+[False]*(N)
    q=graph[0]
    heapq.heapify(q)
    result=0
    while q:
        Z, X = heapq.heappop(q)
        if not visited[X]:
            visited[X] = True
            result += Z
            for j in graph[X]:
                if not visited[j[1]]:
                    heapq.heappush(q,j)

    return result


N, M = map(int, input().split())

max_graph = [[] for _ in range(N+1)]
min_graph = [[] for _ in range(N+1)]

for i in range(M + 1):
    a, b, c = map(int, input().split())
    if c == 0:  # 오르막길일 때를 생각하는 건데

        # max 에서는 오르막길을 최대한 포함시키려고 가중치를 0으로 설정 (sort 쓰면 앞으로 가지니깐)
        max_graph[a].append((0, b))
        max_graph[b].append((0, a))

        # min 에서는 오르막길을 최대한 포함시키지 않으려고 가중치를 1로 설정 (sort 쓰면 뒤로 가지니깐)
        min_graph[a].append((1, b))
        min_graph[b].append((1, a))

    else:  # 내리막길일 때를 생각하는 건데

        # max 에서는 내리막길을 최대한 포함시키지 않으려고 가중치를 1로 설정 (sort 쓰면 뒤로 가지니깐)
        max_graph[a].append((1, b))
        max_graph[b].append((1, a))

        # min 에서는 내리막길을 최대한 포함시키려고 가중치를 0으로 설정 (sort 쓰면 앞으로 가지니깐)
        min_graph[a].append((0, b))
        min_graph[b].append((0, a))


# 가능한 한 많은 오르막길을 사용했을때의 최대 피로도
# N은 모든 도로가 오르막길일때 최대 피로도이고,
# MST(max_graph)는 오르막길 + 내리막길이 섞였지만 최소한의 길을 찾아가는 것
# 근데 우리가 구하고 싶은거는 그냥 오르막길을 잔뜩 올라가면 그게 최악이 되는거니깐
# 그 최악을 구해야한다
max_fatigue = (N - MST(max_graph))**2
min_fatigue = MST(min_graph)**2

print(max_fatigue - min_fatigue)