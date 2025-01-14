import sys
from copy import deepcopy
from itertools import combinations

def start_round(archers, enemy_map, D):  # 궁수 위치를 정하면 그 위치에 대한 최댓값 구하는 함수
    temp_map = deepcopy(enemy_map)
    total_kills = 0

    while any(sum(row) for row in temp_map):  # 적이 남아있으면 (아직 순회가 덜 됨)
        total_kills += attack(archers, temp_map, D)  # 한 줄씩 적 죽이는 함수

        temp_map.pop()  # 맨 아래 줄 없애고
        temp_map.insert(0, [0] * M)  # 맨 위에 적 없는 배열 삽입

    return total_kills


def attack(archers, temp_map, D):  # 한 줄씩 처리해주는 함수
    attacked = set()  # 중복이 될 수 있으므로 set으로 하여 중복 제거

    for archer in archers:  # 각 궁수마다 처리해줄거임
        target = None
        min_distance = float('inf')

        for r in range(N - 1, -1, -1):
            for c in range(M):
                if temp_map[r][c] == 1:  # 적이 있다면
                    attack_range = abs(N - r) + abs(archer - c)  # 공격 사거리 설정
                    if attack_range <= D:  # 사정거리 안에 있는 적
                        # 더 가까운 적을 고르거나 거리가 같으면 왼쪽 적을 타겟으로 설정
                        if attack_range < min_distance or (attack_range == min_distance and c < target[1]):
                            target = (r, c)
                            min_distance = attack_range

        if target:  # 타겟으로 설정된 적이 있다면(사정거리 안에 적이 있다면)
            attacked.add(target)  # 타겟을 공격 대상으로 설정

    for r, c in attacked:
        temp_map[r][c] = 0  # 공격해서 죽여

    return len(attacked)  # 공격한 대상의 수를 반환


N, M, D = map(int, sys.stdin.readline().split())

enemy_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

archers_location = combinations(range(M), 3)

max_kills = 0
for archers in archers_location:
    kills = start_round(archers, enemy_map, D)
    max_kills = max(max_kills, kills)

print(max_kills)