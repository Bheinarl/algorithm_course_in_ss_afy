def fm(w):
    for i in range(1, len(arr)+1):
        if i//w != 0 and i % w == 0:
            if arr[i-1] == 0:
                arr[i-1] = 1
            elif arr[i-1] == 1:
                arr[i-1] = 0


def ff(w):
    k = 0
    while w-k-1 >= 0 and w+k-1 <= len(arr)-1 and arr[w-k-1] == arr[w+k-1]:
        if k == 0:
            if arr[w-1] == 0:
                arr[w-1] = 1
            elif arr[w-1] == 1:
                arr[w-1] = 0
        elif k > 0:
            if arr[w-k-1] == 0:
                arr[w-k-1] = 1
            elif arr[w-k-1] == 1:
                arr[w-k-1] = 0

            if arr[w+k-1] == 1:
                arr[w+k-1] = 0
            elif arr[w+k-1] == 0:
                arr[w+k-1] = 1

        k += 1


n = int(input())
arr = list(map(int, input().split()))
student = int(input())
for _ in range(student):
    m_f, switch_num = map(int, input().split())
    if m_f == 1:
        fm(switch_num)
    elif m_f == 2:
        ff(switch_num)

for i in range(1, n+1):
    print(arr[i-1], end=' ')
    if i%20 == 0 and i != 0:
        print()