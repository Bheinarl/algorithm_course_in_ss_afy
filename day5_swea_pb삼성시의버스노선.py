def how_many_bus_in_bus_stop(buses, bus_stops):

    bus_counts = []
    for bus_stop in bus_stops:  # 버스 정류장 번호를 순회하면서
        counts = 0
        for bus in buses:  # 버스의 노선 안에 정류장 번호가 있으면 count+1
            if bus_stop in list(range(bus[0], bus[1]+1)):
                counts += 1
        bus_counts += [counts]  # 한 버스 정류장 번호 스캔 완료하면 리스트에 추가

    return bus_counts


T = int(input())
for test_case in range(1, T+1):

    N = int(input())

    BUSES = []
    for _ in range(N):
        BUSES += [list(map(int, input().split()))]

    P = int(input())

    BUS_STOPS = []
    for _ in range(P):
        BUS_STOPS += [int(input())]

    result = how_many_bus_in_bus_stop(BUSES, BUS_STOPS)

    print(f'#{test_case}', end=' ')
    print(*result, end=' ')
    print('')
