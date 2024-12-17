def dust_spread():
  TEMP_ROOM = [[0] * C for _ in range(R)]
  TEMP_ROOM[purifier_location][0], TEMP_ROOM[purifier_location + 1][0] = -1, -1

  for i in range(R):
   for j in range(C):
    if ROOM[i][j] > 0:
     direction_count = 0
     for k in range(4):
      if 0 <= i + di[k] < R and 0 <= j + dj[k] < C and ROOM[i + di[k]][j + dj[k]] != -1:
       TEMP_ROOM[i + di[k]][j + dj[k]] += ROOM[i][j] // 5
       direction_count += 1
     TEMP_ROOM[i][j] += ROOM[i][j] - (ROOM[i][j] // 5) * direction_count
  return TEMP_ROOM

def upper_clean():  # 위쪽 순환
  for i in range(purifier_location - 1, 0, -1):  # 왼쪽 세로
   ROOM[i][0] = ROOM[i - 1][0]
  for j in range(C - 1):  # 아래쪽 가로
   ROOM[0][j] = ROOM[0][j + 1]
  for i in range(purifier_location):  # 오른쪽 세로
   ROOM[i][C - 1] = ROOM[i + 1][C - 1]
  for j in range(C - 1, 1, -1):  # 위쪽 가로
   ROOM[purifier_location][j] = ROOM[purifier_location][j - 1]
  ROOM[purifier_location][1] = 0  # 공기청정기 위치 -1이 순환하여 초기화


def lower_clean():  # 아래쪽 순환
  for i in range(purifier_location + 2, R - 1):  # 오른쪽 세로
   ROOM[i][0] = ROOM[i + 1][0]
  for j in range(C - 1):  # 아래쪽 가로
   ROOM[R - 1][j] = ROOM[R - 1][j + 1]
  for i in range(R - 1, purifier_location + 1, -1):  # 왼쪽 세로
   ROOM[i][C - 1] = ROOM[i - 1][C - 1]
  for j in range(C - 1, 1, -1):  # 위쪽 가로
   ROOM[purifier_location + 1][j] = ROOM[purifier_location + 1][j - 1]
  ROOM[purifier_location + 1][1] = 0  # 공기청정기 위치 -1이 순환하여 초기화

R, C, T = map(int, input().split())

ROOM = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
  if ROOM[i][0] == -1:
    purifier_location = i  # 위쪽 공기청정기 위치만 기록
    break

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

while T > 0:
  T -= 1
  ROOM = dust_spread()
  upper_clean()
  lower_clean()

ans = sum(sum(row) for row in ROOM) + 2
print(ans)

