from itertools import permutations
import sys

# 회전 함수
def rotate(temp_LST, r, c, s):
    for level in range(1, s + 1):
        # 가장 왼쪽 위 값을 임시 저장
        temp = temp_LST[r - level][c - level]
        # 왼쪽 이동
        for i in range(r - level, r + level):
            temp_LST[i][c - level] = temp_LST[i + 1][c - level]
        # 아래쪽 이동
        for i in range(c - level, c + level):
            temp_LST[r + level][i] = temp_LST[r + level][i + 1]
        # 오른쪽 이동
        for i in range(r + level, r - level, -1):
            temp_LST[i][c + level] = temp_LST[i - 1][c + level]
        # 위쪽 이동
        for i in range(c + level, c - level, -1):
            temp_LST[r - level][i] = temp_LST[r - level][i - 1]
        # 저장한 값 복원
        temp_LST[r - level][c - level + 1] = temp

# 최소 행 합 계산
def min_row_sum(array):
    return min(sum(row) for row in array)

# 입력 처리
N, M, K = map(int, sys.stdin.readline().split())
LST = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]

# 순열 생성
min_value = float('inf')
for perm in permutations(rotations):
    temp_LST = [row[:] for row in LST]  # 얕은 복사
    for r, c, s in perm:
        rotate(temp_LST, r - 1, c - 1, s)
    min_value = min(min_value, min_row_sum(temp_LST))

# 결과 출력
print(min_value)