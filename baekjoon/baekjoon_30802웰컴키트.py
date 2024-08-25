N = int(input())
size_arr = list(map(int, input().split()))
T, P = map(int, input().split())

counts = 0
for i in range(6):
    counts += size_arr[i] // T
    if size_arr[i] % T != 0:
        counts += 1

print(counts)
print(f'{N//P} {N%P}')
