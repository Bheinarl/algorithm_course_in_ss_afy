def word_in_word(str1, str2):

    if str1 in str2:
        return 1
    else:
        return 0


T = int(input())

for test_case in range(1, T+1):

    str_1 = str(input())
    str_2 = str(input())

    result = word_in_word(str_1, str_2)

    print(f'#{test_case} {result}')
