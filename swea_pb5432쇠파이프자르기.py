def f():

    cutting_pipe = 0
    open_pipe = 0

    for i in range(len(ARR)):
        if ARR[i] == '(' and ARR[i+1] != ')':
            open_pipe += 1
            cutting_pipe += 1
        elif ARR[i] == ')' and ARR[i-1] != '(':
            open_pipe -= 1
        elif ARR[i] == '(' and ARR[i+1] == ')':
            cutting_pipe += open_pipe

    return cutting_pipe


T = int(input())
for TEST_CASE in range(1, T+1):
    ARR = list(input())

    RESULT = f()

    print(f'#{TEST_CASE} {RESULT}')

"""
def pipe_cut(arr):
    arr = arr.replace('()', 'i')  # 레이저를 () 대신 i로 변경
    arr = list(arr)
    open_bracket_counts = 0
    result = 0
    razor_count = 0

    # 어느 파이프에 레이저가 맞던간에 파이프에 레이저가 맞으면 파이프 갯수대로 일단 한조각이 튀어 나온다.
    for txt in arr:
        if txt == '(':  # 파이프가 시작되면
            razor_count += 1  # 총 파이프의 갯수
            open_bracket_counts += 1  # 레이저에 맞을 현재 파이프 갯수
        elif txt == 'i':
            result += open_bracket_counts  # 레이저가 맞은 파이프 수만큼 결과값에 +
        else:  # txt == ')'
            open_bracket_counts -= 1  # 파이프가 끝났으니 현재 파이프 갯수 -1

    result += razor_count  # 레이저에 한 번 맞으면 일단 두 조각이 되므로 총 파이프 갯수만큼 +

    return result


T = int(input())
for test_case in range(1, T + 1):
    input_arr = input()
    answer = pipe_cut(input_arr)
    print(f'#{test_case} {answer}')
"""