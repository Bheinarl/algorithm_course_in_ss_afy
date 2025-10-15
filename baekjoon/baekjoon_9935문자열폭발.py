import sys

input = sys.stdin.readline
code = input().rstrip("\n")
bomb = input().rstrip("\n")

# bomb를 모두 제거할 때까지 반복해서 replace
while True:
    new_code = code.replace(bomb, "")
    if new_code == code:
        break
    code = new_code

print(code if code != "" else "FRULA")

"""
import sys
input = sys.stdin.readline

code = input().rstrip('\n')
bomb = input().rstrip('\n')

stack = []
last_char = bomb[-1]
bomb_list = list(bomb)

for ch in code:
    stack.append(ch)
    if ch == last_char and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb_list:
            del stack[-len(bomb):]

print(''.join(stack) if stack else 'FRULA')


"""