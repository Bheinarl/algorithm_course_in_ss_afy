T = int(input())

for t in range(1, T+1):
    m, n = map(int, input().split())

    ans_1 = m // n
    ans_2 = m % n

    print(f'#{t} {ans_1} {ans_2}')