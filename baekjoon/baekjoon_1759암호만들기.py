import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
chars = sorted(input().split())

is_moum = [False] * 26
for char in ['a', 'e', 'i', 'o', 'u']:
    is_moum[ord(char) - 97] = True

for combi in combinations(chars, L):
    moum_count = sum(is_moum[ord(char) - 97] for char in combi)
    jaum_count = L - moum_count
    if moum_count >= 1 and jaum_count >= 2:
        print(''.join(combi))