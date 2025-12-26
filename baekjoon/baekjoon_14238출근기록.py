import sys

S = input().strip()

A = S.count('A')
B = S.count('B')
C = S.count('C')

N = len(S)
answer = None
visited = set()

def dfs(a, b, c, yesterday, yesterday_yesterday, path):
    global answer

    if answer is not None:
        return

    state = (a, b, c, yesterday, yesterday_yesterday)
    if state in visited:
        return
    visited.add(state)

    if len(path) == N:
        answer = path
        return

    # A
    if a > 0:
        dfs(a-1, b, c, 'A', yesterday, path + 'A')

    # B
    if b > 0 and yesterday != 'B':
        dfs(a, b-1, c, 'B', yesterday, path + 'B')

    # C
    if c > 0 and yesterday != 'C' and yesterday_yesterday != 'C':
        dfs(a, b, c-1, 'C', yesterday, path + 'C')

dfs(A, B, C, '', '', '')

print(answer if answer else -1)