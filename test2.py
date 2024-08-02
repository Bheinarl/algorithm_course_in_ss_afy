def pipe_cut(arr):

    arr = arr.replace('()', 'i')
    arr = list(arr)

    # amount_bracket = arr.count('(')

    close_bracket = []
    open_bracket_counts = 0
    idx = 0
    result = 0
    razor_count = 0

    for txt in arr:
        if txt == '(':
            razor_count += 1
            open_bracket_counts += 1
        elif txt == 'i':
            result += open_bracket_counts

        else:
            open_bracket_counts -= 1

    result += razor_count

    return result


T = int(input())
for test_case in range(1, T+1):
    input_arr = input()
    answer = pipe_cut(input_arr)
    print(f'#{test_case} {answer}')
