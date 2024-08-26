N, K = map(int, input().split())
ARR = list(map(int, input().split()))

sum_list = [sum(ARR[:K])]
for i in range(1, N-K+1):
    sum_list += [sum_list[-1] + ARR[i+K-1] - ARR[i-1]]

print(max(sum_list))
