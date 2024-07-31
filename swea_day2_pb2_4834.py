T = int(input())

def max_card_num_amount(arr_num):

    counts = [0] * 10

    for num in arr_num: # 각 자리 숫자를 counts에 +1
        counts[num] += 1

    a = 0
    max_amount = 0
    max_num = 0

    for i in counts: # counts에서 가장 많은 숫자와 그 숫자를 찾아
        if i >= max_amount:
            max_amount = i
            max_num = a

        a += 1

    return max_amount, max_num

for test_case in range(1, T+1):
    N = int(input())
    arr_num = list(map(int, input()))
    max_amount, max_num = max_card_num_amount((arr_num))

    print(f'#{test_case} {max_num} {max_amount}')