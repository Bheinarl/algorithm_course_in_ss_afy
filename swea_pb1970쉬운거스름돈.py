T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ANS = [0]*8

    while N >= 50000:
        ANS[0] += 1
        N -= 50000

    while N >= 10000:
        ANS[1] += 1
        N -= 10000

    while N >= 5000:
        ANS[2] += 1
        N -= 5000

    while N >= 1000:
        ANS[3] += 1
        N -= 1000

    while N >= 500:
        ANS[4] += 1
        N -= 500

    while N >= 100:
        ANS[5] += 1
        N -= 100

    while N >= 50:
        ANS[6] += 1
        N -= 50

    while N >= 10:
        ANS[7] += 1
        N -= 10

    print(f'#{TEST_CASE}')
    print(*ANS)