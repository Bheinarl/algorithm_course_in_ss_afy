def f(n, m, arr):

    counts = 0
    now_carrot = 0

    for i in range(n):  # i 는 인덱스 번호임. 헷갈리면 안됨. 칸 번호 아님. 이동할 때 +1 해줘야됨. 미안 바로 까먹음 ㅋㅋ;
        counts += 1  # 앞으로 한 칸 씩
        while arr[i] >= 0:
            if now_carrot == 0:  # 남은 당근 없다
                if arr[i] > m:
                    counts += 2 * (i+1)  # 왔다 갔다
                    arr[i] -= m
                elif arr[i] == m:
                    counts += 2 * (i+1)  # 왔다 갔다
                    arr[i] = 0
                    break  # 이 칸에 당근 없으니깐 다음 칸으로 가야 해
                else:
                    now_carrot = arr[i]
                    arr[i] = 0
                    break
            else:  # 당근 남아있다
                if arr[i] > m - now_carrot:
                    counts += 2 * (i+1)  # 왔다 갔다
                    arr[i] -= m - now_carrot
                    now_carrot = 0  # 수레를 비우자
                elif arr[i] == m - now_carrot:
                    counts += 2 * (i+1)  # 왔다 갔다
                    arr[i] = 0
                    now_carrot = 0  # 수레를 비우자
                    break  # 이 칸에 당근 없으니깐 다음 칸으로 가야 해
                else:
                    now_carrot += arr[i]
                    arr[i] = 0
                    break  # 이 칸에 당근 없으니깐 다음 칸으로 가야 해
    counts += n

    return counts


T = int(input())
for TEST_CASE in range(1, T + 1):
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))

    RESULT = f(N, M, ARR)

    print(f'#{TEST_CASE} {RESULT}')