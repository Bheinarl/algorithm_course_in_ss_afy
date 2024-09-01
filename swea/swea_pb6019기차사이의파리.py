T = int(input())
for TEST_CASE in range(1, T+1):
    D, A, B, F = map(int, input().split())

    print(f'#{TEST_CASE} {D/(A+B)*F}')