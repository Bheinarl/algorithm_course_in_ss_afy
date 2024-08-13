def f(arr):

    front = 0
    sub_num = 0
    while arr[front] > sub_num % 5 + 1:  # 빼면 원소가 0이 될 때 (암호가 될 때)

        sub_num = sub_num % 5 + 1  # sub_num = 1, 2, 3, 4, 5
        arr[front] -= sub_num
        front = (front+1) % 8  # front = 0, 1, 2, 3, 4, 5, 6, 7

    arr[front] = 0  # while 문 빠져 나온건 빼면 0이 될 때이다.

    front = (front+1) % 8  # 0인 원소를 맨 뒤로 이동

    lst = []
    for _ in range(8):
        lst += [arr[front]]
        front = (front+1) % 8
    return lst


for _ in range(10):
    TEST_CASE = int(input())

    ARR = list(map(int, input().split()))

    RESULT = f(ARR)

    print(f'#{TEST_CASE}', end=' ')
    print(*RESULT)
