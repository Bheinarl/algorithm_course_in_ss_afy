def find_book_page_binary_search(whole_page, start_page, answer_page):
    global counts
    counts += 1
    end_page = whole_page
    center_page = (start_page + end_page) // 2
    if center_page == answer_page:  # 찾고자하는 페이지를 찾으면
        result = counts  # 횟수를 반환
        counts = 0  # 'counts' 는 다시 써야되므로 초기화
        return result
    elif center_page < answer_page:  # 중앙 페이지보다 찾고자 하는 페이지가 크면
        return find_book_page_binary_search(whole_page, center_page, answer_page)  # 중앙 페이지+1 ~ 끝 페이지 다시 검색
    elif center_page > answer_page:  # 중앙 페이지보다 찾고자 하는 페이지가 작으면
        return find_book_page_binary_search(center_page, start_page, answer_page)  # 처음 페이지 ~ 중앙 페이지-1 다시 검색


T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    counts = 0
    count_A = find_book_page_binary_search(P, 1, Pa)  # A의 횟수
    count_B = find_book_page_binary_search(P, 1, Pb)  # B의 횟수

    if count_A > count_B:  # 승자 찾기
        winner = 'B'
    elif count_A < count_B:
        winner = 'A'
    else:
        winner = 0

    print(f'#{test_case} {winner}')
