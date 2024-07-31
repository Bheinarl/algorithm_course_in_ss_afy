T = int(input())

def charge_num(K, N, M, charge_bus_stop):
    bus_idx = 0
    result = 0
    result_False = 0
    count_bf = 0
    count_af = 0

    while bus_idx < N - K: # 버스가 마지막 운행 가능한 시점에 도달하면 반복문 종료
        bus_idx_able = list(range(bus_idx+1, (bus_idx + K + 1)))[::-1] # 버스가 갈 수 있는 인덱스 list
        for bus_charge_able in bus_idx_able:
            if bus_charge_able in charge_bus_stop: # 버스가 갈 수 있는 곳안에 충전할 곳이 있다면
                count_af += 1 # 횟수 1번 추가
                break # 반복문 다시 시작

        if count_bf == count_af: # 횟수가 이전 횟수랑 같다면 (버스가 충전을 하지 못하였다면)
            return result_False # 0 반환
        else:
            count_bf = count_af # 횟수가 이전 횟수랑 다르다면 (버스가 충전을 했다면) 반복문 진행

        bus_idx = bus_charge_able #버스가 충전하러 간 곳으로 이동
        result = count_af


    return result

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_bus_stop = list(map(int, input().split()))

    result = charge_num(K, N, M, charge_bus_stop)

    print(f'#{test_case} {result}')