import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

# 아이템 이름 ↔ 정수 인덱스 매핑을 위한 딕셔너리
name2num = dict()
num2name = dict()
idx = 0  # 아이템 ID 카운터

# 그래프 구조와 진입차수 테이블
connect_graph = defaultdict(list)  # id당 하위 아이템을 리스트로 묶어서 dict으로
count_buy_down = dict()  # id 당 하위 아이템이 필요한 갯수를 dict으로

# 관계 입력
for _ in range(N):
    a, b = input().split()  # a는 b보다 먼저 사야 함 (a → b)

    # 이름이 처음 등장한 경우 ID 부여 및 초기 설정
    for name in [a, b]:
        if name not in name2num:
            name2num[name] = idx
            num2name[idx] = name
            count_buy_down[idx] = 0
            idx += 1

    u = name2num[a]  # 선행 아이템 ID
    v = name2num[b]  # 후행 아이템 ID

    connect_graph[u].append(v)  # u → v 간선 추가
    count_buy_down[v] += 1     # v의 진입 차수 증가

# 초기 구매 가능한 아이템: count_buy_down가 0인 것들
# → 사전순 구매 위해 min-heap 사용
pq = []
for i in range(idx):
    if count_buy_down[i] == 0:
        heapq.heappush(pq, num2name[i])  # 이름 기준으로 넣는다 (heapq는 문자열 정렬 가능)

result = []         # 최종 구매 순서 결과 리스트
visited = set()     # 이미 구매한 아이템 ID 기록

# 위상 정렬 시작
while pq:
    this_turn = []  # 이번 라운드에 구매 가능한 아이템들

    # 현재 round에서 구매 가능한 모든 아이템 꺼내기
    while pq:
        name = heapq.heappop(pq)
        id = name2num[name]
        if id in visited:
            continue  # 중복 제거
        this_turn.append((name, id))
        visited.add(id)

    for name, id in this_turn:
        result.append(name)  # 최종 구매 목록에 추가

        # 현재 아이템과 연결된 다음 아이템들의 하위 아이템 사야되는 갯수 감소
        for next_id in connect_graph[id]:
            count_buy_down[next_id] -= 1
            if count_buy_down[next_id] == 0:
                # 이제 구매 가능한 상태 → pq에 추가
                heapq.heappush(pq, num2name[next_id])

# 모든 아이템을 구매했는지 확인
if len(result) != idx:
    print(-1)  # 사이클이 존재하여 일부 아이템 구매 불가
else:
    for name in result:
        print(name)
