def f(arr):

    front = 0
    sub_num = 0
    while arr[front] > sub_num:

        sub_num = (sub_num) % 5 + 11  # sub_num = 1, 2, 3, 4, 5
        arr[front] -= sub_num
        front = (front+1)%8

    if arr[front] == sub_num:
        arr[front] - sub_num
    elif arr[front] <= sub_num:
        arr[front] = 0

    front = (front+1)%8

    lst = []
    for _ in range(8):
        lst += [arr[front]]
        front = (front+1)%8
    return lst


for _ in range(10):
    TEST_CASE = int(input())

    ARR = list(map(int, input().split()))

    RESULT = f(ARR)

    print(f'#{TEST_CASE}',end=' ')
    print(*RESULT)

# 왜 안될까