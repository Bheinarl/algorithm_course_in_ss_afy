from itertools import combinations
from copy import deepcopy


N, M = map(int, input().split())
LST = [list(map(int, input().split())) for _ in range(N)]

chicken_zip_list = []
house_list = []

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

for i in range(N):
    for j in range(N):
        if LST[i][j] == 1:
            house_list.append((i, j))
        elif LST[i][j] == 2:
            chicken_zip_list.append((i, j))

Mge_chicken_zip = list(combinations(chicken_zip_list, M))

min_distance_sum = N ** 2 * len(house_list)

for idx in range(len(Mge_chicken_zip)):
    temp_LST = deepcopy(LST)
    distance_sum = 0
    for chicken_zip in chicken_zip_list:
        if chicken_zip not in Mge_chicken_zip[idx]:
            (i, j) = chicken_zip
            temp_LST[i][j] = 0
    for house in house_list:
        house2chicken_zip = N ** 2
        for chicken_zip in Mge_chicken_zip[idx]:
            Hi, Hj = house
            Ci, Cj = chicken_zip
            distance = abs(Hi-Ci) + abs(Hj-Cj)
            if house2chicken_zip > distance:
                house2chicken_zip = distance
        distance_sum += house2chicken_zip

    if distance_sum < min_distance_sum:
        min_distance_sum = distance_sum

print(min_distance_sum)