# 백준에서는 틀려서 다시 정리
def f():

    # 범위 밖을 벗어나는 것은 다 안겹친다.
    if rec1_x2 < rec2_x1 or rec1_x1 > rec2_x2 or rec1_y2 < rec2_y1 or rec1_y1 > rec2_y2:
        return 4

    # 만날 수 있는 점을 모두 걸러내
    elif rec1_x2 == rec2_x1 and rec1_y1 == rec2_y2:
        return 3
    elif rec1_x2 == rec2_x1 and rec1_y2 == rec2_y1:
        return 3
    elif rec1_x1 == rec2_x2 and rec1_y2 == rec2_y1:
        return 3
    elif rec1_x1 == rec2_x2 and rec1_y1 == rec2_y2:
        return 3

    # 점을 걸러내고도 같은거는 선으로 겹치는 것
    # rec1_x1 == rec2_x1은 둘이 면이 겹치게 되므로 제외. y도 마찬가지
    elif rec1_x2 == rec2_x1 or rec1_x1 == rec2_x2 or rec1_y1 == rec2_y2 or rec1_y2 == rec2_y1:
        return 2

    # 나머지는 면으로 겹치겠지
    else:
        return 1


T = int(input())
for TEST_CASE in range(1, T+1):

    rec1_x1, rec1_y1, rec1_x2, rec1_y2 = map(int, input().split())
    rec2_x1, rec2_y1, rec2_x2, rec2_y2 = map(int, input().split())

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')
