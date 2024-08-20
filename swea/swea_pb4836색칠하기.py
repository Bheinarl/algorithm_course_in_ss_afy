T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = []
    ans = [[0]*11 for _ in range(11)]
    for _ in range(N):
        ARR += [list(map(int, input().split()))]

    for i in range(N):
        for a in range(ARR[i][0], ARR[i][2]+1):
            for b in range(ARR[i][1], ARR[i][3]+1):
                ans[a][b] += ARR[i][4]

    counts = 0
    for x in range(11):
        for y in range(11):
            if ans[x][y] == 3:
                counts += 1

    print(f'#{TEST_CASE} {counts}')

"""
T = int(input())

def mixed_color_area(arr):

    whole_arr = [ [0] * 10 for _ in range(10) ] # 그림그릴 10x10 행렬 생성
    counts = 0

    for coloring in arr: # 한 행씩 구분하여 색칠

        fi = coloring[0]
        fj = coloring[1]
        ti = coloring[2]
        tj = coloring[3]
        color = coloring[4]

        for i in range(fi,ti+1): # 해당 범위를 스캔하여 색 숫자만큼 +
            for j in range(fj,tj+1):
                whole_arr[i][j] += color

    for i in range(10): # 다 그림그린 10x10 행렬을 다 스캔하여 color들의 합 3인 칸의 갯수를 count
        for j in range(10):
            if whole_arr[i][j] == 3:
                counts += 1

    result = counts

    return result

for test_case in range(1, T+1):
    N = int(input())
    arr = []

    for _ in range(N):
        arr += [list(map(int,input().split()))] #데이터를 Nx5 행렬로 생성

    result = mixed_color_area(arr)

    print(f'#{test_case} {result}')
"""