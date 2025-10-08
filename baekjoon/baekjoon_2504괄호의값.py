import sys
char = input().strip()

if len(char) % 2 == 1:
    print(0)
    sys.exit(0)

stack = []
ans = 0
temp = 1  #  가중치 - ()는 2, []는 3

for i, bracket in enumerate(char):
    if bracket == '(':
        stack.append('(')
        temp *= 2
    elif bracket == '[':
        stack.append('[')
        temp *= 3
    elif bracket == ')':
        # 열린 소괄호 없음
        if not stack or stack[-1] != '(':
            print(0)
            sys.exit(0)
        # 바로 닫음 ()
        if i > 0 and char[i-1] == '(':
            ans += temp
        stack.pop()
        temp //= 2
    elif bracket == ']':
        # 열린 대괄호 없음
        if not stack or stack[-1] != '[':
            print(0)
            sys.exit(0)
        # 바로 닫음 []
        if i > 0 and char[i-1] == '[':
            ans += temp
        stack.pop()
        temp //= 3
    else:
        print(0)
        sys.exit(0)

# 다 계산 후 스택에 남아 있으면 잘못된 괄호열
print(0 if stack else ans)