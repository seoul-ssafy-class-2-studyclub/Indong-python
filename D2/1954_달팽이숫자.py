def snail(n, n_list, board):
    def snail_second(m, m_list, BS):
        RS_index = int((len(BS) - m) / 2) + m
        CS_index = int((len(BS) - m) / 2)
        if m == 1:
            BS[RS_index].insert(CS_index, m_list.pop(0))
            return BS
        else:
            for RS in range(m):
                BS[RS_index].insert(CS_index, m_list.pop(0))
            for CS in range(1, m):  
                BS[RS_index - CS].insert(CS_index, m_list.pop(0))  # ㄱ자 모양을 만들 때와는 반대로 위로 올라감.

            return snail(m - 1, m_list, BS)

    row_index = int((len(board) - n) / 2)  # 몇 번째 행에서 시작할 것인가?
    column_index = int((len(board) - n) / 2)  # 몇 번째 열에 집어넣을 것인가?
    if n == 1:
        board[row_index].insert(column_index, n_list.pop(0))
        return board
    else:
        for row in range(n):
            board[row_index].insert(column_index + row, n_list.pop(0))  # 행 번호는 고정되어 있고 열 번호가 이동함으로써 숫자를 집어넣음.

        for column in range(1, n):  # ㄱ 모양으로 만드는 작업. 반대로 열번호는 고정되어 있고 행 번호가 이동함.
            board[row_index + column].insert(column_index, n_list.pop(0))

        return snail_second(n - 1, n_list, board)

case_size = int(input())
for case in range(case_size):
    length = int(input())
    number_list = list(range(1, length ** 2 + 1))
    snail_board = [[] for i in range(length)]
    result_matrix = snail(length, number_list, snail_board)
    print(f'#{case + 1}')
    for row in result_matrix:
        print(' '.join(map(str, row)))          
