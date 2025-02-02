N, C = map(int, input().split())
HOME = []
for _ in range(N):
    HOME.append(int(input()))

HOME.sort()

min_distance = 1
max_distance = HOME[N-1] - HOME[0]
ans = 0

while min_distance <= max_distance:

    minimum_installation_distance = (max_distance + min_distance) // 2
    router_count = 1  # 시작 점에 공유기를 설치해.

    router_house = HOME[0]

    for i in range(1, N):
        distance = HOME[i] - router_house

        if minimum_installation_distance <= distance:
            router_count += 1
            router_house = HOME[i]

    if C <= router_count:
        ans = minimum_installation_distance
        min_distance = minimum_installation_distance + 1
    else:
        max_distance = minimum_installation_distance - 1

print(ans)