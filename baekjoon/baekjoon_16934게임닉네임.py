import sys
input = sys.stdin.readline

N = int(input())

nicknames = set()      # 지금까지 등장한 별칭들 집합
name_count = {}        # 이름 등장 횟수

for _ in range(N):
    name = input().rstrip()

    name_count[name] = name_count.get(name, 0) + 1 # 마지막에 숫자 붙이려고

    nickname = ""      # 이번 유저에게 부여될 별칭

    # 1글자 ~ 전체까지 별칭(접두사) 확인
    for i in range(1, len(name) + 1):
        prefix = name[:i]

        # 처음 나온 별칭이라면 이번 유저의 별칭
        if nickname == "" and prefix not in nicknames:
            nickname = prefix

        # 지금까지의 별칭 목록에 추가
        nicknames.add(prefix)

    # 자신만의 별칭을 찾지 못한 경우 동일 닉네임에 숫자를 붙여서 사용
    if nickname == "":
        count = name_count[name]
        if count == 1:
            nickname = name
        else:
            nickname = name + str(count)

    print(nickname)