def check_around(now_pipe, next_pipe, next_dirt):
    if next_dirt == 0:
        if now_pipe == 3 or now_pipe == 5 or now_pipe == 6:
            return 0
        else:
            if next_pipe != 3 and next_pipe != 4 and next_pipe != 7:
                return 1
            else:
                return 0
    if next_dirt == 1:
        if now_pipe == 2 or now_pipe == 6 or now_pipe == 7:
            return 0
        else:
            if next_pipe != 2 and next_pipe != 4 and next_pipe != 5:
                return 1
            else:
                return 0
    if next_dirt == 2:
        if now_pipe == 3 or now_pipe == 4 or now_pipe == 7:
            return 0
        else:
            if next_pipe != 3 and next_pipe != 5 and next_pipe != 6:
                return 1
            else:
                return 0
    if next_dirt == 3:
        if now_pipe == 2 or now_pipe == 4 or now_pipe == 5:
            return 0
        else:
            if next_pipe != 2 and next_pipe != 6 and next_pipe != 7:
                return 1
            else:
                return 0