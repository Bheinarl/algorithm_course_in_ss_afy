T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    d = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]  # 상하좌우 했을 때 좌표 이동 값
    ans = 0
    # 1개 있으면 더 이상 충돌 없으니깐 1개 남을때까지 계속 반속하면 되지않을까요
    for sec in range(4001):  # -1000~1000인데 (0,0), (0,1)이면 (0, 0.5)에서 만나버려서 0.5를 기준으로 해서 2배 한 값
        while len(atom) > 1:  # 1개면 어차피 만나서 부딫힐 일 없으니깐 기준은 2개 이상
            for i in range(len(atom)):
                atom[i][0] += d[atom[i][2]][0]  # 0.5초 후의 x 좌표
                atom[i][1] += d[atom[i][2]][1]  # 0.5초 후의 y 좌표

            once = set()  # 처음 나온 애들은 이리로 저장
            twice = set()  # 두 번째부터는 이리로 저장
            for j in range(len(atom)):
                (x, y) = atom[j][0], atom[j][1]
                if (x, y) in once:
                    twice.add((x, y))
                else:
                    once.add((x, y))

            for k in range(len(atom)-1, -1, -1):  # 앞에서부터 순회하면 pop 때문에 index 가 꼬여버려요.. 그래서 뒤에서부터 ㄱㄱ
                if (atom[k][0], atom[k][1]) in twice:  # 중복된 좌표라면 (처음나온 원자나 두번째 나온 원자나 좌표는 똑같아서 구분 못해요 우린 너의 에너지만 알면되잖아)
                    ans += atom[k][3]  # 에너지 저장
                    atom.pop(k)  # 너 이제 쓸모없어
                elif abs(atom[k][0]) > 1000 or abs(atom[k][1]) > 1000:  # 범위를 넘어갔네
                    atom.pop(k)  # 너도 잘가라

    print(f'#{TEST_CASE} {ans}')
