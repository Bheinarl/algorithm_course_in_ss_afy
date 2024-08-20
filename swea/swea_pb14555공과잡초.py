def f(arr):
    n = len(arr)
    counts = 0

    for i in range(n):
        if arr[i] == ')' and arr[i-1] == '|':
            arr[i-1] = '('
        elif arr[i] == '(' and arr[i+1] == '|':
            arr[i+1] = ')'

    for j in range(n):
        if arr[j] == '(' and arr[j+1] == ')':
            counts += 1

    return counts


T = int(input())
for TEST_CASE in range(1, T+1):
    ARR = list(input())

    RESULT = f(ARR)

    print(f'#{TEST_CASE} {RESULT}')