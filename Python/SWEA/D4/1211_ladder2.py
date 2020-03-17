for case in range(1, 11):
    board = []
    N = int(input())
    for row in range(100):
        board.append(list(map(int, input().split())))

    min_cnt = 0
    min_idx = 0
    for i in range(100):
        if board[0][i] != 1:
            continue
        start = i
        idx = i
        cnt = 0
        for j in range(1, 100):
            cnt += 1
            if idx != 0 and board[j][idx-1]:
                while idx > 0 and board[j][idx-1]:
                    idx -= 1
                    cnt += 1
            elif idx != 99 and board[j][idx+1]:
                while idx < 99 and board[j][idx+1]:
                    idx += 1
                    cnt += 1

        if not min_cnt:
            min_cnt = cnt
            min_idx = start

        if cnt <= min_cnt:
            min_cnt = cnt
            min_idx = start
            
    print(f'#{case} {min_idx}')
        