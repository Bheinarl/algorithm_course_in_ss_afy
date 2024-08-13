def f(blue, orange, bo_order):

    min_sec = 0

    b_location = 1
    o_location = 1

    b_len = len(blue)
    o_len = len(orange)

    blue_idx = 0
    orange_idx = 0

    for j in range(len(bo_order)):
        if bo_order[j] == 'B':  # 블루 차례
            if blue_idx < b_len and orange_idx < o_len:  # 둘 다 이동해야 할 때
                if abs(b_location - blue[blue_idx]) >= abs(o_location - orange[orange_idx]):  # 블루가 가야할 곳이 더 멀다면
                    o_location = orange[orange_idx]  # 오렌지는 목적지까지 이동

                elif abs(b_location - blue[blue_idx]) < abs(o_location - orange[orange_idx]):  # 오렌지가 가야할 곳이 더 멀다면
                    if o_location < orange[orange_idx]:  # 오렌지는 이동시간만큼 이동해
                        o_location += abs(b_location - blue[blue_idx]) + 1
                    else:
                        o_location -= abs(b_location - blue[blue_idx]) + 1

                min_sec += abs(b_location - blue[blue_idx]) + 1  # 블루는 목적지까지 가서 종을 눌러
                b_location = blue[blue_idx]  # 블루 목적지까지 이동하고
                blue_idx += 1  # 블루 다음 목적지 설정

            elif blue_idx < b_len:  # 블루만 이동해야한다면
                min_sec += abs(blue[blue_idx] - b_location) + 1  # 블루 목적지까지 가서 이동하고 종 눌러
                b_location = blue[blue_idx]  # 블루 목적지까지 이동하고
                blue_idx += 1  # 블루 다음 목적지 설정

            elif orange_idx < o_len:  # 오렌지만 이동해야한다면
                min_sec += abs(orange[orange_idx] - o_location) + 1  # 오렌지 목적지까지 가서 이동하고 종 눌러
                o_location = orange[orange_idx]  # 오렌지 목적지까지 이동하고
                orange_idx += 1  # 오렌지 다음 목적지 설정

        else:  # 오렌지 차례
            if blue_idx < b_len and orange_idx < o_len:  # 둘 다 이동해야 할 때
                if abs(o_location - orange[orange_idx]) >= abs(b_location - blue[blue_idx]):  # 오렌지가 가야할 곳이 더 멀다면
                    b_location = blue[blue_idx]  # 블루는 목적지까지 이동

                elif abs(o_location - orange[orange_idx]) < abs(b_location - blue[blue_idx]):  # 블루가 가야할 곳이 더 멀다면
                    if b_location < blue[blue_idx]:  # 블루는 이동 시간만큼 이동해
                        b_location += abs(o_location - orange[orange_idx]) + 1
                    else:
                        b_location -= abs(o_location - orange[orange_idx]) + 1

                min_sec += abs(o_location - orange[orange_idx]) + 1  # 오렌지는 가서 종을 눌러
                o_location = orange[orange_idx]  # 오렌지는 목적지까지 이동
                orange_idx += 1  # 오렌지는 다음 목적지 설정

            elif blue_idx < b_len:  # 블루만 이동해야한다면
                min_sec += abs(blue[blue_idx] - b_location) + 1  # 블루 목적지까지 가서 이동하고 종 눌러
                b_location = blue[blue_idx]  # 블루 목적지까지 이동하고
                blue_idx += 1  # 블루 다음 목적지 설정

            elif orange_idx < o_len:  # 오렌지만 이동해야한다면
                min_sec += abs(orange[orange_idx] - o_location) + 1  # 오렌지 목적지까지 가서 이동하고 종 눌러
                o_location = orange[orange_idx]  # 오렌지 목적지까지 이동하고
                orange_idx += 1  # 오렌지 다음 목적지 설정

    return min_sec


T = int(input())
for TEST_CASE in range(1, T+1):
    ARR = list(input().split())

    Blue = []
    Orange = []
    BO_order = []

    N = ARR[0]

    for i in range(1, len(ARR)):
        if i % 2 == 1:
            BO_order += ARR[i]  # 블루 오렌지 순서대로 누가 눌러야하는지 저장
            if ARR[i] == 'B':
                Blue += [int(ARR[i+1])]  # 블루 목적지
            elif ARR[i] == 'O':
                Orange += [int(ARR[i+1])]  # 오렌지 목적지

    RESULT = f(Blue, Orange, BO_order)

    print(f'#{TEST_CASE} {RESULT}')
