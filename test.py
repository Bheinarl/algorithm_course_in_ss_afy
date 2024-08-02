def pipe_cut(arr):

    arr = arr.replace('()', 'i')
    arr = list(arr)

    # amount_bracket = 0
    # for txt in arr:
    #     if txt == '(':
    #         amount_bracket += 1

    close_bracket = []
    open_bracket_counts = 0
    idx = 0

    for txt in arr:
        if txt == '(':
            # open_bracket_counts = str(open_bracket_counts)
            arr[idx] = open_bracket_counts
            # open_bracket_counts = int(open_bracket_counts)
            close_bracket += [open_bracket_counts]
            open_bracket_counts += 1
            idx += 1
        elif txt == ')':
            close_num = close_bracket[-1]
            close_bracket.remove(close_num)
            if close_bracket is None:
                close_bracket = []
            # close_num = str(close_num)
            arr[idx] = close_num
            idx += 1
        else:
            idx += 1




    result = 0
    for num in range(open_bracket_counts):
        idx_list = []
        # num = str(num)
        for idx_arr in range(len(arr)):
            if arr[idx_arr] == num:

                idx_list += [idx_arr]

        between_array = arr[idx_list[0]+1:idx_list[1]]
        counting_i = 0
        for elements in between_array:
            if elements == 'i':
                counting_i += 1
        result += counting_i + 1

    return result


T = int(input())
for test_case in range(1, T+1):
    input_arr = input()
    answer = pipe_cut(input_arr)
    print(f'#{test_case} {answer}')
