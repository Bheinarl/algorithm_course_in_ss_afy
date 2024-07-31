def counting_sort(lst):
    counts = [0] * (max(lst) + 1)
    Temp = [0] * len(lst)

    for num in lst:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    for j in range(len(lst) - 1, -1, -1):
        counts[lst[j]] -= 1
        Temp[counts[lst[j]]] = lst[j]

    return Temp


A = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(A))

"""
# 강사님 코드
def counting_sort(DATA, TEMP, k)
# DATA [] -- 입력 배열 (0 to k)
# TEMP [] -- 정렬된 배열
# COUNTS [] -- 카운트 배열

    COUNTS = [0] * (k-1)

    for i in range(0, len(DATA)):
        COUNTS[DATA[i]] += 1

    for j in range(1, k+1):
        COUNTS[j] += COUNTS[j-1]

    for p in range(len(TEMP)-1, -1, -1):
        COUNTS[DATA[p]] -= 1
        TEMP[COUNTS[DATA[p]]] = DATA[p]
"""

"""
DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5                    # DATA가 0~4까지의 정수

N = len(DATA)                       # DATA의 크기
TEMP = [0] * N                      # 정렬 결과 저장

# 1단계 : DATA 원소 별 개수 세기
for x in DATA:                      # DATA의 원소 x를 가져와서 COUNTS[x]에 개수 기록
    COUNTS[x] += 1

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1,5):                # COUNT[1]~COUNT[4]까지 누적개수
    COUNTS[i] += COUNTS[i-1]

# 3단계 : DATA의 맨 뒤부터 TEMP에 자리 잡기
for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1            # 누적개수 1개 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i]
"""

