from collections import defaultdict

N, M, K = map(int, input().split())

fireballs = []  # 파이어볼 정보 수집

# 방향은 순서대로 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(M):
    r, c, m, s, d =  map(int, input().split())
    fireballs.append((r-1, c-1, m, s, d))  # index는 0부터 시작

for _ in range(K):

    # 모든 파이어볼 이동
    new_fireballs_positions = defaultdict(list)  # 초기값을 []로 생성

    for r, c, m, s, d in fireballs:
        new_r = (r + directions[d][0] * s) % N
        new_c = (c + directions[d][1] * s) % N

        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:  # 격자 밖으로 나가면 제거
            continue

        new_fireballs_positions[(new_r, new_c)].append((m, s, d))
        # (1, 2) : [(3, 4, 5)]  1, 2 위치에 질량, 속도, 방향을 넣은 파이어볼 값으로 설정

    # 같은 칸에 있는 파이어볼
    fireballs = []
    for (r, c), fireball_infos in new_fireballs_positions.items():
        if len(fireball_infos) == 1:  # 그 위치에 파이어볼이 1개라면
            fireballs.append((r, c, *fireball_infos[0]))  # 원래 초기 정보처럼 저장

        else:  # 2개 이상이라면
            fireball_counts = len(fireball_infos)
            new_m = sum(fb[0] for fb in fireball_infos) // 5  # 질량 계산
            new_s = sum(fb[1] for fb in fireball_infos) // fireball_counts  # 속력 계산

            if new_m == 0:  # 질량이 0이라면 소멸
                continue

            # 방향 설정
            all_even = all(fb[2] % 2 == 0 for fb in fireball_infos)
            all_odd = all(fb[2] % 2 == 1 for fb in fireball_infos)
            if all_even or all_odd:
                new_directions = [0, 2, 4, 6]
            else:
                new_directions = [1, 3, 5, 7]

            for d in new_directions:  # 다 처리한 파이어볼 다시 등록
                fireballs.append((r, c, new_m, new_s, d))

print(sum(fireball[2] for fireball in fireballs))