def func(n, arr):

    txt_idx = 0
    max_counts = 0

    for txt in arr:  # 글자 하나씩 순회하여
        if txt == '1':  # 1이면
            counts = 0
            i = txt_idx
            while i <= n-1 and arr[i] == '1':  # i가 마지막 인덱스 넘어가지 않고 1이 아닐때까지 반복하여 count
                                               # 순서 바뀌면 Error
                i += 1
                counts += 1
            if counts > max_counts:
                max_counts = counts
        txt_idx += 1

    return max_counts


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ARR = str(input())

    result = func(N, ARR)

    print(f'#{test_case} {result}')
