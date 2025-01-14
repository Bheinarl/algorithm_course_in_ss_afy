import heapq
from collections import defaultdict

def dijkstra(start, road):  # start : 시작 마을
    time_cost_list = [float('inf')] * (N + 1)  # 각 마을까지의 최소 시간 초기화
    time_cost_list[start] = 0  # 시작 마을 -> 시작 마을 시간은 0
    Q = [(0, start)]  # 초기값 [(시간, 시작 마을)]

    while Q:
        current_time, current_town = heapq.heappop(Q)

        if current_time > time_cost_list[current_town]:  # 지금까지의 시간이 이전에 기록된 시간보다 오버되면 굳이 볼 필요없음
            continue

        for next_town, road_time in road[current_town]:  # 가고자하는 마을, 그 길의 시간
            time_cost = current_time + road_time
            if time_cost < time_cost_list[next_town]:  # 가고자하는 마을 길의 시간이 다음 마을의 결과(그때의 최소치)보다 작으면
                time_cost_list[next_town] = time_cost  # 최소 시간으로 갱신하고
                heapq.heappush(Q, (time_cost, next_town))  # q에 넣고

    return time_cost_list


N, M, X = map(int, input().split())
road = defaultdict(list)

for _ in range(M):
    a, b, t = map(int, input().split())
    road[a].append((b, t))  # 길 넣어. 근데 양방향 아니니깐 한 방향만.

x2home = dijkstra(X, road)  # X부터 마을까지 가는 길(다 저장된 list 형태)

max_time = 0
for i in range(1, N + 1):
    if i == X:
        continue  # X 자신에서 X로 가는 경로는 계산 불필요. 어차피 0임.
    home2x = dijkstra(i, road)[X]  # 출발 마을부터 계산
    if home2x == float('inf') or x2home[i] == float('inf'):  # 경로가 없는 경우 (초기 설정값과 동일)
        continue
    max_time = max(max_time, home2x + x2home[i])  # 그 중 최고

print(max_time)