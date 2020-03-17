for case in range(1, int(input()) + 1):
    board = []
    max_len = 0
    for i in range(5):
        word_list = [i for i in input()]
        if len(word_list) > max_len:
            max_len = len(word_list)
        board.append(word_list)
    for i in range(5):
        board[i] += ['#'] * (max_len - len(board[i]))
    result = ''
    for i in range(max_len):
        for j in range(5):
            if board[j][i] == '#':
                continue
            result += board[j][i]
    print(f'#{case} {result}')
    