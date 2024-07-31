"""
# 내가 만든 코드
T = int(input()) # 테스트 케이스 수

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = 0
    max_num = 0
    for number in arr:
        if min_num == 0 and max_num == 0:
            min_num = number
            max_num = number
        else:
            if number < min_num:
                min_num = number

            if number > max_num:
                max_num = number

    result = max_num - min_num

    print(f'#{tc} {result}')
"""

# 강사님이 만든 코드
T = int(input()) # 테스트 케이스 수

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]

        if min_v > arr[i]:
            min_v = arr[i]

    result = max_v - min_v

    print(f'#{tc} {result}')