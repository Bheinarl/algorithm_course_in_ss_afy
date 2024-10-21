# find 연산
# 연결고리를 만들어줘요 누구랑 누구랑 연결되어 있는지
def find_parent(parent, x):  # 끝까지 조사해서 누구랑 연결되어있는지 조사를 해
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union_연산
# 우리가 선을 정하는 느낌이라서 어느 비용낮은 길을 고를건지, 고른 후 연결까지
def union_parent(parent, a, b):
    a = find_parent(parent, a)  # a의 맨 위가 누구인지
    b = find_parent(parent, b)  # b의 맨 위가 누구인지
    if a < b:  # 최소한의 값을 부모노드로 설정하고 하는 작업
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
LST = [list(map(int, input().split())) for _ in range(N)]
connecting = [n for n in range(N+1)]  # 연결 관계를 쓸려고 했는데 생각해보니 필요가 없넹 다 연결되어있네 그래서 연결고리로 바꿈
connecting_value = []  # 좌표와 연결값을 담을 list

for i in range(N):
    for j in range(N):
        if i < j:  # 굳이 반을 볼 필요가 없어요
            connecting_value.append((i, j, LST[i][j]))  # 담아

connecting_value.sort(key=lambda x: x[2])  # 최소 가중치로 정렬

counts = 0
cost = 0
for planet_i, planet_j, value in connecting_value:
    if find_parent(connecting, planet_i) != find_parent(connecting, planet_j):  # 길이 없나요? 그럼 길을 연결해 이게 가장 싸
        union_parent(connecting, planet_i, planet_j)  # 길 만들어줍시다
        cost += value  # 값을 저장하고
        counts += 1  # 길 갯수 추가하고
        if counts == N-1:  # ex) 행성이 3개면 길은 2개면 된다. 그럼 더 만들 필요가 없지
            break

print(cost)