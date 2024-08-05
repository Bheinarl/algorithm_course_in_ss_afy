def f(t, p):  # 패턴 p와 일치하는 구간의 시작인덱스 리턴, 일치하는 경우가 없으면 -1 리턴
    n = len(t)
    m = len(p)

    for i in range(n-m+1):
        for j in ragne(m):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return -1
