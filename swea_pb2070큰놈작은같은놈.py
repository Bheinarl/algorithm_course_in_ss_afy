T = int(input())

for test_case in range(1, T+1):

    A, B = map(int, input().split())

    if A > B:
        result = '>'
    elif A < B:
        result = '<'
    else:
        result = '='

    print(f'#{test_case} {result}')
