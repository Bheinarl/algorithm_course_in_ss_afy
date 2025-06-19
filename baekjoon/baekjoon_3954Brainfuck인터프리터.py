import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sm, sc, si = map(int, input().split())
    code = input().rstrip()
    input_str = input().rstrip()

    memory = [0] * sm  # 메모리 배열 (unsigned 8-bit, 초기값 0)
    pointer = 0  # 메모리 포인터 (초기 위치 0)
    code_idx = 0  # 코드 실행 위치
    input_idx = 0  # 입력 문자열 위치

    # 괄호 매칭
    bracket = {}
    stack = []
    for i in range(sc):
        if code[i] == '[':
            stack.append(i)
        elif code[i] == ']':
            j = stack.pop()
            bracket[i] = j
            bracket[j] = i

    exec_count = 0  # 총 실행된 명령어 수
    max_count = 100000000  # 최대 명령어 실행 횟수 (1억)
    loop_min_idx = sc  # 무한 루프 발생 시 가장 먼저 반복된 루프 시작점

    while code_idx < sc and exec_count < max_count:
        cmd = code[code_idx]
        exec_count += 1

        if cmd == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif cmd == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif cmd == '<':
            pointer = (pointer - 1 + sm) % sm
        elif cmd == '>':
            pointer = (pointer + 1) % sm
        elif cmd == '[':
            # 현재 값이 0이면 ]로 점프
            if memory[pointer] == 0:
                code_idx = bracket[code_idx]
        elif cmd == ']':
            # 현재 값이 0이 아니면 [로 점프 (루프 반복)
            if memory[pointer] != 0:
                code_idx = bracket[code_idx]
                # 무한 루프 추적 조건: 5천만 번 이후 점프한 루프 기록
                if exec_count >= 50000000:
                    loop_min_idx = min(loop_min_idx, code_idx)
        elif cmd == ',':
            # 입력이 남아있으면 아스키 값 저장, 아니면 255 저장
            if input_idx < len(input_str):
                memory[pointer] = ord(input_str[input_idx])
                input_idx += 1
            else:
                memory[pointer] = 255

        code_idx += 1

    if exec_count < max_count:
        print("Terminates")  # 정상 종료
    else:
        # 무한 루프일 경우, 가장 먼저 반복된 루프 구간 출력
        loop_start = loop_min_idx
        loop_end = bracket[loop_start]
        print(f"Loops {min(loop_start, loop_end)} {max(loop_start, loop_end)}")
