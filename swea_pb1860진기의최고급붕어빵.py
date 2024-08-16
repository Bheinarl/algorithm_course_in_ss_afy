T = int(input())
for TEST_CASE in range(1, T+1):
    N, M, K = map(int, input().split())
    sonnim = list(map(int, input().split()))
    sonnim.sort()
    last_order = sonnim[-1]  # 라스트 오더까지 붕어빵을 만들꺼야

    boong_num = [0]*(last_order+1)  # 붕어빵 넣을 list

    z = 1
    while M*z < last_order+1:
        boong_num[M*z] += K  # 붕어빵을 다 넣어
        z += 1

    for a in sonnim:
        for b in range(1, a+1):  # 손님 오기 전까지 만든 붕어빵
            if boong_num[b] != 0:  # 있으면
                boong_num[b] -= 1  # 1개 손님 주고
                break
        else:  # 없으면 불가능이라고 출력
            print(f'#{TEST_CASE} Impossible')
            break
    else:  # 마지막 손님까지 붕어빵 다 줬으면 가능 이라고 출력
        print(f'#{TEST_CASE} Possible')
