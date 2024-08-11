def find_team(start_idx, final_idx):
    if start_idx == final_idx:
        return start_idx
    else:
        middle_idx = (start_idx + final_idx)//2
        left_team = find_team(start_idx, middle_idx)
        right_team = find_team(middle_idx+1, final_idx)
        return find_winner(left_team, right_team)

def find_winner(left_player, right_player):  # 가위바위보
    if ARR[left_player-1] == 1:
        if ARR[right_player-1] == 2:
            return right_player
        else:
            return left_player

    elif ARR[left_player-1] == 2:
        if ARR[right_player-1] == 3:
            return right_player
        else:
            return left_player

    else:
        if ARR[left_player-1] == 3:
            if ARR[right_player-1] == 1:
                return right_player
            else:
                return left_player


T = int(input())
for TEST_CASE in range(1, T+1):
    N = int(input())
    ARR = list(map(int, input().split()))

    final_winner = find_team(1, N)

    print(f'#{TEST_CASE} {final_winner}')
