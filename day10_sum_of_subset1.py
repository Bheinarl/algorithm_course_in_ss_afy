def f(i, k):    # bit[i]를 결정하는 함수
    if i == k:  # 모든 원소에 대해 결정하면
        s = 0  # 부분집합의 합 저장
        for j in range(k):
            if bit[j]:  # bit[j]가 0이 아니면
                print(a[j], end=' ')  # 부분집합을 한 행에 표시
                s += a[j]
        print(' : ', s)
    else:
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)
        for j in [1, 0]:
            bit[i] = j
            f(i+1, k)


N = 3
a = [1, 2, 3]  # 주어진 원소의 집합
bit = [0] * N  # 원소의 포함 여부를 표시하는 배열
f(0, N)        # N개의 원소에 대해 부분집합을 만드는 함수
