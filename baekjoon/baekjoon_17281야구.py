from itertools import permutations

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
max_score = 0

players = [1, 2, 3, 4, 5, 6, 7, 8]

for entry in permutations(players):
    order = list(entry[:3]) + [0] + list(entry[3:])
    score = 0
    batting_player = 0

    for inning in innings:
        out_count = 0
        base1 = 0
        base2 = 0
        base3 = 0

        while out_count < 3:
            result = inning[order[batting_player]]
            batting_player = (batting_player + 1) % 9

            if result == 0:
                out_count += 1`
            elif result == 1:
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            elif result == 2:
                score += base3 + base2
                base3 = base1
                base2 = 1
                base1 = 0
            elif result == 3:
                score += base3 + base2 + base1
                base3 = 1
                base2 = 0
                base1 = 0
            elif result == 4:
                score += base3 + base2 + base1 + 1
                base1, base2, base3 = 0, 0, 0

    max_score = max(max_score, score)

print(max_score)