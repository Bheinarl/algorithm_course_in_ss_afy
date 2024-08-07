T = int(input())
for _ in range(T):
    test_case = int(input())
    arr = list(map(int, input().split()))

    score_arr = [0] * 101

    for i in arr:
        score_arr[i] += 1

    max_counts = 0
    max_num = 0
    for ans in range(len(score_arr)):
        if max_counts <= score_arr[ans]:
            max_counts = score_arr[ans]
            max_num = ans
    print(f'#{test_case} {max_num}')