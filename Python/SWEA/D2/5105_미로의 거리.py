def maze(board, N):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = []
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                queue.append((i, j))

    result = 0
    cnt = 0
    is_fin = False
    while queue and not is_fin:
        cnt += 1
        for _ in range(len(queue)):
            y, x = queue.pop(0)
            for i in range(4):
                xi = x + dx[i]
                yi = y + dy[i]
                if 0 <= xi < N and 0 <= yi < N:
                    if board[yi][xi] == 0:
                        board[yi][xi] = -1
                        queue.append((yi, xi))
                    if board[yi][xi] == 3:
                        result = cnt - 1
                        is_fin = True
                        break

    print('#{0} {1}'.format(case, result))


for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    maze(board, N)
    