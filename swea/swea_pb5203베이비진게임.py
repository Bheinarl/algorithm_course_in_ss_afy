def f():
    for a in range(10):
        if A[a] >= 3:  # A 먼저 triplet
            return 1
        elif a <= 7 and A[a] >= 1 and A[a+1] >= 1 and A[a+2] >= 1:  # A 먼저 run
            return 1

        elif B[a] >= 3:  # B triplet
            return 2
        elif a <= 7 and B[a] >= 1 and B[a+1] >= 1 and B[a+2] >= 1:  # B run
            return 2


T = int(input())
for TEST_CASE in range(1, T+1):
    ARR = list(map(int, input().split()))

    A = [0] * 10
    B = [0] * 10
    RESULT = 0
    for i in range(len(ARR)):
        if i % 2 == 0:
            A[ARR[i]] += 1
        else:
            B[ARR[i]] += 1

        if f() == 1 or f() == 2:
            RESULT = f()  # RESULT 값이 나오면 승자 출력
            print(f'#{TEST_CASE} {RESULT}')
            break
    else:
        if RESULT == 0:  # 다 순회했는데도 승자가 안정해지면 무승부 0 출력
            print(f'#{TEST_CASE} 0')
