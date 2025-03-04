def calc(a, b, buho):
    if buho == '+':
        return a + b
    elif buho == '-':
        return a - b
    elif buho == '*':
        return a * b


def backtracking(idx, result):
    global max_result

    # 수식 끝까지 탐색한 경우, 최댓값 갱신
    if idx == n:
        max_result = max(max_result, result)
        return

    # 현재 부호와 다음 숫자
    buho = susik[idx]
    next_num = int(susik[idx + 1])

    # 1. 괄호 없이 진행
    backtracking(idx + 2, calc(result, next_num, buho))

    # 2. 괄호를 치는 경우 (괄호 안에 들어갈 다음 연산자가 존재해야 함)
    if idx + 2 < n:
        next_buho = susik[idx + 2]  # 다음 부호
        after_next_num = int(susik[idx + 3])  # 다다음 숫자
        bracket_result = calc(next_num, after_next_num, next_buho)  # 괄호 계산을 먼저 해주고
        backtracking(idx + 4, calc(result, bracket_result, buho))  # 괄호 계산 했으니 그만큼 넘겨주고 백트래킹 함수로


n = int(input().strip())
susik = input().strip()
max_result = -float('inf')

backtracking(1, int(susik[0]))
print(max_result)