N, K = map(int, input().split())
belt = list(map(int, input().split()))  # 벨트 길이는 2 * N
robot_location = [0] * N   # 로봇은 벨트 위에만 있으면 되므로 길이는 N

zero_count = 0  # 내구도 0 개수
ans = 0  # 단계 횟수

while zero_count < K:  # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    ans += 1  # 단계 추가

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt = [belt[-1]] + belt[:-1]  # 벨트 회전
    robot_location = [robot_location[-1]] + robot_location[:-1]  # 벨트 회전으로 인한 로봇 위치 변경
    robot_location[-1] = 0  # 벨트 끝에는 로봇 내림

    for i in range(N-2, -1, -1):  # 먼저 벨트에 올라간 로봇부터 이동시켜야하므로 역순으로 순회
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
        if robot_location[i] and not robot_location[i+1] and belt[i+1] > 0:  # 로봇이 있고, 다음 칸에 로봇이 없고, 내구도 존재
            robot_location[i] = 0  # 로봇 이동
            robot_location[i+1] = 1
            belt[i+1] -= 1  # 내구도 감소
            if not belt[i+1]:  # 내구도 확인
                zero_count += 1

    robot_location[-1] = 0  # 로봇이 벨트 끝으로 이동하였다면 로봇을 내려.

    if belt[0] > 0:  # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        robot_location[0] = 1
        belt[0] -= 1
        if not belt[0]:
            zero_count += 1

print(ans)