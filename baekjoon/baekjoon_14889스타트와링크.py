def check_status(lst):  # 늘 했던 계산, i=j일 경우에는 계산에서 빼주는 것이 좋지만 어차피 값이 0이므로 그냥 계산
    status = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            status += ARR[lst[i]][lst[j]]

    return status


def f(idx, lst_A, lst_B):  # 반반 나눠서 확인해보는 시스템

    global min_diff

    if min_diff == 0:  # 이미 차이가 0이라는 것은 황밸이니까 다음 팀을 안짜도 된다. 빠른 가지치기
        return

    if idx == N and len(lst_A) > N//2:  # 다 팀을 나눴는데 A팀이 너무 많아
        return
    elif idx == N and len(lst_B) > N//2:  # 다 팀을 나눴는데 B팀이 너무 많아
        return
    elif idx == N and len(lst_A)==N//2 and len(lst_B)==N//2:  # 다 팀 나눴는데 A, B팀 인원 반반으로 나뉘었으면 계산 시작
        sum_A = check_status(lst_A)
        sum_B = check_status(lst_B)
        diff = abs(sum_B - sum_A)

        min_diff = min(min_diff, diff)

    else:
        # 무조건 팀은 정해야하므로 A팀에 안들어가면 B팀에 들어가야 함
        f(idx + 1, lst_A+[idx], lst_B)
        f(idx + 1, lst_A, lst_B+[idx])


N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]
min_diff = 100 * N**2 # 최대가 1 ~ 100이니깐 두 명의 차이가 최대 100이라고 생각하면 최대차이가 100*N^2면 충분히 큰 수
f(0, [], [])

print(min_diff)