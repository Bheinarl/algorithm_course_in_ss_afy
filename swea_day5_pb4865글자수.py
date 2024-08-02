def amount_of_str(str1, str2):

    max_count = 0

    for text_1 in str1:
        counts = 0
        for text_2 in str2:
            if text_1 == text_2:
                counts += 1
        if counts > max_count:
            max_count = counts

    return max_count


T = int(input())

for test_case in range(1, T+1):

    str_1 = list(input())
    str_2 = list(input())

    result = amount_of_str(str_1, str_2)

    print(f'#{test_case} {result}')
