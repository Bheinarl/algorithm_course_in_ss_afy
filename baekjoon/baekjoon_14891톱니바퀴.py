def f(mag, dirt):

    m0_1 = mag
    m0_2 = mag
    m1 = mag + 1
    m2 = mag - 1
    lst = []

    while m1 < 4 and ARR[m0_1][right[m0_1]] != ARR[m1][left[m1]]:  # 해당 자석의 오른쪽에 있는거
        lst.append(m1)  # 둘이 극이 다르면 저장
        m0_1 += 1
        m1 += 1

    while m2 >= 0 and ARR[m0_2][left[m0_2]] != ARR[m2][right[m2]]:  # 해당 자석의 왼쪽에 있는거
        lst.append(m2)  # 둘이 극이 다르면 저장
        m0_2 -= 1
        m2 -= 1

    for i in range(len(lst)):
        magnetic = lst[i]
        if magnetic % 2 == mag % 2:  # 실제로 돌리는 자석과 퐁당 건넌 자석이라면
            if dirt == 1:  # 방향이 시계 방향일 때
                left[magnetic] = (left[magnetic] - 1) % 8
                right[magnetic] = (right[magnetic] - 1) % 8
                red[magnetic] = (red[magnetic] - 1) % 8
            else:  # 방향이 반시계 방향일 때
                left[magnetic] = (left[magnetic] + 1) % 8
                right[magnetic] = (right[magnetic] + 1) % 8
                red[magnetic] = (red[magnetic] + 1) % 8
        else:  # 실제로 돌리는 자석 옆의 자석이라면
            if dirt == 1:  # 방향이 시계 방향일 때
                left[magnetic] = (left[magnetic] + 1) % 8
                right[magnetic] = (right[magnetic] + 1) % 8
                red[magnetic] = (red[magnetic] + 1) % 8
            else:  # 방향이 반시계 방향일 때
                left[magnetic] = (left[magnetic] - 1) % 8
                right[magnetic] = (right[magnetic] - 1) % 8
                red[magnetic] = (red[magnetic] - 1) % 8

    if dirt == 1:  # 방향이 시계 방향일 때
        left[mag] = (left[mag] - 1) % 8
        right[mag] = (right[mag] - 1) % 8
        red[mag] = (red[mag] - 1) % 8
    else:  # 방향이 반시계 방향일 때
        left[mag] = (left[mag] + 1) % 8
        right[mag] = (right[mag] + 1) % 8
        red[mag] = (red[mag] + 1) % 8


ARR = []
temp = []
for pp in range(4):
    temp = list(input())
    for pp in range(8):
        temp[pp] = int(temp[pp])
    ARR += [temp]

red = [0, 0, 0, 0]
left = [6, 6, 6, 6]
right = [2, 2, 2, 2]

K = int(input())
for _ in range(K):
    MAG, DIRT = map(int, input().split())
    f(MAG-1, DIRT)

score = 0
if ARR[0][red[0]] == 1:
    score += 1

if ARR[1][red[1]] == 1:
    score += 2

if ARR[2][red[2]] == 1:
    score += 4

if ARR[3][red[3]] == 1:
    score += 8

print(score)
