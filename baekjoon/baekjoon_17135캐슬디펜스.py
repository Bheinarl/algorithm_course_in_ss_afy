import sys
from itertools import combinations

N, M, D = map(int, sys.stdin.readline().split())

enemy_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# range = abs(r1 - r2) + abs(c1 - c2)

archer_map = [n for n in range(N)]
archer_location = combinations(archer_map, 3)

for A, B, C in archer_location:
    