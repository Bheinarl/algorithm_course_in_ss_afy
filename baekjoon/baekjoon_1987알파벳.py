from collections import deque

def change2bit(alphabet):
    return 1 << (ord(alphabet) - ord('A'))

R, C = map(int, input().split())
LST = [list(input()) for _ in range(R)]

Q = deque()
visited = [[set() for _ in range(C)] for _ in range(R)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

start_bit_mask = change2bit(LST[0][0])  # 처음 알파벳 비트마스크
Q.append((0, 0, start_bit_mask, 1))
visited[0][0].add(start_bit_mask)
max_length = 1  # 처음 시작할 때는 길이 1

while Q:
    i, j, bit_mask, length = Q.popleft()

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        max_length = max(max_length, length)
        if 0 <= ni < R and 0 <= nj < C:
            next_alphabet = LST[ni][nj]
            next_bit_mask = change2bit(next_alphabet)

            if not (bit_mask & next_bit_mask):  # 만약 이미 있는 알파벳이라면 & 값이 자연수, 없는 알파벳이라면 0으로 나온다.
                # 없는 알파벳이라면
                new_bit_mask = bit_mask | next_bit_mask  # 이러면 비트끼리 합쳐져서 나온다.
                if new_bit_mask not in visited[ni][nj]:
                    visited[ni][nj].add(new_bit_mask)
                    Q.append((ni, nj, new_bit_mask, length + 1))  # 길이 추가

print(max_length)