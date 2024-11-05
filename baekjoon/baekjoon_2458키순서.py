import sys

N, M = map(int, sys.stdin.readline().split())

lst = [[] for _ in range(N + 1)]

check_arr = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    check_arr[a][b] = 1

for k in range(1, N + 1):  # 3중 for 문 에반데..
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if check_arr[i][k] == 1 and check_arr[k][j] == 1:
                # 하나 사이로 연결이 되어 있다면 그 둘은 중간 다리 없이도 연결되어 있음을 표시
                check_arr[i][j] = 1

ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and check_arr[i][j] == 0 and check_arr[j][i] == 0:  # 자기 자신은 연결 안했으니깐 i != j 꼭 넣어야한다.
            break
    else:  # 자기 자신을 뺀 나머지 사람이 연결?
        ans += 1

print(ans)