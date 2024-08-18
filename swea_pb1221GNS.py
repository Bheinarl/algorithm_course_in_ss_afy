T = int(input())
for TEST_CASE in range(1, T+1):
    tc, N = input().split()
    ARR = list(input().split())

    num2eng = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
    eng2num = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

    for i in range(len(ARR)):
        ARR[i] = eng2num[ARR[i]]

    ARR.sort()

    for i in range(len(ARR)):
        ARR[i] = num2eng[ARR[i]]

    print(f'#{TEST_CASE}')
    print(*ARR)

"""
def sort_char_digit(n, arr):

    num_word = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    word_num = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}

    arr_1 = []

    for txt_word in arr:
        txt_word = num_word[txt_word]
        arr_1 += [txt_word]

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr_1[min_idx] > arr_1[j]:
                min_idx = j
        arr_1[i], arr_1[min_idx] = arr_1[min_idx], arr_1[i]


    arr_2 = []
    for txt_num in arr_1:
        txt_num = word_num[txt_num]
        arr_2 += [txt_num]

    return arr_2


T = int(input())

for test_case in range(1, T+1):

    tc, amount_of_words = map(str, input().split())
    arr_words = list(map(str, input().split()))

    amount_of_words = int(amount_of_words)

    result = sort_char_digit(amount_of_words, arr_words)

    print(f'#{test_case}', end=' ')
    for num in result:
        print(num, end=' ')
    print('')
"""
