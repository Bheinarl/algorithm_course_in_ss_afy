def special_sort(N,arr):

    for i in range(N-1):
        min_idx = i
        max_idx = i

        if i%2 == 0: # 홀수번째 원소는 남아있는 원소들 중 최댓값으로 (선택 정렬 방식)
            for j in range(i+1,N):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[max_idx], arr[i] = arr[i], arr[max_idx]
        else: # 짝수번재 원소는 남아있는 원소들 중 최솟값으로 (선택 정렬 빙식)
            for j in range(i+1,N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]

    result = arr[0:10] # 앞에서부터 원소 10개만 출력
    return result

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    result = special_sort(N,arr)
    print(f'#{test_case}',end=' ')
    for num in result:
        print(num,end=' ')
    print('')